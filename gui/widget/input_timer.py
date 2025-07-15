from PyQt5.QtWidgets import QWidget, QToolButton, QDoubleSpinBox, QHBoxLayout, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from config.app import APP_DELAY, APP_MAX_TIMER, APP_MIN_TIMER
from config.icon import ICON_TIMER
from service.config_file import CONFIG_FILE, COOLDOWN, TIMER_ACTIVE
from util.number import clamp
from util.widgets import ICON_BTN


class InputTimer(QWidget):
    def __init__(self, parent: QWidget, key_seq: str, buff_timer) -> None:
        super().__init__(parent)
        self.key_seq = key_seq
        self.buff_timer = buff_timer
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
        self.spinbox.valueChanged.connect(lambda value: CONFIG_FILE.update(self.key_seq + COOLDOWN, value))
        self._on_active_delay(self.toggle.isChecked())

    def _build_toggle(self) -> QToolButton:
        toggle = QToolButton()
        toggle.setCheckable(True)
        active = CONFIG_FILE.read(self.key_seq + TIMER_ACTIVE)
        toggle.setChecked(active if active else False)
        toggle.setIcon(QIcon(ICON_TIMER))
        toggle.setIconSize(ICON_BTN)
        return toggle

    def _build_spinbox(self) -> QDoubleSpinBox:
        spinbox = QDoubleSpinBox()
        spinbox.setRange(APP_MIN_TIMER, APP_MAX_TIMER)
        timer_s = self._get_timer()
        CONFIG_FILE.update(self.key_seq + COOLDOWN, timer_s)
        spinbox.setValue(timer_s)
        spinbox.setFixedWidth(120)
        spinbox.setSuffix("s")
        return spinbox

    def _get_timer(self) -> float:
        delay = CONFIG_FILE.read(self.key_seq + COOLDOWN)
        if not delay:
            return self.buff_timer or 30
        if delay is not None:
            return clamp(delay, APP_MIN_TIMER, APP_MAX_TIMER)
        return delay

    def _on_active_delay(self, value: bool) -> None:
        self.spinbox.setVisible(value)
        self.toggle.setToolTip(f"Cooldown para reutilizar novamente o Buff - {"LIGADO" if value else "DESLIGADO"}")
        CONFIG_FILE.update(self.key_seq + TIMER_ACTIVE, value)
