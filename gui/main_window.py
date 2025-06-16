from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QEvent

from config.app import APP_HEIGHT, APP_NAME, APP_ICON, APP_WIDTH
from events.game_event import GAME_EVENT
from gui.central_widget import CentralWidget
from gui.widget.tray_menu import TrayMenu


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self._config_layout()

    def closeEvent(self, event: QEvent) -> None:
        GAME_EVENT.stop()
        event.accept()

    def changeEvent(self, event: QEvent) -> None:
        if event.type() == QEvent.Type.WindowStateChange and self.isMinimized():
            self.hide()
        super().changeEvent(event)

    def _config_layout(self) -> None:
        self.setWindowTitle(APP_NAME)
        # self.setFixedSize(APP_WIDTH, APP_HEIGHT)
        self.setWindowIcon(QIcon(APP_ICON))
        self.setCentralWidget(CentralWidget(self))
        self.tray_menu = TrayMenu(self)
