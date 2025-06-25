from PyQt6.QtWidgets import QVBoxLayout, QWidget, QPlainTextEdit, QCheckBox
from PyQt6.QtCore import Qt

from gui.app_controller import APP_CONTROLLER
from service.config_file import CONFIG_FILE, DEBUG_ACTIVE


class PainelDebug(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self.terminal = QPlainTextEdit()
        self._config_layout()
        APP_CONTROLLER.debug.connect(self._update_terminal)

    def _update_terminal(self, msg):
        self.terminal.setPlainText(msg)

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.setSpacing(15)
        self.terminal.setReadOnly(True)
        self.layout.addWidget(self._build_check_debug())
        self.layout.addWidget(self.terminal)

    def _build_check_debug(self):
        check_debug = QCheckBox("Debug habilitado?")
        active = CONFIG_FILE.read(DEBUG_ACTIVE)
        check_debug.setChecked(True if active else False)
        check_debug.checkStateChanged.connect(self._update_check_debug)
        return check_debug

    def _update_check_debug(self, state):
        CONFIG_FILE.update(DEBUG_ACTIVE, state.value == 2)
