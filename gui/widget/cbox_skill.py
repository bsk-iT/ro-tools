from PyQt6.QtWidgets import QComboBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt6.QtCore import pyqtSignal

from config.app import APP_CBOX_WIDTH
from gui.app_controller import APP_CONTROLLER
from gui.widget.cbox_jobs import CboxJobs
from service.config_file import ACTIVE, CONFIG_FILE, SKIL_SPAWNNER
from util.widgets import build_cbox_category


class CboxSkill(QComboBox):

    updated_skill = pyqtSignal(object, str)

    def __init__(self, parent, cbox_job: CboxJobs, resource: str = SKIL_SPAWNNER):
        super().__init__(parent)
        self.setFixedWidth(APP_CBOX_WIDTH)
        self.resource = resource
        self.model = QStandardItemModel()
        self.currentIndexChanged.connect(self._on_changed)
        self.build_cbox(APP_CONTROLLER.job)
        cbox_job.updated_job.connect(self.build_cbox)

    def _on_changed(self, index):
        if index == -1:
            return
        (skill, job_id) = self.model.takeItem(index, 0).data()
        self.model.takeRow(index)
        CONFIG_FILE.update_config(True, [self.resource, job_id, skill.id, ACTIVE])
        self.updated_skill.emit(skill, job_id)

    def add_item(self, skill, job):
        item = QStandardItem(skill.name)
        item.setIcon(QIcon(skill.icon))
        item.setData((skill, job.id))
        self.model.appendRow(item)

    def build_cbox(self, job):
        self.model.clear()
        self.currentIndexChanged.disconnect()
        while job is not None:
            build_cbox_category(self.model, job.name)
            skill_list = job.spawn_skills if self.resource == SKIL_SPAWNNER else job.buff_skill
            for skill in skill_list:
                if skill in APP_CONTROLLER.spawn_skills:
                    continue
                self.add_item(skill, job)
            job = job.previous_job
        self.setModel(self.model)
        self.currentIndexChanged.connect(self._on_changed)
