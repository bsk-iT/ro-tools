from PyQt6.QtWidgets import QWidget, QToolButton, QHBoxLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

from config.icon import ICON_MOUSE
from service.config_file import CONFIG_FILE
from util.widgets import ICON_BTN


class InputMouseClick(QWidget):
    def __init__(self, parent: QWidget, active_prop: str, active: bool) -> None:
        super().__init__(parent)
        self.active_prop = active_prop
        self.active = active
        self.layout = QHBoxLayout(self)
        self.toggle = self._build_toggle(active_prop)
        self._config_layout()
        self._config_events()

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.toggle)

    def _config_events(self) -> None:
        self.toggle.toggled.connect(self._on_active_delay)
        self._on_active_delay(self.toggle.isChecked())

    def _build_toggle(self, active: str) -> QToolButton:
        toggle = QToolButton()
        active = CONFIG_FILE.read(active) or self.active
        toggle.setCheckable(active)
        toggle.setChecked(active if active else False)
        toggle.setIcon(QIcon(ICON_MOUSE))
        toggle.setIconSize(ICON_BTN)
        return toggle

    def _on_active_delay(self, value: bool) -> None:
        self.toggle.setToolTip(f"Mouse click {"ON" if value else "OFF"}")
        CONFIG_FILE.update(self.active_prop, value)
