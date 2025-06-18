from PyQt6.QtWidgets import QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

from util.widgets import build_painel


class PainelConfig(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self._config_layout()

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        painel = build_painel(self.layout, "Configuração")
        vbox = QVBoxLayout()
        painel.addLayout(vbox)
