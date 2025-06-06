from PyQt6.QtWidgets import QComboBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QFont, QIcon
from PyQt6.QtCore import Qt

from game.jobs import JOB_GROUPS


class CboxJobs(QComboBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.model = QStandardItemModel()
        self._build_cbox()

    def add_category(self, label):
        item = QStandardItem(label)
        item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEnabled)
        item.setFont(QFont(None, weight=QFont.Weight.Bold))
        self.model.appendRow(item)

    def add_item(self, job, data=None):
        item = QStandardItem(job.name)
        item.setIcon(QIcon(job.icon))
        item.setData(data)
        self.model.appendRow(item)

    def _build_cbox(self):
        for group in JOB_GROUPS:
            self.add_category(group)
            for job in JOB_GROUPS[group]:
                self.add_item(job)
        self.setModel(self.model)