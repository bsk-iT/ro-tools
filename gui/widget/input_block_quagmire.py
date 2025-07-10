from PyQt6.QtWidgets import QWidget, QToolButton, QHBoxLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

from config.icon import ICON_BLOCK_QUAGMIRE
from service.config_file import BLOCK_QUAGMIRE, CONFIG_FILE
from util.widgets import ICON_BTN


class InputBlockQuagmire(QWidget):
    def __init__(self, parent: QWidget, key_base: str, block_quagmire: bool) -> None:
        super().__init__(parent)
        self.key_base = key_base
        self.block_quagmire = block_quagmire
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
        active = CONFIG_FILE.read(self.key_base + BLOCK_QUAGMIRE)
        active = self.block_quagmire if active is None else active
        toggle.setChecked(active if active else False)
        toggle.setIcon(QIcon(ICON_BLOCK_QUAGMIRE))
        toggle.setIconSize(ICON_BTN)
        return toggle

    def _on_active_delay(self, value: bool) -> None:
        self.toggle.setToolTip(f"Não utilizar quando estiver dentro do Pântano dos Mortos - {"LIGADO" if value else "DESLIGADO"}")
        CONFIG_FILE.update(self.key_base + BLOCK_QUAGMIRE, value)
