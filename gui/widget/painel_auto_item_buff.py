from PyQt6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QHBoxLayout, QFrame, QPushButton
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon

from config.icon import ICON_DELETE
from game.buff import ITEM_BUFF_GROUP, Buff, Buff
from gui.app_controller import APP_CONTROLLER
from gui.widget.cbox_item import CboxItem
from gui.widget.input_keybind import InputKeybind
from gui.widget.input_map_criteria import InputMapCriteria
from service.config_file import ACTIVE, AUTO_ITEM, CONFIG_FILE, ITEM_BUFF, KEY
from util.widgets import build_hr, build_icon, build_label_info, build_scroll_vbox, clear_layout


class PainelAutoItemBuff(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self.cbox_item: CboxItem = CboxItem(self)
        self._config_layout()

    def _config_layout(self):
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.layout.addWidget(self.cbox_item)
        self.update_item_buffs()
        APP_CONTROLLER.added_item_buff.connect(self._on_add_skill)

    def update_item_buffs(self):
        clear_layout(self.layout.takeAt(1))
        (vbox, scroll) = build_scroll_vbox()
        for group, items in ITEM_BUFF_GROUP.items():
            has_item = False
            vbox_item_buff = QVBoxLayout()
            vbox_item_buff.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
            for item in items:
                if item.id not in [a_item.id for a_item in APP_CONTROLLER.item_buffs]:
                    continue
                has_item = True
                vbox_item_buff.addWidget(self._build_item_inputs(item))
            if has_item:
                vbox.addWidget(build_label_info(group))
                vbox.addLayout(vbox_item_buff)
        self.layout.addWidget(scroll)

    def _build_item_inputs(self, item: Buff):
        widget = QWidget()
        vbox = QVBoxLayout(widget)
        hbox = QHBoxLayout()
        hbox.setSpacing(5)
        hbox.setAlignment(Qt.AlignmentFlag.AlignLeft)
        hbox.addWidget(self._build_item_icon(item))
        key_base = f"{AUTO_ITEM}:{ITEM_BUFF}:{item.id}:"
        hbox.addWidget(InputKeybind(self, key_base + KEY))
        hbox.addWidget(InputMapCriteria(self, key_base))
        vbox.addLayout(hbox)
        vbox.addWidget(build_hr())
        return widget

    def _build_item_icon(self, item: Buff) -> QFrame:
        frame = QFrame()
        icon = build_icon(item.icon, item.id, 25, frame)
        icon.move(9, 9)
        frame.setFixedSize(35, 40)
        btn_delete = QPushButton(frame)
        btn_delete.move(0, 0)
        btn_delete.setIcon(QIcon(ICON_DELETE))
        btn_delete.setIconSize(QSize(10, 10))
        btn_delete.setContentsMargins(0, 0, 0, 0)
        btn_delete.clicked.connect(lambda: self._on_remove_item(item))
        btn_delete.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        return frame

    def _active_skill(self, item: Buff, active=True):
        self.update_item_buffs()
        CONFIG_FILE.update_config(active, [AUTO_ITEM, ITEM_BUFF, item.id, ACTIVE])
        self.cbox_item.build_cbox()

    def _on_add_skill(self, item: Buff):
        APP_CONTROLLER.item_buffs.append(item)
        self._active_skill(item)
        APP_CONTROLLER.status_toggle.setFocus()

    def _on_remove_item(self, item: Buff):
        APP_CONTROLLER.item_buffs.remove(item)
        self._active_skill(item, False)
