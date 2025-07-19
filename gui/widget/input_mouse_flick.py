from PySide6.QtWidgets import QWidget, QToolButton, QHBoxLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

from config.icon import ICON_FLICK
from service.config_file import CONFIG_FILE, MOUSE_FLICK
from util.widgets import ICON_BTN


class InputMouseFlick(QWidget):
    def __init__(self, parent: QWidget, key_base: str) -> None:
        super().__init__(parent)
        self.key_base = key_base
        self.layout = QHBoxLayout(self)
        self.toggle = self._build_toggle()
        self._config_layout()
        self._config_events()

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.toggle)

    def _config_events(self) -> None:
        self.toggle.toggled.connect(self._on_active_flick)
        self._on_active_flick(self.toggle.isChecked())

    def _build_toggle(self) -> QToolButton:
        toggle = QToolButton()
        toggle.setCheckable(True)
        active = CONFIG_FILE.read(self.key_base + MOUSE_FLICK)
        toggle.setChecked(active if active else False)
        toggle.setIcon(QIcon(ICON_FLICK))
        toggle.setIconSize(ICON_BTN)
        return toggle

    def _on_active_flick(self, value: bool) -> None:
        self.toggle.setToolTip(f"Mouse flick - {"LIGADO" if value else "DESLIGADO"}")
        CONFIG_FILE.update(self.key_base + MOUSE_FLICK, value)
