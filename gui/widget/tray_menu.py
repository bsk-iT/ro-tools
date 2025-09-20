from typing import Any, Optional
from PySide6.QtWidgets import QMenu, QSystemTrayIcon, QApplication, QWidget
from PySide6.QtGui import QIcon, QAction

from config.app import APP_ICON


class TrayMenu(QSystemTrayIcon):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self._config_layout()

    def _config_layout(self) -> None:
        self.setIcon(QIcon(APP_ICON))
        menu = self._build_context_menu()
        if menu:
            self.setContextMenu(menu)
        self.activated.connect(self._on_click)
        self.show()

    def _build_context_menu(self) -> Optional[QMenu]:
        menu = QMenu()
        parent_widget = self.parent()
        app_instance = QApplication.instance()
        
        if isinstance(parent_widget, QWidget):
            restore_action = self._build_action("Restaurar", parent_widget.showNormal)
        else:
            return None
            
        if app_instance:
            quit_action = self._build_action("Sair", app_instance.quit)
        else:
            return None
            
        if restore_action:
            menu.addAction(restore_action)
        if quit_action:
            menu.addAction(quit_action)
        return menu

    def _build_action(self, name: str, slot: Any) -> Optional[QAction]:
        action = QAction(name, self)
        action.triggered.connect(slot)
        return action

    def _on_click(self, reason: Any) -> None:
        if reason == QSystemTrayIcon.ActivationReason.Trigger:
            parent_widget = self.parent()
            if isinstance(parent_widget, QWidget):
                parent_widget.showNormal()
                parent_widget.activateWindow()
