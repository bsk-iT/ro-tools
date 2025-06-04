from PyQt6.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QSpinBox, QCheckBox
from PyQt6.QtCore import Qt

from config.icon import IMG_BLUE_POTION, IMG_RED_POTION, IMG_YGG
from gui.widget.input_delay import InputDelay
from gui.widget.input_keybind import InputKeybind
from gui.widget.input_map_criteria import InputMapCriteria
from service.event import EVENT, EventType, Prop, Resource
from service.file import MAPS_FILE
from util.widgets import build_icon, build_label_info, build_label_subtitle, build_link_file, build_painel, build_spinbox_percentage


class PainelAutoPot(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self._config_layout()

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        painel = build_painel(self.layout, "Auto Pot")
        painel.addLayout(self._build_layout_config())
        painel.addWidget(build_label_subtitle("Potions"))
        painel.addLayout(self._build_layout_auto_potions())
        painel.addWidget(build_label_subtitle("YGG / Telar"))
        painel.addLayout(self._build_layout_auto_ygg())

    def _build_layout_config(self):
        vbox = QVBoxLayout()
        vbox.setContentsMargins(0, 20, 0, 0)
        hbox_city = QHBoxLayout()
        check_city = QCheckBox("Ativo em cidades")
        active_city = EVENT.get_config(Prop.CITY_ACTIVE, EventType.AUTO_POT)
        check_city.setChecked(True if active_city else False)
        check_city.checkStateChanged.connect(self._update_active_city)
        hbox_city.addWidget(check_city)
        hbox_city.addWidget(build_link_file(MAPS_FILE))
        vbox.addLayout(hbox_city)
        return vbox

    def _update_active_city(self, state):
        EVENT.update_config(Prop.CITY_ACTIVE, state.value == 2, EventType.AUTO_POT)

    def _build_layout_auto_potions(self):
        vbox_potion = QVBoxLayout()
        vbox_potion.setSpacing(0)
        hp_layout = self._build_action_layout("HP", IMG_RED_POTION, Resource.HP_POTION)
        sp_layout = self._build_action_layout("SP", IMG_BLUE_POTION, Resource.SP_POTION)
        vbox_potion.addLayout(hp_layout)
        vbox_potion.addLayout(sp_layout)
        return vbox_potion

    def _build_layout_auto_ygg(self):
        vbox_ygg = QVBoxLayout()
        ygg_layout = self._build_action_layout("YGG", IMG_YGG, Resource.YGG, True)
        vbox_ygg.addWidget(build_label_info("Tem preferência de uso sobre as Potions.\nÉ possível utilizar a tecla da asa de mosca ou macro do jogo (Ex: ALT+1) para telar."))
        vbox_ygg.addLayout(ygg_layout)
        return vbox_ygg

    def _build_action_layout(self, tooltip: str, icon: str, resource: Resource, is_ygg=False) -> QHBoxLayout:
        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        key = EVENT.get_config_key(Prop.KEY, EventType.AUTO_POT, resource)
        percentage = EVENT.get_config_key(Prop.PERCENT, EventType.AUTO_POT, resource)
        delay_active = EVENT.get_config_key(Prop.DELAY_ACTIVE, EventType.AUTO_POT, resource)
        delay = EVENT.get_config_key(Prop.DELAY, EventType.AUTO_POT, resource)
        map_active = EVENT.get_config_key(Prop.MAP_ACTIVE, EventType.AUTO_POT, resource)
        _map = EVENT.get_config_key(Prop.MAP, EventType.AUTO_POT, resource)

        layout.addWidget(build_icon(icon))
        layout.addWidget(InputKeybind(self, key))
        if percentage:
            widget = self._build_ygg_widget(resource) if is_ygg else build_spinbox_percentage(percentage, tooltip)
            layout.addWidget(widget)
        layout.addWidget(InputDelay(self, delay_active, delay))
        if map_active and _map:
            layout.addWidget(InputMapCriteria(self, map_active, _map))
        return layout

    def _build_ygg_widget(self, resource: Resource) -> QSpinBox:
        widget = QWidget()
        hp_percent = EVENT.get_config_key(Prop.HP_PERCENT, EventType.AUTO_POT, resource)
        sp_percent = EVENT.get_config_key(Prop.SP_PERCENT, EventType.AUTO_POT, resource)
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
