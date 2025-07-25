from PySide6.QtWidgets import QWidget, QToolButton, QHBoxLayout, QSizePolicy
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

from config.icon import ICON_REPEAT
from service.config_file import CONFIG_FILE, REPEAT, REPEAT_ACTIVE
from util.widgets import ICON_BTN, build_spinbox_times


class InputRepeatTimes(QWidget):
    def __init__(self, parent: QWidget, key_seq: str) -> None:
        super().__init__(parent)
        self.key_seq = key_seq
        self.layout = QHBoxLayout(self)
        self.spinbox = build_spinbox_times(self.key_seq + REPEAT, "Repetir")
        self.toggle = self._build_toggle()
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
        self._on_active_delay(self.toggle.isChecked())

    def _build_toggle(self) -> QToolButton:
        toggle = QToolButton()
        toggle.setCheckable(True)
        active = CONFIG_FILE.read(self.key_seq + REPEAT_ACTIVE)
        toggle.setChecked(active if active else False)
        toggle.setIcon(QIcon(ICON_REPEAT))
        toggle.setIconSize(ICON_BTN)
        return toggle

    def _on_active_delay(self, value: bool) -> None:
        self.spinbox.setVisible(value)
        self.toggle.setToolTip(f"Executar mais de uma vez o Macro - {"LIGADO" if value else "DESLIGADO"}")
        CONFIG_FILE.update(self.key_seq + REPEAT_ACTIVE, value)
