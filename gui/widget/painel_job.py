from PyQt6.QtWidgets import QVBoxLayout, QWidget, QTabWidget
from PyQt6.QtCore import Qt

from gui.widget.cbox_jobs import CboxJobs
from gui.widget.painel_job_buff import PainelJobBuff
from gui.widget.painel_job_spawn_skill import PainelJobSpawnSkill
from util.widgets import build_painel


class PainelJob(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self._config_layout()

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        painel = build_painel(self.layout, "Job Tools")
        cbox_job = CboxJobs(self)
        painel.addWidget(cbox_job)
        tab_panel = QTabWidget()
        tab_panel.addTab(PainelJobSpawnSkill(self, cbox_job), "Skill Spawnner")
        tab_panel.addTab(PainelJobBuff(self, cbox_job), "Buff")
        painel.addWidget(tab_panel)
