from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel, QHBoxLayout, QSpinBox
from PyQt6.QtCore import Qt

from config.action import Action
from config.icon import IMG_BLUE_POTION, IMG_RED_POTION, IMG_YGG
from db.item import Item
from gui.widget.input_delay import InputDelay
from gui.widget.input_keybind import InputKeybind
from gui.widget.input_map_criteria import InputMapCriteria
from service.auto_pot import AUTO_POT
from util.widgets import build_icon, build_painel, build_spinbox_percentage


class PainelAutoPot(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self.title = QLabel("Auto Pot")
        self._config_layout()
        AUTO_POT.run()

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        painel_potion = build_painel(self.layout, "Auto Potion")
        vbox_potion = QVBoxLayout()
        vbox_potion.setSpacing(0)
        hp_layout = self._build_action_layout("HP", IMG_RED_POTION, Item.HP_POTION)
        sp_layout = self._build_action_layout("SP", IMG_BLUE_POTION, Item.SP_POTION)
        vbox_potion.addLayout(hp_layout)
        vbox_potion.addLayout(sp_layout)
        painel_potion.addLayout(vbox_potion)

        painel_ygg = build_painel(self.layout, "Auto Ygg")
        vbox_ygg = QVBoxLayout()
        ygg_layout = self._build_action_layout("YGG", IMG_YGG, Item.YGG, True)
        vbox_ygg.addLayout(ygg_layout)
        painel_ygg.addLayout(vbox_ygg)

    def _build_action_layout(self, tooltip: str, icon: str, item: Item, is_ygg=False) -> QHBoxLayout:
        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        key = AUTO_POT.getConfigKey(item, Action.KEY)
        percentage = AUTO_POT.getConfigKey(item, Action.PERCENT)
        delay_active = AUTO_POT.getConfigKey(item, Action.DELAY_ACTIVE)
        delay = AUTO_POT.getConfigKey(item, Action.DELAY)
        map_active = AUTO_POT.getConfigKey(item, Action.MAP_ACTIVE)
        _map = AUTO_POT.getConfigKey(item, Action.MAP)

        layout.addWidget(build_icon(icon))
        layout.addWidget(InputKeybind(self, key))
        if percentage:
            widget = self._build_ygg_widget(item) if is_ygg else build_spinbox_percentage(percentage, tooltip)
            layout.addWidget(widget)
        layout.addWidget(InputDelay(self, delay_active, delay))
        if map_active and _map:
            layout.addWidget(InputMapCriteria(self, map_active, _map))
        return layout

    def _build_ygg_widget(self, item: Item) -> QSpinBox:
        widget = QWidget()
        hp_percent = AUTO_POT.getConfigKey(item, Action.HP_PERCENT)
        sp_percent = AUTO_POT.getConfigKey(item, Action.SP_PERCENT)
        vbox = QVBoxLayout(widget)
        vbox.setContentsMargins(0, 0, 0, 0)
        vbox.setSpacing(0)
        hbox_hp = QHBoxLayout()
        hbox_hp.addWidget(build_spinbox_percentage(hp_percent, "HP"))
        vbox.addLayout(hbox_hp)
        hbox_sp = QHBoxLayout()
        hbox_sp.addWidget(build_spinbox_percentage(sp_percent, "SP"))
        vbox.addLayout(hbox_sp)
        return widget
