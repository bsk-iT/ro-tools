from itertools import chain
from PyQt6.QtWidgets import QComboBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QIcon
from PyQt6.QtCore import pyqtSignal

from config.app import APP_CBOX_WIDTH
from gui.app_controller import APP_CONTROLLER
from game.macro import MACRO_TYPES
from gui.widget.cbox_jobs import CboxJobs
from service.config_file import ACTIVE, CONFIG_FILE, MACRO
from util.widgets import build_cbox_category, get_color_by_id


class CboxMacro(QComboBox):

    updated_macro = pyqtSignal()

    def __init__(self, parent, cbox_job: CboxJobs, resource: str = MACRO):
        super().__init__(parent)
        self.setFixedWidth(APP_CBOX_WIDTH)
        self.resource = resource
        self.model = QStandardItemModel()
        self.currentIndexChanged.connect(self._on_changed)
        self.build_cbox()
        cbox_job.updated_job.connect(self.build_cbox)

    def _on_changed(self, index):
        if index < 1:
            return
        (macro, job_id) = self.model.takeItem(index, 0).data()
        self.model.takeRow(index)
        CONFIG_FILE.update_config(True, [self.resource, job_id, macro.id, ACTIVE])
        APP_CONTROLLER.update_macros(macro, True)
        self.updated_macro.emit()
        APP_CONTROLLER.status_widget.setFocus()

    def add_item(self, macro, job):
        if not macro and not job:
            return self.model.appendRow(QStandardItem(""))
        item = QStandardItem(macro.name)
        color = get_color_by_id(macro.id)
        if color is not None:
            item.setForeground(color)
        item.setIcon(QIcon(macro.icon))
        item.setData((macro, job.id))
        self.model.appendRow(item)

    def build_cbox(self):
        self.model.clear()
        self.currentIndexChanged.disconnect()
        active_macros = list(chain.from_iterable(APP_CONTROLLER.job_macros.values()))
        self.add_item(None, None)
        self.setCurrentIndex(0)
        for group, macros in MACRO_TYPES.items():
            build_cbox_category(self.model, group)
            for macro in macros:
                if macro in active_macros:
                    continue
                self.add_item(macro, APP_CONTROLLER.job)
        self.setModel(self.model)
        self.currentIndexChanged.connect(self._on_changed)
