from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import Qt

from gui.widget.cbox_process import CboxProcess
from gui.widget.painel_auto_pot import PainelAutoPot


class CentralWidget(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.cbox_process = CboxProcess(self)
        self.gui_autopot = PainelAutoPot(self)
        self._config_layout()

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.layout.addWidget(self.cbox_process)
        self.layout.addWidget(self.gui_autopot)
