from PyQt6.QtWidgets import QComboBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt6.QtCore import pyqtSignal

from config.app import APP_CBOX_WIDTH
from game.jobs import JOB_GROUPS, Job
from gui.app_controller import APP_CONTROLLER
from util.widgets import build_cbox_category


class CboxJobs(QComboBox):

    updated_job = pyqtSignal(Job)

    def __init__(self, parent):
        super().__init__(parent)
        self.model: QStandardItemModel = QStandardItemModel()
        self.setFixedWidth(APP_CBOX_WIDTH)
        self.build_cbox()
        self.currentIndexChanged.connect(lambda index: APP_CONTROLLER.on_change_job(self, index))

    def build_cbox(self):
        for group in JOB_GROUPS:
            build_cbox_category(self.model, group)
            for job in JOB_GROUPS[group]:
                self._add_item(job)
        self.setModel(self.model)

    def _add_item(self, job: Job):
        item = QStandardItem(job.name)
        item.setIcon(QIcon(job.icon))
        item.setData(job)
        self.model.appendRow(item)
