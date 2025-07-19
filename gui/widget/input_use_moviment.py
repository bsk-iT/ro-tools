from PySide6.QtWidgets import QWidget, QToolButton, QHBoxLayout, QSizePolicy
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

from config.icon import ICON_FOOTPRINT
from service.config_file import CONFIG_FILE, MOVIMENT_CELLS, USE_MOVIMENT
from util.widgets import ICON_BTN, build_spinbox_cells


class InputUseMoviment(QWidget):
    def __init__(self, parent: QWidget, key_base: str) -> None:
        super().__init__(parent)
        self.key_base = key_base
        self.layout = QHBoxLayout(self)
        self.spinbox = build_spinbox_cells(self.key_base + MOVIMENT_CELLS)
        self.toggle = self._build_toggle()
        self._config_layout()
        self._config_events()

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.toggle)
        self.layout.addWidget(self.spinbox)

    def _config_events(self) -> None:
        self.toggle.toggled.connect(self._on_active_use_moviment)
        self._on_active_use_moviment(self.toggle.isChecked())

    def _build_toggle(self) -> QToolButton:
        toggle = QToolButton()
        toggle.setCheckable(True)
        active = CONFIG_FILE.read(self.key_base + USE_MOVIMENT)
        toggle.setChecked(active if active else False)
        toggle.setIcon(QIcon(ICON_FOOTPRINT))
        toggle.setIconSize(ICON_BTN)
        return toggle

    def _on_active_use_moviment(self, value: bool) -> None:
        self.spinbox.setVisible(value)
        self.toggle.setToolTip(f"Utilizar quando andar X células - {"LIGADO" if value else "DESLIGADO"}")
        CONFIG_FILE.update(self.key_base + USE_MOVIMENT, value)
