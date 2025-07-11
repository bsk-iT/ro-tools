from itertools import chain
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon

from config.app import APP_CBOX_WIDTH
from game.buff import EQUIP_BUFFS
from gui.app_controller import APP_CONTROLLER
from service.config_file import ACTIVE, CONFIG_FILE, SKILL_EQUIP, SKILL_SPAWMMER
from util.widgets import build_cbox_category, get_color_by_id


class CboxSkill(QComboBox):

    def __init__(self, parent, resource: str = SKILL_SPAWMMER):
        super().__init__(parent)
        self.setFixedWidth(APP_CBOX_WIDTH)
        self.resource = resource
        self.model = QStandardItemModel()
        self.currentIndexChanged.connect(self._on_changed)
        self.build_cbox(APP_CONTROLLER.job)
        APP_CONTROLLER.updated_job.connect(self.build_cbox)

    def _on_changed(self, index):
        if index < 1:
            return
        (skill, job_id) = self.model.takeItem(index, 0).data()
        self.model.takeRow(index)
        CONFIG_FILE.update_config(True, [job_id, self.resource, skill.id, ACTIVE])
        self._emit_add_event(skill, job_id)
        APP_CONTROLLER.status_toggle.setFocus()

    def add_item(self, skill, job):
        if not skill and not job:
            return self.model.appendRow(QStandardItem(""))
        item = QStandardItem(skill.name)
        color = get_color_by_id(skill.id)
        if color is not None:
            item.setForeground(color)
        item.setIcon(QIcon(skill.icon))
        item.setData((skill, job.id))
        self.model.appendRow(item)

    def _emit_add_event(self, skill, job_id):
        if self.resource == SKILL_EQUIP:
            return APP_CONTROLLER.added_skill_equip.emit(job_id, skill)
        if self.resource == SKILL_SPAWMMER:
            return APP_CONTROLLER.added_skill_spawmmer.emit(job_id, skill)
        APP_CONTROLLER.added_skill_buff.emit(job_id, skill)

    def _get_active_skills(self):
        skills = APP_CONTROLLER.job_buff_skills
        if self.resource == SKILL_EQUIP:
            skills = APP_CONTROLLER.job_equip_skills
        if self.resource == SKILL_SPAWMMER:
            skills = APP_CONTROLLER.job_spawn_skills
        return list(chain.from_iterable(skills.values()))

    def _get_job_skills(self, job):
        if self.resource == SKILL_EQUIP:
            return EQUIP_BUFFS
        if self.resource == SKILL_SPAWMMER:
            return job.spawn_skills
        return job.buff_skills

    def build_cbox(self, job):
        self.model.clear()
        self.currentIndexChanged.disconnect()
        self.add_item(None, None)
        self.setCurrentIndex(0)
        active_skills = self._get_active_skills()
        if self.resource == SKILL_EQUIP:
            self.build_only_itens(job, active_skills)
        else:
            self.build_by_job_category(job, active_skills)
        self.setModel(self.model)
        self.currentIndexChanged.connect(self._on_changed)

    def build_only_itens(self, job, active_skills):
        for skill in self._get_job_skills(job):
            if skill in active_skills:
                continue
            self.add_item(skill, job)

    def build_by_job_category(self, job, active_skills):
        while job is not None:
            build_cbox_category(self.model, job.name)
            for skill in self._get_job_skills(job):
                if skill in active_skills:
                    continue
                self.add_item(skill, job)
            job = job.previous_job
