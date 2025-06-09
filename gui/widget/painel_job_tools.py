from PyQt6.QtWidgets import QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

from gui.widget.cbox_jobs import CboxJobs
from gui.widget.painel_spawn_skill import PainelSpawnSkill
from util.widgets import build_painel


class PainelJobTools(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self._config_layout()

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        painel = build_painel(self.layout, "Job Tools")
        cbox_job = CboxJobs(self)
        painel.addWidget(cbox_job)
        painel.addWidget(PainelSpawnSkill(self, cbox_job))
