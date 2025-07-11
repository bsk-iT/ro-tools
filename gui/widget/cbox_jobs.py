from PyQt5.QtWidgets import QComboBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon

from config.app import APP_CBOX_WIDTH
from game.jobs import JOB_GROUPS, Job
from gui.app_controller import APP_CONTROLLER
from util.widgets import build_cbox_category


class CboxJobs(QComboBox):

    def __init__(self, parent):
        super().__init__(parent)
        self.model: QStandardItemModel = QStandardItemModel()
        self.setFixedWidth(APP_CBOX_WIDTH)
        self.build_cbox()
        self.currentIndexChanged.connect(self.on_change_job)
        APP_CONTROLLER.updated_job.connect(self.set_current_job)

    def set_current_job(self, job: Job):
        index = self.model.findItems(job.name).pop().row()
        self.setCurrentIndex(index)

    def build_cbox(self):
        for group in JOB_GROUPS:
            build_cbox_category(self.model, group)
            for job in JOB_GROUPS[group]:
                self._add_item(job)
        self.setModel(self.model)

    def on_change_job(self, index):
        job = self.model.item(index, 0).data()
        APP_CONTROLLER.status_toggle.setFocus()
        APP_CONTROLLER.updated_job.emit(job)

    def _add_item(self, job: Job):
        item = QStandardItem(job.name)
        item.setIcon(QIcon(job.icon))
        item.setData(job)
        self.model.appendRow(item)
