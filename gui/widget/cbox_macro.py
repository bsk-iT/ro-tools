from itertools import chain
from PyQt6.QtWidgets import QComboBox
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QIcon

from config.app import APP_CBOX_WIDTH
from gui.app_controller import APP_CONTROLLER
from game.macro import MACRO_ELEMENTS, MACRO_TYPES
from service.config_file import AUTO_ELEMENT, HOTKEY, MACRO
from util.widgets import build_cbox_category, get_color_by_id


class CboxMacro(QComboBox):

    def __init__(self, parent, resource: str = MACRO):
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
        (macro, job_id) = self.model.takeItem(index, 0).data()
        self.model.takeRow(index)
        self._emit_event(job_id, macro)
        APP_CONTROLLER.status_toggle.setFocus()

    def _emit_event(self, job_id, macro):
        if self.resource == MACRO:
            return APP_CONTROLLER.added_macro.emit(job_id, macro)
        if self.resource == AUTO_ELEMENT:
            return APP_CONTROLLER.added_auto_element.emit(job_id, macro)
        APP_CONTROLLER.added_hotkey.emit(job_id, macro)

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

    def _get_active_macros(self):
        macros = APP_CONTROLLER.job_macros
        if self.resource == HOTKEY:
            macros = APP_CONTROLLER.job_hotkeys
        if self.resource == AUTO_ELEMENT:
            macros = APP_CONTROLLER.job_auto_elements
        return list(chain.from_iterable(macros.values()))

    def _get_macros(self):
        if self.resource == AUTO_ELEMENT:
            return {None: MACRO_ELEMENTS}.items()
        return MACRO_TYPES.items()

    def build_cbox(self, job):
        self.model.clear()
        self.currentIndexChanged.disconnect()
        self.add_item(None, None)
        self.setCurrentIndex(0)
        for group, macros in self._get_macros():
            build_cbox_category(self.model, group)
            for macro in macros:
                if macro in self._get_active_macros():
                    continue
                self.add_item(macro, job)
        self.setModel(self.model)
        self.currentIndexChanged.connect(self._on_changed)
