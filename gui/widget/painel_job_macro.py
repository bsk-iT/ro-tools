import copy
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QHBoxLayout, QLabel, QPushButton, QFrame
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap, QIcon

from config.icon import ICON_ARROW_DOWN, ICON_ARROW_RIGHT, ICON_DELETE, PATH_ITEM, get_image
from game.macro import MACRO_MAP, MAX_HOTKEY
from gui.app_controller import APP_CONTROLLER
from gui.widget.cbox_macro import CboxMacro
from gui.widget.input_delay import InputDelay
from gui.widget.input_keybind import InputKeybind
from service.config_file import ACTIVE, CONFIG_FILE, KEY, KNIFE_KEY, MACRO, VIOLIN_KEY
from util.widgets import build_action_badge, build_badge_btn, build_hr, build_icon, build_label_info, build_scroll_vbox, clear_layout


DEFAULT_SIZE = 25


class PainelJobMacro(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self.cbox_macro: CboxMacro = CboxMacro(self)
        self._config_layout()
        APP_CONTROLLER.updated_job.connect(self.update_macros)

    def _config_layout(self):
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.layout.setSpacing(10)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.layout.addWidget(self.cbox_macro)
        APP_CONTROLLER.added_macro.connect(self._on_add_macro)
        self.update_macros()

    def update_macros(self, _=None):
        clear_layout(self.layout.takeAt(1))
        job = copy.deepcopy(APP_CONTROLLER.job)
        (vbox, scroll) = build_scroll_vbox()
        while job is not None:
            has_macro = False
            active_macros = APP_CONTROLLER.job_macros[job.id]
            vbox_macro = QVBoxLayout()
            vbox_macro.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
            for macro in MACRO_MAP.values():
                if macro.id not in [a_macro.id for a_macro in active_macros]:
                    continue
                has_macro = True
                vbox_macro.addWidget(self._build_macro_inputs(macro, job.id))
            if has_macro:
                vbox.addWidget(build_label_info(job.name))
                vbox.addLayout(vbox_macro)
            job = job.previous_job
        self.layout.addWidget(scroll)

    def _build_macro_inputs(self, macro, job_id):
        widget = QWidget()
        key_seq = f"{job_id}:{MACRO}:{macro.id}:"
        vbox = QVBoxLayout(widget)
        vbox.setSpacing(10)
        vbox.addWidget(self._build_title_macro(job_id, key_seq, macro))
        vbox.addLayout(self._build_frame_input_delay(key_seq, macro))
        vbox.addWidget(build_hr())
        return widget

    def _build_frame_input_delay(self, key_seq, macro):
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

    def _build_btn_remove_macro(self, job_id, key_seq, macro):
        frame = QFrame()
        icon = build_icon(macro.icon, macro.id, 25, frame)
        icon.move(9, 9)
        frame.setFixedSize(35, 40)
        btn_delete = QPushButton(frame)
        btn_delete.move(0, 0)
        btn_delete.setIcon(QIcon(ICON_DELETE))
        btn_delete.setIconSize(QSize(10, 10))
        btn_delete.setContentsMargins(0, 0, 0, 0)
        btn_delete.clicked.connect(lambda: self._on_remove_macro(job_id, key_seq, macro))
        btn_delete.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        return frame

    def _on_remove_macro(self, job_id, key_seq, macro):
        CONFIG_FILE.update(key_seq + ACTIVE, False)
        APP_CONTROLLER.job_macros[job_id].remove(macro)
        APP_CONTROLLER.removed_macro.emit(macro)
        self.cbox_macro.build_cbox(APP_CONTROLLER.job)
        self.update_macros()

    def _on_add_macro(self, job_id, macro):
        CONFIG_FILE.update_config(True, [job_id, MACRO, macro.id, ACTIVE])
        APP_CONTROLLER.job_macros[job_id].append(macro)
        self.update_macros()
        APP_CONTROLLER.add_macro_select.emit(job_id, macro)

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

    def _build_title_macro(self, job_id, key_seq, macro):
        widget = QWidget()
        widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        hbox = QHBoxLayout(widget)
        hbox.setSpacing(0)
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox_title = QHBoxLayout()
        hbox_title.setSpacing(5)
        hbox_title.setContentsMargins(0, 0, 0, 0)
        hbox_title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        label = QLabel(macro.name)
        label.setObjectName(macro.id)
        hbox_title.addWidget(self._build_btn_remove_macro(job_id, key_seq, macro))
        hbox_title.addWidget(label)
        hbox.addLayout(hbox_title)
        if "song" in macro.id:
            hbox.addLayout(self._build_knife_violin_keys(key_seq))
        return widget

    def _build_knife_violin_keys(self, key_seq):
        hbox_weapon = QHBoxLayout()
        hbox_weapon.setSpacing(5)
        hbox_weapon.setContentsMargins(0, 0, 0, 0)
        hbox_weapon.setAlignment(Qt.AlignmentFlag.AlignRight)
        hbox_weapon.addWidget(build_icon(get_image(PATH_ITEM, "violin")))
        hbox_weapon.addWidget(InputKeybind(self, key_seq + VIOLIN_KEY))
        hbox_weapon.addWidget(build_icon(get_image(PATH_ITEM, "novice_knife")))
        hbox_weapon.addWidget(InputKeybind(self, key_seq + KNIFE_KEY))
        return hbox_weapon
