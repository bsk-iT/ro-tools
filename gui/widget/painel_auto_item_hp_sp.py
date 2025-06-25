from PyQt6.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QSpinBox, QCheckBox
from PyQt6.QtCore import Qt

from config.icon import IMG_BLUE_POTION, IMG_RED_POTION, IMG_YGG, PATH_ITEM, get_image
from game.jobs import Job
from gui.app_controller import APP_CONTROLLER
from gui.widget.input_delay import InputDelay
from gui.widget.input_keybind import InputKeybind
from gui.widget.input_map_criteria import InputMapCriteria
from gui.widget.input_teleport import InputTeleport
from service.config_file import AUTO_ITEM, CITY_BLOCK, CONFIG_FILE, FLY_WING, HP_PERCENT, HP_POTION, KEY, PERCENT, SP_PERCENT, SP_POTION, YGG
from util.widgets import build_icon, build_label_info, build_label_subtitle, build_scroll_vbox, build_spinbox_percentage, clear_layout


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

    def update_auto_item(self, job: Job):
        clear_layout(self.layout.takeAt(1))
        clear_layout(self.layout.takeAt(0))
        self.layout.addWidget(self._build_config(job))
        (vbox, scroll) = build_scroll_vbox()
        vbox.setSpacing(10)
        vbox.addWidget(build_label_subtitle("Potions"))
        vbox.addLayout(self._build_layout_auto_potions(job))
        vbox.addWidget(build_label_subtitle("YGG"))
        vbox.addLayout(self._build_layout_auto_ygg(job))
        vbox.addWidget(build_label_subtitle("Asa de Mosca"))
        vbox.addLayout(self._build_layout_fly_wing(job))
        self.layout.addWidget(scroll)

    def _update_active_city(self, state):
        CONFIG_FILE.update_config(state.value == 2, [AUTO_ITEM, CITY_BLOCK])

    def _build_layout_auto_potions(self, job: Job):
        vbox_potion = QVBoxLayout()
        vbox_potion.setSpacing(0)
        hp_layout = self._build_action_layout(job, "HP", IMG_RED_POTION, HP_POTION)
        sp_layout = self._build_action_layout(job, "SP", IMG_BLUE_POTION, SP_POTION)
        vbox_potion.addLayout(hp_layout)
        vbox_potion.addLayout(sp_layout)
        return vbox_potion

    def _build_layout_auto_ygg(self, job: Job):
        vbox_ygg = QVBoxLayout()
        ygg_layout = self._build_action_layout(job, "YGG", IMG_YGG, YGG, True)
        vbox_ygg.addLayout(ygg_layout)
        return vbox_ygg

    def _build_action_layout(self, job: Job, tooltip: str, icon: str, resource: str, is_ygg=False) -> QHBoxLayout:
        layout = QHBoxLayout()
        layout.setSpacing(0)
        layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        key_seq = f"{job.id}:{AUTO_ITEM}:{resource}:"

        layout.addWidget(build_icon(icon))
        layout.addWidget(InputKeybind(self, key_seq + KEY))
        widget = self._build_ygg_widget(job, resource) if is_ygg else build_spinbox_percentage(f"{key_seq}{PERCENT}", tooltip)
        layout.addWidget(widget)
        layout.addWidget(InputDelay(self, key_seq))
        layout.addWidget(InputMapCriteria(self, key_seq))
        return layout

    def _build_ygg_widget(self, job: Job, resource: str) -> QSpinBox:
        widget = QWidget()
        hp_percent = f"{job.id}:{AUTO_ITEM}:{resource}:{HP_PERCENT}"
        sp_percent = f"{job.id}:{AUTO_ITEM}:{resource}:{SP_PERCENT}"
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

    def _build_layout_fly_wing(self, job: Job):
        vbox = QVBoxLayout()
        vbox.addWidget(build_label_info("Configurar a tecla do item abaixo, irá evitar o 'lock' do Auto Pot devido ao jogo não permitir utilizar mais de um item ao mesmo tempo"))
        hbox = QHBoxLayout()
        hbox.setSpacing(0)
        hbox.setAlignment(Qt.AlignmentFlag.AlignLeft)
        hbox.addWidget(build_icon(get_image(PATH_ITEM, "fly_wing")))
        hbox.addWidget(InputKeybind(self, f"{job.id}:{AUTO_ITEM}:{FLY_WING}:{KEY}", True))
        hbox.addWidget(InputTeleport(self, f"{job.id}:{AUTO_ITEM}:{FLY_WING}:"))
        vbox.addLayout(hbox)
        return vbox

    def _build_config(self, job: Job):
        widget = QWidget()
        vbox = QVBoxLayout(widget)
        vbox.setContentsMargins(0, 0, 0, 0)
        hbox_city = QHBoxLayout()
        check_city = QCheckBox("Bloquear uso em cidades?")
        city_block = CONFIG_FILE.get_value([job.id, AUTO_ITEM, CITY_BLOCK])
        check_city.setChecked(True if city_block else False)
        check_city.checkStateChanged.connect(lambda state: self._update_city_block(state, job))
        hbox_city.addWidget(check_city)
        vbox.addLayout(hbox_city)
        return widget

    def _update_city_block(self, state, job: Job):
        CONFIG_FILE.update_config(state.value == 2, [job.id, AUTO_ITEM, CITY_BLOCK])
