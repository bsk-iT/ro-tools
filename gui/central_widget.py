from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt

from gui.widget.input_app_status import InputAppStatus
from gui.widget.cbox_process import CboxProcess
from gui.widget.painel_auto_item import PainelAutoItem
from gui.widget.painel_auto_pot import PainelAutoPot
from gui.widget.painel_job_tools import PainelJobTools


class CentralWidget(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.cbox_process = CboxProcess(self)
        self.gui_autopot = PainelAutoPot(self)
        self._config_layout()

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        header_hbox = QHBoxLayout()
        header_hbox.addWidget(self.cbox_process)
        header_hbox.addWidget(InputAppStatus(self))
        self.layout.addLayout(header_hbox)
        body_hbox = QHBoxLayout()
        body_hbox.addWidget(self.gui_autopot, alignment=Qt.AlignmentFlag.AlignLeft)
        body_hbox.addWidget(PainelJobTools(self))
        self.layout.addLayout(body_hbox)
        self.layout.addWidget(PainelAutoItem(self))
