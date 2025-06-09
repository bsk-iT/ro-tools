from PyQt6.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QSpinBox, QCheckBox
from PyQt6.QtCore import Qt

from config.icon import IMG_BLUE_POTION, IMG_RED_POTION, IMG_YGG
from gui.widget.input_delay import InputDelay
from gui.widget.input_keybind import InputKeybind
from gui.widget.input_map_criteria import InputMapCriteria
from service.config_file import AUTO_POT, CITY_ACTIVE, CONFIG_FILE, DELAY, DELAY_ACTIVE, HP_PERCENT, HP_POTION, KEY, MAP, MAP_ACTIVE, PERCENT, SP_PERCENT, SP_POTION, YGG
from service.servers_file import SERVERS_FILE
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
        active_city = CONFIG_FILE.get_value([AUTO_POT, CITY_ACTIVE])
        check_city.setChecked(True if active_city else False)
        check_city.checkStateChanged.connect(self._update_active_city)
        hbox_city.addWidget(check_city)
        hbox_city.addWidget(build_link_file(SERVERS_FILE))
        vbox.addLayout(hbox_city)
        return vbox

    def _update_active_city(self, state):
        CONFIG_FILE.update_config(state.value == 2, [AUTO_POT, CITY_ACTIVE])

    def _build_layout_auto_potions(self):
        vbox_potion = QVBoxLayout()
        vbox_potion.setSpacing(0)
        hp_layout = self._build_action_layout("HP", IMG_RED_POTION, HP_POTION)
        sp_layout = self._build_action_layout("SP", IMG_BLUE_POTION, SP_POTION)
        vbox_potion.addLayout(hp_layout)
        vbox_potion.addLayout(sp_layout)
        return vbox_potion

    def _build_layout_auto_ygg(self):
        vbox_ygg = QVBoxLayout()
        ygg_layout = self._build_action_layout("YGG", IMG_YGG, YGG, True)
        vbox_ygg.addWidget(build_label_info("Tem preferência de uso sobre as Potions.\nÉ possível utilizar a tecla da asa de mosca ou macro do jogo (Ex: ALT+1) para telar."))
        vbox_ygg.addLayout(ygg_layout)
        return vbox_ygg

    def _build_action_layout(self, tooltip: str, icon: str, resource: str, is_ygg=False) -> QHBoxLayout:
        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        key = CONFIG_FILE.get_key([AUTO_POT, resource, KEY])
        percentage = CONFIG_FILE.get_key([AUTO_POT, resource, PERCENT])
        delay_active = CONFIG_FILE.get_key([AUTO_POT, resource, DELAY_ACTIVE])
        delay = CONFIG_FILE.get_key([AUTO_POT, resource, DELAY])
        map_active = CONFIG_FILE.get_key([AUTO_POT, resource, MAP_ACTIVE])
        _map = CONFIG_FILE.get_key([AUTO_POT, resource, MAP])

        layout.addWidget(build_icon(icon))
        layout.addWidget(InputKeybind(self, key))
        if percentage:
            widget = self._build_ygg_widget(resource) if is_ygg else build_spinbox_percentage(percentage, tooltip)
            layout.addWidget(widget)
        layout.addWidget(InputDelay(self, delay_active, delay))
        if map_active and _map:
            layout.addWidget(InputMapCriteria(self, map_active, _map))
        return layout

    def _build_ygg_widget(self, resource: str) -> QSpinBox:
        widget = QWidget()
        hp_percent = CONFIG_FILE.get_key([AUTO_POT, resource, HP_PERCENT])
        sp_percent = CONFIG_FILE.get_key([AUTO_POT, resource, SP_PERCENT])
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
