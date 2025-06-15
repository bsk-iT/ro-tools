from PyQt6.QtWidgets import QVBoxLayout, QWidget, QTabWidget
from PyQt6.QtCore import Qt

from gui.widget.cbox_jobs import CboxJobs
from gui.widget.painel_job_skill_buff import PainelJobSkillBuff
from gui.widget.painel_job_hotkey import PainelJobHotkey
from gui.widget.painel_job_skill_equip import PainelJobEquipBuff
from gui.widget.painel_job_skill_spawmmer import PainelJobSkillSpawmmer
from gui.widget.painel_job_macro import PainelJobMacro
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
        tab_panel.addTab(PainelJobSkillSpawmmer(self), "Skill Spawmmer")
        tab_panel.addTab(PainelJobSkillBuff(self), "Skill Buff")
        tab_panel.addTab(PainelJobEquipBuff(self), "Equip. Buff")
        tab_panel.addTab(PainelJobHotkey(self), "Hotkey")
        tab_panel.addTab(PainelJobMacro(self), "Macro")
        painel.addWidget(tab_panel)
