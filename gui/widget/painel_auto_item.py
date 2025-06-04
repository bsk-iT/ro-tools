from PyQt6.QtWidgets import QVBoxLayout, QWidget, QSizePolicy
from PyQt6.QtCore import Qt

from util.widgets import build_painel


class PainelAutoItem(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self._config_layout()

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        build_painel(self.layout, "Auto Item")
