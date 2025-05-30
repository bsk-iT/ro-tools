from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QEvent

from config.app import APP_NAME, APP_WIDTH, APP_HEIGHT, APP_ICON
from gui.central_widget import CentralWidget
from gui.widget.tray_menu import TrayMenu
from service.auto_pot import AUTO_POT
from service.file import CONFIG_FILE


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self._config_layout()

    def closeEvent(self, event: QEvent) -> None:
        AUTO_POT.stop()
        CONFIG_FILE.save()
        event.accept()

    def changeEvent(self, event: QEvent) -> None:
        if event.type() == QEvent.Type.WindowStateChange and self.isMinimized():
            self.hide()
        super().changeEvent(event)

    def _config_layout(self) -> None:
        self.setWindowTitle(APP_NAME)
        self.setFixedSize(APP_WIDTH, APP_HEIGHT)
        self.setWindowIcon(QIcon(APP_ICON))
        self.setCentralWidget(CentralWidget(self))
        self.tray_menu = TrayMenu(self)
