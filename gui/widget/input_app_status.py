import keyboard

from PyQt6.QtWidgets import QToolButton, QVBoxLayout, QHBoxLayout, QLabel, QWidget
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from config.icon import ICON_OFF
from gui.app_controller import APP_CONTROLLER
from gui.widget.input_keybind import InputKeybind
from service.config_file import CONFIG_FILE, KEY_MONITORING
from util.widgets import ICON_STATUS


class InputAppStatus(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QHBoxLayout(self)
        self.status_key = CONFIG_FILE.get_value([KEY_MONITORING])
        self._config_layout()
        if self.status_key:
            self.on_change_keybind(self.status_key)
        self.status_toggle.toggled.connect(lambda value: APP_CONTROLLER.on_togle_monitoring(self.status_toggle, value))
        self.input_keybind.updated_key.connect(self.on_change_keybind)

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        toggle = QToolButton()
        toggle.setCheckable(True)
        toggle.setObjectName("status-btn")
        toggle.setChecked(False)
        toggle.setIcon(QIcon(ICON_OFF))
        toggle.setIconSize(ICON_STATUS)
        toggle.setToolTip("LIGAR/DESLIGAR o monitoramento e eventos do RO Tools")
        self.status_toggle = toggle
        self.input_keybind = InputKeybind(None, KEY_MONITORING)
        vbox = QVBoxLayout()
        vbox.setSpacing(0)
        vbox.addWidget(QLabel("Status"))
        vbox.addWidget(self.input_keybind, alignment=Qt.AlignmentFlag.AlignRight)
        self.layout.addLayout(vbox)
        self.layout.addWidget(self.status_toggle)

    def on_change_keybind(self, key: str):
        if self.status_key != key and not self.status_key is None:
            keyboard.remove_hotkey(self.status_key)
        self.status_key = key
        keyboard.add_hotkey(key, lambda: APP_CONTROLLER.on_togle_monitoring(self.status_toggle, None))
