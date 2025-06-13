from PyQt6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QHBoxLayout, QLabel, QPushButton, QFrame
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

from config.icon import ICON_ARROW_DOWN, ICON_ARROW_RIGHT, ICON_DELETE
from game.macro import MACRO_MAP
from gui.app_controller import APP_CONTROLLER
from gui.widget.cbox_jobs import CboxJobs
from gui.widget.cbox_macro import CboxMacro
from gui.widget.input_delay import InputDelay
from gui.widget.input_keybind import InputKeybind
from service.config_file import ACTIVE, CONFIG_FILE, KEY, MACRO
from util.widgets import build_action_badge, build_badge_btn, build_hr, build_icon, build_label_info, build_scroll_vbox, clear_layout


MAX_HOTKEY = 10
DEFAULT_SIZE = 25


class PainelJobMacro(QWidget):
    def __init__(self, parent, cbox_jobs: CboxJobs):
        super().__init__(parent)
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self.cbox_macro: CboxMacro = CboxMacro(self, cbox_jobs)
        cbox_jobs.updated_job.connect(self.update_macros)
        self._config_layout()

    def _config_layout(self):
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.layout.addWidget(self.cbox_macro)
        self.cbox_macro.updated_macro.connect(self.update_macros)
        self.update_macros()

    def update_macros(self):
        clear_layout(self.layout.takeAt(1))
        job = APP_CONTROLLER.job
        (vbox, scroll) = build_scroll_vbox()
        while job is not None:
            has_macro = False
            active_macros = APP_CONTROLLER.job_macros[job.id]
            vbox_macro = QVBoxLayout()
            vbox_macro.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
            for macro in filter(lambda macro: macro in active_macros, MACRO_MAP.values()):
                has_macro = True
                vbox_macro.addWidget(self._build_macro_inputs(macro, job.id))
            if has_macro:
                vbox.addWidget(build_label_info(job.name))
                vbox.addLayout(vbox_macro)
            job = job.previous_job
        self.layout.addWidget(scroll)

    def _build_macro_inputs(self, macro, job_id):
        widget = QWidget()
        key_seq = f"{MACRO}:{job_id}:{macro.id}:"
        vbox = QVBoxLayout(widget)
        vbox.setSpacing(10)
        vbox.addLayout(self._build_title_macro(key_seq, macro))
        vbox.addLayout(self._build_frame_input_delay(key_seq, macro, job_id))
        vbox.addWidget(build_hr())
        return widget

    def _build_frame_input_delay(self, key_seq, macro, job_id):
        hbox = QHBoxLayout()
        hbox.setAlignment(Qt.AlignmentFlag.AlignLeft)
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSpacing(0)
        for index in range(MAX_HOTKEY + 1):
            is_finished = False
            (vbox, is_finished) = self._add_vbox_inputs(key_seq, index, macro)
            if vbox:
                hbox.addLayout(vbox)
            if is_finished:
                break
            else:
                hbox.addWidget(self._build_icon_right())
        return hbox

    def _build_icon_right(self):
        icon_right = QLabel()
        icon_right.setPixmap(QPixmap(ICON_ARROW_RIGHT).scaled(25, 65))
        return icon_right

    def _add_vbox_inputs(self, key_seq, index, macro):
        new_key_seq = f"{key_seq}seq_{index}_"
        is_active = CONFIG_FILE.read(new_key_seq + ACTIVE)
        next_is_active = CONFIG_FILE.read(f"{key_seq}seq_{index + 1}_" + ACTIVE)
        is_last_key = index == MAX_HOTKEY - 1
        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignBottom)
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.setSpacing(0)
        if index > 0 and not is_active:
            vbox.addWidget(self._build_add_btn(new_key_seq))
            self._build_empty_widgets(vbox)
            return (vbox, True)
        if index == 0:
            self._build_empty_widgets(vbox)
            vbox.addWidget(InputDelay(self, new_key_seq))
            return (vbox, False)
        vbox.addWidget(self._build_input_keybind(new_key_seq, next_is_active))
        if not is_last_key:
            vbox.addWidget(build_icon(ICON_ARROW_DOWN))
            vbox.addWidget(InputDelay(self, new_key_seq))
        else:
            self._build_empty_widgets(vbox)
        return (vbox, is_last_key)

    def _build_add_btn(self, new_key_seq):
        add_btn = QPushButton("+")
        add_btn.setContentsMargins(0, 0, 0, 0)
        add_btn.setStyleSheet("background-color: green;")
        add_btn.clicked.connect(lambda: self._on_add_remove_keybind(new_key_seq, True))
        add_btn.setFixedSize(DEFAULT_SIZE + 4, DEFAULT_SIZE + 4)
        return add_btn

    def _build_btn_remove_input_keybind(self, key_seq, parent):
        btn = build_badge_btn(parent, ICON_DELETE)
        btn.clicked.connect(lambda: self._on_add_remove_keybind(key_seq, False))

    def _on_add_remove_keybind(self, key_seq, active):
        CONFIG_FILE.update(key_seq + ACTIVE, active)
        self.update_macros()

    def _build_btn_remove_macro(self, key_seq, macro, parent):
        btn = build_badge_btn(parent, ICON_DELETE)
        btn.clicked.connect(lambda: self._on_add_remove_macro(key_seq, macro, False))

    def _on_add_remove_macro(self, key_seq, macro, active):
        CONFIG_FILE.update(key_seq + ACTIVE, active)
        APP_CONTROLLER.update_macros(macro, active)
        self.cbox_macro.build_cbox()
        self.update_macros()

    def _build_input_keybind(self, new_key_seq, next_is_active) -> QFrame:
        (widget, layout) = build_action_badge()
        layout.addWidget(InputKeybind(widget, new_key_seq + KEY))
        if not next_is_active:
            self._build_btn_remove_input_keybind(new_key_seq, widget)
        return widget

    def _build_empty_widgets(self, vbox):
        label = QLabel()
        label.setFixedSize(DEFAULT_SIZE + 4, DEFAULT_SIZE + 4)
        vbox.addWidget(label)
        vbox.addWidget(label)

    def _build_title_macro(self, key_seq, macro):
        (widget, layout) = build_action_badge()
        icon = build_icon(macro.icon, None, 25, widget)
        icon.setFixedSize(DEFAULT_SIZE, DEFAULT_SIZE)
        layout.addWidget(icon)
        self._build_btn_remove_macro(key_seq, macro, widget)

        hbox = QHBoxLayout()
        hbox.setSpacing(0)
        hbox.setContentsMargins(0, 0, 0, 0)
        label = QLabel(macro.name)
        label.setObjectName(macro.id)
        hbox.addWidget(widget)
        hbox.addWidget(label)
        return hbox
