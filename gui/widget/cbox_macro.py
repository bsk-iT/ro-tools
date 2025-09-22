from itertools import chain
from PySide6.QtWidgets import QComboBox
from PySide6.QtGui import QStandardItemModel, QStandardItem, QIcon

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
        self.item_model = QStandardItemModel()
        self.currentIndexChanged.connect(self._on_changed)
        self.build_cbox(APP_CONTROLLER.job)
        APP_CONTROLLER.updated_job.connect(self.build_cbox)

    def _on_changed(self, index):
        if index < 1:
            return
        (macro, job_id) = self.item_model.takeItem(index, 0).data()
        self.item_model.takeRow(index)
        self._emit_event(job_id, macro)
        if APP_CONTROLLER.status_toggle is not None:
            APP_CONTROLLER.status_toggle.setFocus()

    def _emit_event(self, job_id, macro):
        if self.resource == MACRO:
            return APP_CONTROLLER.added_macro.emit(job_id, macro)
        if self.resource == AUTO_ELEMENT:
            return APP_CONTROLLER.added_auto_element.emit(job_id, macro)
        APP_CONTROLLER.added_hotkey.emit(job_id, macro)

    def add_item(self, macro, job):
        if not macro and not job:
            return self.item_model.appendRow(QStandardItem(""))
        item = QStandardItem(macro.name)
        color = get_color_by_id(macro.id)
        if color is not None:
            item.setForeground(color)
        item.setIcon(QIcon(macro.icon))
        item.setData((macro, job.id))
        self.item_model.appendRow(item)

    def _get_active_macros(self):
        macros = APP_CONTROLLER.job_macros
        if self.resource == HOTKEY:
            macros = APP_CONTROLLER.job_hotkeys
        if self.resource == AUTO_ELEMENT:
            macros = APP_CONTROLLER.job_auto_elements
        return list(chain.from_iterable(macros.values()))

    def _get_macros(self):
        if self.resource == AUTO_ELEMENT:
            from game.macro import ATK_1, ATK_2, ATK_3, ATK_4, ATK_5, DEF_1, DEF_2, DEF_3, DEF_4, DEF_5
            auto_element_macros = {
                "Elementos": MACRO_ELEMENTS,
                "Equipes de Ataque": [ATK_1, ATK_2, ATK_3, ATK_4, ATK_5],
                "Equipes de Defesa": [DEF_1, DEF_2, DEF_3, DEF_4, DEF_5]
            }
            return auto_element_macros.items()
        return MACRO_TYPES.items()

    def build_cbox(self, job):
        self.item_model.clear()
        self.currentIndexChanged.disconnect()
        self.add_item(None, None)
        self.setCurrentIndex(0)
        for group, macros in self._get_macros():
            build_cbox_category(self.item_model, group)
            for macro in macros:
                if macro in self._get_active_macros():
                    continue
                self.add_item(macro, job)
        self.setModel(self.item_model)
        self.currentIndexChanged.connect(self._on_changed)
