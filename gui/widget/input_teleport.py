from PySide6.QtWidgets import QWidget, QToolButton, QHBoxLayout, QVBoxLayout, QLabel, QPlainTextEdit, QSizePolicy
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

from config.icon import ICON_TELEPORT
from gui.widget.input_delay import InputDelay
from gui.widget.input_keybind import InputKeybind
from gui.widget.input_map_region import InputMapRegion
from service.config_file import AUTO_TELEPORT, CELL_RADIUS, CONFIG_FILE, COORDINATE, MOB_IDS, MACRO_KEY, REGIONS, TELEPORT_TYPE, X_POSITION, Y_POSITION
from util.widgets import ICON_BTN, build_label, build_radio_btn, build_spinbox_cells, build_spinbox_position

DEFAULT_MOB_LIST = """--- Comum ---
;12;19; -> Cavaleiro do Abismo [gefenia04]
;13;75; -> Papel [ama_dun02]
;17;13; -> Acidus Dorada [abyss_03]
;12;53; -> Gárgula [gl_sew02]

--- MVP ---
;565; -> B Tomb
;1087; -> Orc Hero [gef_fild02, gef_fild14]
;1492; -> Samurai Encarnado [ama_dun03]
;1832; -> Ifrit [8]
;1112; -> Drake [treasure02]
;1147; -> Maya [anthell02, gld_dun03]
;1159; -> Freeoni [moc_fild17]
;1251; -> Cavaleiro da Tempestade [xmas_dun02]
;1252; -> Haitii [xmas_fild01]
;1623; -> RSX-0806 [ein_dun02]
;1157; -> Farao [in_sphinx5]
;1038; -> Osíris [moc_pryd04]
;1511; -> Amon Ra [moc_pryd06]
;1768; -> Pesar Noturno [ra_san05]
;1115; -> Eddga [gld_dun01, pay_fild11]
;1190; -> Senhor dos Orcs [gef_fild10]
;1373; -> Senhor dos Mortos [niflheim]
;1272; -> Senhor das Trevas [gl_chyard, gld_dun04]
;1059; -> Abelha Rainha [mjolnir_04]
;1871; -> Bispo Decadente [abbey02]
;1873; -> Beelzebub [abbey03]
;1779; -> Ktullanux [ice_dun03]
;1751; -> Valquíria Randrige [odin_tem03]
;1086; -> Besouro-Ladrão Dourado [prt_sewb4]
;1039; -> Bafomé [prt_maze03]
;1917; -> Morocc Ferido [moc_fild22]
;1389; -> Drácula [gef_dun01]
;1046; -> Doppelganger [gef_dun02, gld_dun02]
;1583; -> Tao Gunka [beach_dun]
;1312; -> General Tartaruga [tur_dun04]
;1688; -> Lady Tanee [ayo_dun02]
;1685; -> Vesper [jupe_core]
;1418; -> Serpente Suprema [gon_dun03]
;1885; -> Gopinich [mosk_dun03]
;1719; -> Detardeurus [abyss03]
;1734; -> Kiel D-01 [kh_dun02]
;1630; -> Lady Branca [lou_dun03]

--- Mini ---
;1582; -> Deviling [pay_fild04, yuno_fild03]
;1096; -> Angeling [pay_fild04, xmas_dun01, yuno_fild03]
;1388; -> Archangeling [yuno_fild05]
;1120; -> Ghostring [pay_fild04, treasure02, prt_maze03, gld_dun04]
;1289; -> Maya Puple [anthell01, gld_dun03]
;1765; -> Valquíria [odin_tem02, odin_tem03]
;1302; -> Ilusão das Trevas [gld_dun04, gl_church]
"""


