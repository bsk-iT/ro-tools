from PyQt5.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QSpinBox, QCheckBox
from PyQt5.QtCore import Qt

from config.icon import IMG_BLUE_POTION, IMG_RED_POTION, IMG_YGG, PATH_ITEM, get_image
from game.jobs import Job
from gui.app_controller import APP_CONTROLLER
from gui.widget.input_delay import InputDelay
from gui.widget.input_keybind import InputKeybind
from gui.widget.input_map_criteria import InputMapCriteria
from gui.widget.input_teleport import InputTeleport
from service.config_file import AUTO_ITEM, CITY_BLOCK, CONFIG_FILE, FLY_WING, HALTER_LEAD, HP_PERCENT, HP_POTION, KEY, MOVIMENT_CELLS, PERCENT, SP_PERCENT, SP_POTION, YGG
from util.widgets import build_icon, build_label_info, build_label_subtitle, build_scroll_vbox, build_spinbox_cells, build_spinbox_percentage, clear_layout


class PainelAutoItemHpSp(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self._config_layout()
        APP_CONTROLLER.updated_job.connect(self.update_auto_item)

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.setSpacing(10)
        self.update_auto_item(APP_CONTROLLER.job)

    def update_auto_item(self, _):
        clear_layout(self.layout.takeAt(1))
        clear_layout(self.layout.takeAt(0))
        self.layout.addWidget(self._build_config())
        (vbox, scroll) = build_scroll_vbox()

        hbox_1 = QHBoxLayout()
        vbox_potions = QVBoxLayout()
        vbox_potions.addWidget(build_label_subtitle("Potions"))
        vbox_potions.addLayout(self._build_layout_auto_potions())
        vbox_ygg = QVBoxLayout()
        vbox_ygg.addWidget(build_label_subtitle("YGG"))
        vbox_ygg.addLayout(self._build_layout_auto_ygg())
        hbox_1.addLayout(vbox_potions)
        hbox_1.addLayout(vbox_ygg)

        vbox_halter_lead = QVBoxLayout()
        vbox_halter_lead.addWidget(build_label_subtitle("Rédeas"))
        vbox_halter_lead.addLayout(self._build_layout_halter_lead())
        vbox_fly_wing = QVBoxLayout()
        vbox_fly_wing.addWidget(build_label_subtitle("Asa de Mosca"))
        vbox_fly_wing.addLayout(self._build_layout_fly_wing())
        
        vbox.setSpacing(10)
        vbox.addLayout(hbox_1)
        vbox.addLayout(vbox_halter_lead)
        vbox.addLayout(vbox_fly_wing)
        self.layout.addWidget(scroll)

    def _update_active_city(self, state):
        CONFIG_FILE.update_config(state == 2, [AUTO_ITEM, CITY_BLOCK])

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
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        key_seq = f"{AUTO_ITEM}:{resource}:"

        layout.addWidget(build_icon(icon))
        layout.addWidget(InputKeybind(self, key_seq + KEY))
        widget = self._build_ygg_widget(resource) if is_ygg else build_spinbox_percentage(f"{key_seq}{PERCENT}", tooltip)
        layout.addWidget(widget)
        layout.addWidget(InputDelay(self, key_seq))
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
        hbox.addWidget(InputKeybind(self, f"{AUTO_ITEM}:{FLY_WING}:{KEY}", True))
        hbox.addWidget(InputTeleport(self, f"{AUTO_ITEM}:{FLY_WING}:"))
        vbox.addLayout(hbox)
        return vbox
    
    def _build_layout_halter_lead(self):
        vbox = QVBoxLayout()
        vbox.addWidget(build_label_info("Usa automáticamente as rédeas quando andar uma quantidade X de células. Ao utilizar alguma Skill Spawmmer é removido o status de montaria. Skill Buff estarão desabilitado enquanto estiver na montaria."))
        hbox = QHBoxLayout()
        hbox.setSpacing(0)
        hbox.setAlignment(Qt.AlignmentFlag.AlignLeft)
        hbox.addWidget(build_icon(get_image(PATH_ITEM, "halter_lead")))
        hbox.addWidget(InputKeybind(self, f"{AUTO_ITEM}:{HALTER_LEAD}:{KEY}", True))
        hbox.addWidget(build_spinbox_cells(f"{AUTO_ITEM}:{HALTER_LEAD}:{MOVIMENT_CELLS}"))
        vbox.addLayout(hbox)
        return vbox

    def _build_config(self):
        widget = QWidget()
        vbox = QVBoxLayout(widget)
        vbox.setContentsMargins(0, 0, 0, 0)
        hbox_city = QHBoxLayout()
        check_city = QCheckBox("Bloquear uso em cidades?")
        city_block = CONFIG_FILE.get_value([AUTO_ITEM, CITY_BLOCK])
        check_city.setChecked(True if city_block else False)
        check_city.stateChanged.connect(lambda state: self._update_city_block(state))
        hbox_city.addWidget(check_city)
        vbox.addLayout(hbox_city)
        return widget

    def _update_city_block(self, state):
        CONFIG_FILE.update_config(state == 2, [AUTO_ITEM, CITY_BLOCK])
