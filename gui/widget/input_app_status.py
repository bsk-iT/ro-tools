from PySide6.QtWidgets import QToolButton, QVBoxLayout, QHBoxLayout, QLabel, QWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from config.icon import ICON_OFF
from gui.app_controller import APP_CONTROLLER
from gui.widget.input_keybind import InputKeybind
from service.config_file import CONFIG_FILE, KEY_MONITORING
from util.widgets import ICON_STATUS


class InputAppStatus(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QHBoxLayout(self)
        self.status_key = CONFIG_FILE.read(KEY_MONITORING)
        self._config_layout()
        self.status_toggle.toggled.connect(lambda value: APP_CONTROLLER.on_togle_monitoring(value))
        APP_CONTROLLER.status_toggle = self.status_toggle

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
        self.input_keybind = InputKeybind(None, KEY_MONITORING, True)
        vbox = QVBoxLayout()
        vbox.setSpacing(0)
        vbox.addWidget(QLabel("Atalho"))
        vbox.addWidget(self.input_keybind, alignment=Qt.AlignmentFlag.AlignRight)
        self.layout.addLayout(vbox)
        self.layout.addWidget(self.status_toggle)
