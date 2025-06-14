from itertools import chain
from PyQt6.QtWidgets import QComboBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QIcon

from config.app import APP_CBOX_WIDTH
from gui.app_controller import APP_CONTROLLER
from service.config_file import ACTIVE, CONFIG_FILE, SKILL_SPAWMMER
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
        CONFIG_FILE.update_config(True, [self.resource, job_id, skill.id, ACTIVE])
        APP_CONTROLLER.added_skill.emit(skill, job_id)
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

    def build_cbox(self, job):
        self.model.clear()
        self.currentIndexChanged.disconnect()
        self.add_item(None, None)
        self.setCurrentIndex(0)
        active_spawn_skills = list(chain.from_iterable(APP_CONTROLLER.job_spawn_skills.values()))
        while job is not None:
            build_cbox_category(self.model, job.name)
            skill_list = job.spawn_skills if self.resource == SKILL_SPAWMMER else job.buff_skill
            for skill in skill_list:
                if skill in active_spawn_skills:
                    continue
                self.add_item(skill, job)
            job = job.previous_job
        self.setModel(self.model)
        self.currentIndexChanged.connect(self._on_changed)
