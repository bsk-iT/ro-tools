from PyQt5.QtWidgets import QWidget, QToolButton, QHBoxLayout, QVBoxLayout, QLabel, QPlainTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from config.icon import ICON_TELEPORT
from gui.widget.input_delay import InputDelay
from gui.widget.input_keybind import InputKeybind
from service.config_file import AUTO_TELEPORT, CONFIG_FILE, MOB_IDS, MACRO_KEY
from util.widgets import ICON_BTN, build_label

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
        self._config_events()

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.toggle)
        self.layout.addWidget(self.config)

    def _build_config(self):
        widget = QWidget()
        hbox = QHBoxLayout(widget)
        vbox = QVBoxLayout()
        vbox.setSpacing(0)
        label_1 = QLabel("Auto Teleport ATIVO")
        label_1.setStyleSheet("color: green; font-size: 10px;")
        label_1.setWordWrap(True)
        vbox.addWidget(label_1)
        vbox.addWidget(build_label('Ao clicar na tecla da "Asa de Mosca" inicia automatização, clicar novamente ou encontrar o mob, irá parar automatização.', 10, True))
        label_2 = QLabel('Adicionar o ID do mob que gostaria de localizar, se for mais de um separar por ";". Ex: 1009;1008;1007')
        label_2.setStyleSheet("color: red; font-size: 10px;")
        label_2.setWordWrap(True)
        vbox.addWidget(label_2)
        text = CONFIG_FILE.read(self.key_base + MOB_IDS) or DEFAULT_MOB_LIST
        self.text_edit.setPlainText(text)
        self.change_mob_id()
        self.text_edit.textChanged.connect(self.change_mob_id)
        hbox_macro_key = QHBoxLayout()
        hbox_macro_key.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignCenter)
        hbox_macro_key.addWidget(InputKeybind(self, self.key_base + MACRO_KEY))
        hbox_macro_key.addWidget(QLabel("Macro do Jogo"))
        hbox_macro_key.addWidget(InputDelay(self, self.key_base))
        vbox_macro_text = QVBoxLayout()
        vbox_macro_text.addLayout(hbox_macro_key)
        vbox_macro_text.addWidget(self.text_edit)
        hbox.addLayout(vbox_macro_text)
        hbox.addLayout(vbox)
        return widget

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
        toggle.setToolTip(f"Auto teleport MOB")
        return toggle

    def _on_active_auto_teleport(self, value: bool) -> None:
        self.config.setVisible(value)
        CONFIG_FILE.update(self.key_base + AUTO_TELEPORT, value)
