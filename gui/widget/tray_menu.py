from typing import Any
from PyQt6.QtWidgets import QMenu, QSystemTrayIcon, QApplication, QWidget
from PyQt6.QtGui import QIcon, QAction

from config.app import APP_ICON


class TrayMenu(QSystemTrayIcon):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self._config_layout()

    def _config_layout(self) -> None:
        self.setIcon(QIcon(APP_ICON))
        self.setContextMenu(self._build_context_menu())
        self.activated.connect(self._on_click)
        self.show()

    def _build_context_menu(self) -> None:
        menu = QMenu()
        restore_action = self._build_action("Restaurar", self.parent().showNormal)
        quit_action = self._build_action("Sair", QApplication.instance().quit)
        menu.addAction(restore_action)
        menu.addAction(quit_action)
        return menu

    def _build_action(self, name: str, slot: Any) -> None:
        action = QAction(name, self)
        action.triggered.connect(slot)
        return action

    def _on_click(self, reason: Any) -> None:
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            self.parent().showNormal()
            self.parent().activateWindow()
