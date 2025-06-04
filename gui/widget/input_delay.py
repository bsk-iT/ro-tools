from PyQt6.QtWidgets import QWidget, QToolButton, QDoubleSpinBox, QHBoxLayout
from PyQt6.QtGui import QIcon

from config.app import APP_DELAY, APP_MAX_DELAY, APP_MIN_DELAY
from config.icon import ICON_QUICK
from service.file import CONFIG_FILE
from util.number import clamp
from util.widgets import ICON_BTN


class InputDelay(QWidget):
    def __init__(self, parent: QWidget, active: str, delay: str) -> None:
        super().__init__(parent)
        self.active = active
        self.delay = delay
        self.layout = QHBoxLayout(self)
        self.toggle = self._build_toggle(active)
        self.spinbox = self._build_spinbox(delay)
        self._config_layout()
        self._config_events()

    def _config_layout(self) -> None:
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.toggle)
        self.layout.addWidget(self.spinbox)

    def _config_events(self) -> None:
        self.toggle.toggled.connect(self._on_active_delay)
        self.spinbox.valueChanged.connect(lambda value: CONFIG_FILE.update(self.delay, value))
        self._on_active_delay(self.toggle.isChecked())

    def _build_toggle(self, active: str) -> QToolButton:
        toggle = QToolButton()
        toggle.setCheckable(True)
        active = CONFIG_FILE.read(active)
        toggle.setChecked(active if active else False)
        toggle.setIcon(QIcon(ICON_QUICK))
        toggle.setIconSize(ICON_BTN)
        toggle.setToolTip("Delay de uso em segundos")
        return toggle

    def _build_spinbox(self, delay: str) -> QDoubleSpinBox:
        spinbox = QDoubleSpinBox()
        spinbox.setRange(APP_MIN_DELAY, APP_MAX_DELAY)
        delay_s = self._get_delay(delay)
        spinbox.setValue(delay_s)
        spinbox.setFixedWidth(95)
        spinbox.setSuffix("s")
        return spinbox

    def _get_delay(self, delay: str) -> float:
        delay_config = CONFIG_FILE.read(delay)
        if not delay_config:
            return APP_DELAY
        if delay_config is not None:
            return clamp(delay_config, APP_MIN_DELAY, APP_MAX_DELAY)
        return delay_config

    def _on_active_delay(self, value: bool) -> None:
        self.spinbox.setVisible(value)
        CONFIG_FILE.update(self.active, value)
