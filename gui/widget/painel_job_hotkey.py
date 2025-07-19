from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QHBoxLayout, QFrame, QPushButton, QLabel
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon

from config.icon import ICON_DELETE
from game.macro import MACRO_MAP, Macro
from gui.app_controller import APP_CONTROLLER
from gui.widget.cbox_macro import CboxMacro
from gui.widget.input_keybind import InputKeybind
from service.config_file import ACTIVE, CONFIG_FILE, HOTKEY, KEY
from util.widgets import build_hr, build_icon, build_label_info, build_scroll_vbox, clear_layout


class PainelJobHotkey(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self.cbox_macro: CboxMacro = CboxMacro(self, HOTKEY)
        self._config_layout()
        APP_CONTROLLER.updated_job.connect(self.update_hotkeys)

    def _config_layout(self):
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.layout.setSpacing(10)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.layout.addWidget(self.cbox_macro)
        APP_CONTROLLER.added_hotkey.connect(self._on_add_hotkey)
        self.update_hotkeys(APP_CONTROLLER.job)

    def update_hotkeys(self, job):
        clear_layout(self.layout.takeAt(1))
        (vbox, scroll) = build_scroll_vbox()
        while job is not None:
            has_hotkey = False
            active_hotkeys = APP_CONTROLLER.job_hotkeys[job.id]
            vbox_hotkey = QVBoxLayout()
            vbox_hotkey.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
            for macro in MACRO_MAP.values():
                if macro.id not in [a_macro.id for a_macro in active_hotkeys]:
                    continue
                has_hotkey = True
                vbox_hotkey.addWidget(self._build_hotkey_inputs(macro, job.id))
            if has_hotkey:
                vbox.addWidget(build_label_info(job.name))
                vbox.addLayout(vbox_hotkey)
            job = job.previous_job
        self.layout.addWidget(scroll)

    def _build_hotkey_inputs(self, macro: Macro, job_id):
        widget = QWidget()
        vbox = QVBoxLayout(widget)
        hbox = QHBoxLayout()
        hbox.setSpacing(5)
        hbox.setAlignment(Qt.AlignmentFlag.AlignLeft)
        hbox.addWidget(self._build_hotkey_icon(macro, job_id))
        key_base = f"{job_id}:{HOTKEY}:{macro.id}:"
        label = QLabel(macro.name)
        label.setObjectName(macro.id)
        hbox.addWidget(label)
        hbox.addWidget(InputKeybind(self, key_base + KEY, True))
        vbox.addLayout(hbox)
        vbox.addWidget(build_hr())
        return widget

    def _build_hotkey_icon(self, macro: Macro, job_id) -> QFrame:
        frame = QFrame()
        icon = build_icon(macro.icon, macro.id, 25, frame)
        icon.move(9, 9)
        frame.setFixedSize(35, 40)
        btn_delete = QPushButton(frame)
        btn_delete.move(0, 0)
        btn_delete.setIcon(QIcon(ICON_DELETE))
        btn_delete.setIconSize(QSize(10, 10))
        btn_delete.setContentsMargins(0, 0, 0, 0)
        btn_delete.clicked.connect(lambda: self._on_remove_hotkey(job_id, macro))
        btn_delete.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        return frame

    def _active_hotkey(self, job_id, macro: Macro, active=True):
        self.update_hotkeys(APP_CONTROLLER.job)
        CONFIG_FILE.update_config(active, [job_id, HOTKEY, macro.id, ACTIVE])
        self.cbox_macro.build_cbox(APP_CONTROLLER.job)

    def _on_add_hotkey(self, job_id, macro: Macro):
        APP_CONTROLLER.update_hotkey(job_id, macro, True)
        self._active_hotkey(job_id, macro)
        APP_CONTROLLER.status_toggle.setFocus()

    def _on_remove_hotkey(self, job_id, macro: Macro):
        APP_CONTROLLER.update_hotkey(job_id, macro, False)
        self._active_hotkey(job_id, macro, False)
