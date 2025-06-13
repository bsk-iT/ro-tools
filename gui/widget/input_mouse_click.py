from PyQt6.QtWidgets import QWidget, QToolButton, QHBoxLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

from config.icon import ICON_MOUSE
from service.config_file import CONFIG_FILE, MOUSE_CLICK
from util.widgets import ICON_BTN


class InputMouseClick(QWidget):
    def __init__(self, parent: QWidget, key_base: str, skill_click: bool) -> None:
        super().__init__(parent)
        self.key_base = key_base
        self.skill_click = skill_click
        self.layout = QHBoxLayout(self)
        self.toggle = self._build_toggle()
        self._config_layout()
        self._config_events()

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.toggle)

    def _config_events(self) -> None:
        self.toggle.toggled.connect(self._on_active_delay)
        self._on_active_delay(self.toggle.isChecked())

    def _build_toggle(self) -> QToolButton:
        toggle = QToolButton()
        toggle.setCheckable(True)
        active = CONFIG_FILE.read(self.key_base + MOUSE_CLICK)
        active = self.skill_click if active is None else active
        toggle.setChecked(active if active else False)
        toggle.setIcon(QIcon(ICON_MOUSE))
        toggle.setIconSize(ICON_BTN)
        return toggle

    def _on_active_delay(self, value: bool) -> None:
        self.toggle.setToolTip(f"Mouse click {"ON" if value else "OFF"}")
        CONFIG_FILE.update(self.key_base + MOUSE_CLICK, value)
