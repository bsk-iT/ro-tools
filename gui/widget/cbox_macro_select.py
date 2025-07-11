from itertools import chain
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon

from config.app import APP_CBOX_WIDTH
from game.macro import MACRO_MAP, MACRO_TYPES, Macro
from gui.app_controller import APP_CONTROLLER
from service.config_file import CONFIG_FILE
from util.widgets import build_cbox_category, get_color_by_id


class CboxMacroSelect(QComboBox):

    def __init__(self, parent, key_base):
        super().__init__(parent)
        self.setFixedWidth(APP_CBOX_WIDTH)
        self.key_base = key_base
        self.model = QStandardItemModel()
        self.update_cbox()
        APP_CONTROLLER.add_macro_select.connect(self.update_cbox)
        APP_CONTROLLER.removed_macro.connect(self.remove_macro)

    def remove_macro(self, macro: Macro):
        if self.currentText() == macro.name:
            CONFIG_FILE.update(self.key_base, None)
        self.update_cbox(macro)

    def update_cbox(self, _=None):
        self.currentIndexChanged.connect(self._on_changed)
        self.currentIndexChanged.disconnect()
        self.build_cbox()
        self.setCurrentIndex(0)
        self.sync_current_item()
        self.currentIndexChanged.connect(self._on_changed)

    def sync_current_item(self):
        macro_id = CONFIG_FILE.read(self.key_base)
        if not macro_id:
            return
        items = self.model.findItems(MACRO_MAP[macro_id].name)
        if len(items) == 0:
            return
        self.setCurrentIndex(items.pop().row())

    def _on_changed(self, index):
        if index < 0:
            return
        macro_id = self.model.item(index, 0).data()
        CONFIG_FILE.update(self.key_base, macro_id)
        APP_CONTROLLER.status_toggle.setFocus()

    def add_item(self, macro):
        if not macro:
            return self.model.appendRow(QStandardItem(""))
        item = QStandardItem(macro.name)
        color = get_color_by_id(macro.id)
        if color is not None:
            item.setForeground(color)
        item.setIcon(QIcon(macro.icon))
        item.setData(macro.id)
        self.model.appendRow(item)

    def build_cbox(self):
        self.model.clear()
        active_macros = list(chain.from_iterable(APP_CONTROLLER.job_macros.values()))
        self.add_item(None)
        for group, macros in MACRO_TYPES.items():
            build_cbox_category(self.model, group)
            for macro in macros:
                if macro not in active_macros:
                    continue
                self.add_item(macro)
        self.setModel(self.model)
