from PyQt6.QtWidgets import QWidget, QToolButton, QDoubleSpinBox, QHBoxLayout, QSizePolicy
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

from config.app import APP_DELAY, APP_MAX_DELAY, APP_MIN_DELAY
from config.icon import ICON_QUICK
from service.config_file import CONFIG_FILE, DELAY, DELAY_ACTIVE
from util.number import clamp
from util.widgets import ICON_BTN


class InputDelay(QWidget):
    def __init__(self, parent: QWidget, key_seq: str) -> None:
        super().__init__(parent)
        self.key_seq = key_seq
        self.layout = QHBoxLayout(self)
        self.toggle = self._build_toggle()
        self.spinbox = self._build_spinbox()
        self._config_layout()
        self._config_events()

    def _config_layout(self) -> None:
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.layout.setSpacing(5)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.toggle)
        self.layout.addWidget(self.spinbox)

    def _config_events(self) -> None:
        self.toggle.toggled.connect(self._on_active_delay)
        self.spinbox.valueChanged.connect(lambda value: CONFIG_FILE.update(self.key_seq + DELAY, value))
        self._on_active_delay(self.toggle.isChecked())

    def _build_toggle(self) -> QToolButton:
        toggle = QToolButton()
        toggle.setCheckable(True)
        active = CONFIG_FILE.read(self.key_seq + DELAY_ACTIVE)
        toggle.setChecked(active if active else False)
        toggle.setIcon(QIcon(ICON_QUICK))
        toggle.setIconSize(ICON_BTN)
        toggle.setToolTip("Delay de uso em segundos")
        return toggle

    def _build_spinbox(self) -> QDoubleSpinBox:
        spinbox = QDoubleSpinBox()
        spinbox.setRange(APP_MIN_DELAY, APP_MAX_DELAY)
        delay_s = self._get_delay()
        spinbox.setValue(delay_s)
        spinbox.setFixedWidth(95)
        spinbox.setSuffix("s")
        return spinbox

    def _get_delay(self) -> float:
        delay = CONFIG_FILE.read(self.key_seq + DELAY)
        if not delay:
            return APP_DELAY
        if delay is not None:
            return clamp(delay, APP_MIN_DELAY, APP_MAX_DELAY)
        return delay

    def _on_active_delay(self, value: bool) -> None:
        self.spinbox.setVisible(value)
        CONFIG_FILE.update(self.key_seq + DELAY_ACTIVE, value)
