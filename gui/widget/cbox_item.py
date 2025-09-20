from PySide6.QtWidgets import QComboBox
from PySide6.QtGui import QStandardItemModel, QStandardItem, QIcon

from config.app import APP_CBOX_WIDTH
from game.buff import ITEM_BUFF_GROUP, ITEM_DEBUFF_GROUP
from gui.app_controller import APP_CONTROLLER
from service.config_file import ACTIVE, AUTO_ITEM, CONFIG_FILE, ITEM_BUFF
from util.widgets import build_cbox_category


class CboxItem(QComboBox):

    def __init__(self, parent, resource=ITEM_BUFF):
        super().__init__(parent)
        self.resource = resource
        self.setFixedWidth(APP_CBOX_WIDTH)
        self.item_model = QStandardItemModel()
        self.currentIndexChanged.connect(self._on_changed)
        self.build_cbox()

    def _on_changed(self, index):
        if index < 1:
            return
        item = self.item_model.takeItem(index, 0).data()
        self.item_model.takeRow(index)
        CONFIG_FILE.update_config(True, [APP_CONTROLLER.job.id, AUTO_ITEM, self.resource, item.id, ACTIVE])
        self._emit_event(item)
        if APP_CONTROLLER.status_toggle is not None:
            APP_CONTROLLER.status_toggle.setFocus()

    def add_item(self, item):
        if not item:
            return self.item_model.appendRow(QStandardItem(""))
        q_item = QStandardItem(item.name)
        q_item.setIcon(QIcon(item.icon))
        q_item.setData(item)
        self.item_model.appendRow(q_item)

    def _emit_event(self, item):
        if self.resource == ITEM_BUFF:
            return APP_CONTROLLER.added_item_buff.emit(item)
        APP_CONTROLLER.added_item_debuff.emit(item)

    def _get_items(self):
        if self.resource == ITEM_BUFF:
            return ITEM_BUFF_GROUP.items()
        return ITEM_DEBUFF_GROUP.items()

    def _get_active_items(self):
        if self.resource == ITEM_BUFF:
            return APP_CONTROLLER.job_item_buffs
        return APP_CONTROLLER.job_item_debuffs

    def build_cbox(self):
        self.item_model.clear()
        self.currentIndexChanged.disconnect()
        self.add_item(None)
        self.setCurrentIndex(0)
        for group, items in self._get_items():
            build_cbox_category(self.item_model, group)
            for item in items:
                if item in self._get_active_items():
                    continue
                self.add_item(item)
        self.setModel(self.item_model)
        self.currentIndexChanged.connect(self._on_changed)