class InputTeleport(QWidget):
    def __init__(self, parent, key_base):
        super().__init__(parent)
        self.key_base = key_base
        self.layout = QHBoxLayout(self)
        self.text_edit = QPlainTextEdit()
        self.toggle = self._build_toggle()
        self.config = self._build_config()
        self._config_layout()
        self.sync_radio_teleport_type()
        self._config_events()

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.toggle)
        self.layout.addWidget(self.config)

    def _build_config(self):
        widget = QWidget()
        vbox = QVBoxLayout(widget)
        vbox.setSpacing(5)
        text = CONFIG_FILE.read(self.key_base + MOB_IDS) or DEFAULT_MOB_LIST
        self.text_edit.setPlainText(text)
        self.change_mob_id()
        self.text_edit.textChanged.connect(self.change_mob_id)
        hbox_macro_key = QHBoxLayout()
        hbox_macro_key.setContentsMargins(0, 0, 0, 0)
        hbox_macro_key.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignCenter)
        hbox_macro_key.addWidget(InputDelay(self, self.key_base))
        hbox_macro_key.addWidget(InputKeybind(self, self.key_base + MACRO_KEY))
        hbox_macro_key.addWidget(QLabel("Macro do Jogo"))
        vbox.addWidget(self._build_label("Auto Teleport - ATIVO", "green", 14))
        vbox.addWidget(build_label('Ao clicar na tecla da "Asa de Mosca" inicia automatização, clicar novamente ou atender o critério de uso, irá parar automatização.', 14, True))
        vbox.addLayout(hbox_macro_key)
        vbox.addWidget(self._build_radio_keyboard_type())
        vbox.addWidget(self._build_tele_mob())
        vbox.addWidget(self._build_tele_region())
        vbox.addWidget(self._build_tele_coordinates())
        return widget

    def _build_radio_keyboard_type(self):
        widget = QWidget()
        vbox = QVBoxLayout(widget)
        vbox.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        vbox.setSpacing(5)
        vbox.setContentsMargins(0, 10, 0, 0)
        vbox.addWidget(QLabel("Selecione o tipo de Auto Teletransporte:"))
        self.rad_mob_id = build_radio_btn("Mob ID - Localizar o monstro na tela pelo seu ID.")
        self.rad_region = build_radio_btn("Região - Região do mapa que gostaria de se teletransportar.")
        self.rad_coord = build_radio_btn("Coordenada - Parar aproximadamente na coordenada informada.")
        self.rad_mob_id.clicked.connect(self.on_radio_keyboard_type)
        self.rad_region.clicked.connect(self.on_radio_keyboard_type)
        self.rad_coord.clicked.connect(self.on_radio_keyboard_type)
        vbox.addWidget(self.rad_mob_id)
        vbox.addWidget(self.rad_region)
        vbox.addWidget(self.rad_coord)
        return widget

    def on_radio_keyboard_type(self):
        if self.rad_mob_id.isChecked():
            CONFIG_FILE.update(self.key_base + TELEPORT_TYPE, MOB_IDS)
            self.sync_option_auto_tele(MOB_IDS)
        if self.rad_region.isChecked():
            CONFIG_FILE.update(self.key_base + TELEPORT_TYPE, REGIONS)
            self.sync_option_auto_tele(REGIONS)
        if self.rad_coord.isChecked():
            CONFIG_FILE.update(self.key_base + TELEPORT_TYPE, COORDINATE)
            self.sync_option_auto_tele(COORDINATE)

    def sync_radio_teleport_type(self):
        teleport_type = CONFIG_FILE.read(self.key_base + TELEPORT_TYPE)
        if teleport_type is None:
            teleport_type = MOB_IDS
            CONFIG_FILE.update(self.key_base + TELEPORT_TYPE, teleport_type)
        if teleport_type == MOB_IDS:
            self.rad_mob_id.setChecked(True)
        if teleport_type == REGIONS:
            self.rad_region.setChecked(True)
        if teleport_type == COORDINATE:
            self.rad_coord.setChecked(True)
        self.sync_option_auto_tele(teleport_type)

    def sync_option_auto_tele(self, teleport_type):
        self.tele_mob.setVisible(teleport_type == MOB_IDS)
        self.tele_region.setVisible(teleport_type == REGIONS)
        self.tele_coordinate.setVisible(teleport_type == COORDINATE)

    def _build_tele_mob(self):
        self.tele_mob = QWidget()
        vbox = QVBoxLayout(self.tele_mob)
        vbox.setContentsMargins(0, 10, 0, 0)
        vbox.addWidget(self.text_edit)
        return self.tele_mob

    def _build_tele_region(self):
        self.tele_region = QWidget()
        vbox = QVBoxLayout(self.tele_region)
        vbox.setContentsMargins(0, 10, 0, 0)
        vbox.addWidget(InputMapRegion(self.tele_region, self.key_base))
        return self.tele_region

    def _build_tele_coordinates(self):
        self.tele_coordinate = QWidget()
        self.tele_coordinate.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        hbox = QHBoxLayout(self.tele_coordinate)
        hbox.setAlignment(Qt.AlignmentFlag.AlignLeft)
        hbox.setSpacing(20)
        hbox.setContentsMargins(0, 10, 0, 0)
        cell_radius = CONFIG_FILE.read(self.key_base + CELL_RADIUS)
        if not cell_radius:
            CONFIG_FILE.update(self.key_base + CELL_RADIUS, 30)
        hbox.addWidget(build_spinbox_position(self.key_base + X_POSITION, "X"))
        hbox.addWidget(build_spinbox_position(self.key_base + Y_POSITION, "Y"))
        hbox.addWidget(build_spinbox_cells(self.key_base + CELL_RADIUS, "Distância Max."))
        return self.tele_coordinate

    def _build_label(self, text, color, fontSize=12):
        label = QLabel(text)
        label.setStyleSheet(f"color: {color}; font-size: {fontSize}px;")
        label.setWordWrap(True)
        return label

    def change_mob_id(self):
        CONFIG_FILE.update(self.key_base + MOB_IDS, self.text_edit.toPlainText())

    def _config_events(self) -> None:
        self.toggle.toggled.connect(self._on_active_auto_teleport)
        self._on_active_auto_teleport(self.toggle.isChecked())

    def _build_toggle(self) -> QToolButton:
        toggle = QToolButton()
        toggle.setCheckable(True)
        active = CONFIG_FILE.read(self.key_base + AUTO_TELEPORT)
        toggle.setChecked(active if active else False)
        toggle.setIcon(QIcon(ICON_TELEPORT))
        toggle.setIconSize(ICON_BTN)
        return toggle

    def _on_active_auto_teleport(self, value: bool) -> None:
        self.config.setVisible(value)
        self.toggle.setToolTip(f"Auto teleport - {"LIGADO" if value else "DESLIGADO"}")
        CONFIG_FILE.update(self.key_base + AUTO_TELEPORT, value)
