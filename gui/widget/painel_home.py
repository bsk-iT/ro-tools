from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTabWidget
from PyQt5.QtCore import Qt

from gui.widget.cbox_jobs import CboxJobs
from gui.widget.painel_auto_element import PainelAutoElement
from gui.widget.painel_auto_item_buff import PainelAutoItemBuff
from gui.widget.painel_auto_item_debuff import PainelAutoItemDebuff
from gui.widget.painel_auto_item_hp_sp import PainelAutoItemHpSp
from gui.widget.painel_job_hotkey import PainelJobHotkey
from gui.widget.painel_job_macro import PainelJobMacro
from gui.widget.painel_job_skill_buff import PainelJobSkillBuff
from gui.widget.painel_job_skill_equip import PainelJobEquipBuff
from gui.widget.painel_job_skill_spawmmer import PainelJobSkillSpawmmer


class PainelHome(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self._config_layout()

    def _config_layout(self):
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.setContentsMargins(15, 15, 0, 0)
        self.layout.setSpacing(15)
        self.layout.addLayout(self._build_cbox_job())
        self.layout.addWidget(self._build_tab_events())

    def _build_cbox_job(self):
        vbox = QVBoxLayout()
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.setSpacing(0)
        vbox.addWidget(QLabel("Select the job:"))
        vbox.addWidget(CboxJobs(self))
        return vbox

    def _build_tab_events(self):
        tab_panel = QTabWidget()
        tab_panel.addTab(PainelAutoItemHpSp(self), "HP/SP")
        tab_panel.addTab(PainelAutoItemBuff(self), "Stuffs")
        tab_panel.addTab(PainelAutoItemDebuff(self), "Debuff")
        tab_panel.addTab(PainelJobSkillSpawmmer(self), "Skill Spawmmer")
        tab_panel.addTab(PainelJobSkillBuff(self), "Skill Buff")
        tab_panel.addTab(PainelJobEquipBuff(self), "Equip. Buff")
        tab_panel.addTab(PainelAutoElement(self), "Auto Element")
        tab_panel.addTab(PainelJobHotkey(self), "Hotkey")
        tab_panel.addTab(PainelJobMacro(self), "Macro")
        return tab_panel
