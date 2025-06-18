from PyQt6.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QSpinBox
from PyQt6.QtCore import Qt

from config.icon import IMG_BLUE_POTION, IMG_RED_POTION, IMG_YGG, PATH_ITEM, get_image
from gui.widget.input_delay import InputDelay
from gui.widget.input_keybind import InputKeybind
from gui.widget.input_map_criteria import InputMapCriteria
from service.config_file import AUTO_ITEM, CITY_BLOCK, CONFIG_FILE, FLY_WING, HP_PERCENT, HP_POTION, KEY, MAP, MAP_ACTIVE, PERCENT, SP_PERCENT, SP_POTION, YGG
from util.widgets import build_icon, build_label_info, build_label_subtitle, build_spinbox_percentage


class PainelAutoItemHpSp(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self._config_layout()

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.layout.setSpacing(15)
        self.layout.setContentsMargins(10, 15, 10, 10)
        self.layout.addWidget(build_label_subtitle("Potions"))
        self.layout.addLayout(self._build_layout_auto_potions())
        self.layout.addWidget(build_label_subtitle("YGG"))
        self.layout.addLayout(self._build_layout_auto_ygg())
        self.layout.addWidget(build_label_subtitle("Asa de Mosca"))
        self.layout.addLayout(self._build_layout_fly_wing())

    def _update_active_city(self, state):
        CONFIG_FILE.update_config(state.value == 2, [AUTO_ITEM, CITY_BLOCK])

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
        vbox_ygg.addLayout(ygg_layout)
        return vbox_ygg

    def _build_action_layout(self, tooltip: str, icon: str, resource: str, is_ygg=False) -> QHBoxLayout:
        layout = QHBoxLayout()
        layout.setSpacing(0)
        key_seq = f"{AUTO_ITEM}:{resource}:"
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        percentage = f"{AUTO_ITEM}:{resource}:{PERCENT}"
        map_active = f"{AUTO_ITEM}:{resource}:{MAP_ACTIVE}"
        _map = f"{AUTO_ITEM}:{resource}:{MAP}"

        layout.addWidget(build_icon(icon))
        layout.addWidget(InputKeybind(self, key_seq + KEY))
        if percentage:
            widget = self._build_ygg_widget(resource) if is_ygg else build_spinbox_percentage(percentage, tooltip)
            layout.addWidget(widget)
        layout.addWidget(InputDelay(self, key_seq))
        if map_active and _map:
            layout.addWidget(InputMapCriteria(self, key_seq))
        return layout

    def _build_ygg_widget(self, resource: str) -> QSpinBox:
        widget = QWidget()
        hp_percent = f"{AUTO_ITEM}:{resource}:{HP_PERCENT}"
        sp_percent = f"{AUTO_ITEM}:{resource}:{SP_PERCENT}"
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

    def _build_layout_fly_wing(self):
        vbox = QVBoxLayout()
        vbox.addWidget(build_label_info("Configurar a tecla do item abaixo, irá evitar o 'lock' do Auto Pot devido ao jogo não permitir utilizar mais de um item ao mesmo tempo"))
        hbox = QHBoxLayout()
        hbox.setSpacing(0)
        hbox.setAlignment(Qt.AlignmentFlag.AlignLeft)
        hbox.addWidget(build_icon(get_image(PATH_ITEM, "fly_wing")))
        hbox.addWidget(InputKeybind(self, f"{AUTO_ITEM}:{FLY_WING}:{KEY}"))
        vbox.addLayout(hbox)
        return vbox
