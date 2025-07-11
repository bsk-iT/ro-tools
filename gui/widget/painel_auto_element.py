from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QHBoxLayout, QFrame, QPushButton, QLabel, QPlainTextEdit
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon

from config.icon import ICON_DELETE
from game.macro import ELEMENT_DARK, ELEMENT_FIRE, ELEMENT_GHOST, ELEMENT_GROUND, ELEMENT_HOLY, ELEMENT_WATER, ELEMENT_WIND, MACRO_MAP, Macro
from gui.app_controller import APP_CONTROLLER
from gui.widget.cbox_macro import CboxMacro
from service.config_file import ACTIVE, AUTO_ELEMENT, CONFIG_FILE, MOB_IDS
from util.widgets import build_hr, build_icon, build_label_info, build_scroll_vbox, clear_layout

DEFAULT_FIRE = """--- Comum ---

--- MVP ---
;1087; -> Orc Hero [gef_fild02, gef_fild14]
;1147; -> Maya [anthell02, gld_dun03]
;1159; -> Freeoni [moc_fild17]
;1511; -> Amon Ra [moc_pryd06]
;1190; -> Senhor dos Orcs [gef_fild10]
;1312; -> General Tartaruga [tur_dun04]
;1885; -> Gopinich [mosk_dun03]
;1648; -> Mestre Ferreiro Howard [lhz_dun03]

--- Mini ---
;1289; -> Maya Puple [anthell01, gld_dun03]
"""

DEFAULT_WATER = """--- Comum ---

--- MVP ---
;1832; -> Ifrit [thor_v03]
;1115; -> Eddga [gld_dun01, pay_fild11]
;1086; -> Besouro-Ladrão Dourado [prt_sewb4]
;1652; -> Egnigem Cenia [lhz_dun02]
;1646; -> Lorde Seyren [lhz_dun03]

--- Mini ---
"""

DEFAULT_GROUND = """--- Comum ---
;12;53; -> Gárgula [gl_sew02]

--- MVP ---
;1251; -> Cavaleiro da Tempestade [xmas_dun02]
;1059; -> Abelha Rainha [mjolnir_04]
;1688; -> Lady Tanee [ayo_dun02]
;1630; -> Lady Branca [lou_dun03]
;1650; -> Atiradora de Elite Ceci [lhz_dun03]


--- Mini ---
"""

DEFAULT_WIND = """--- Comum ---

--- MVP ---
;1252; -> Haitii [xmas_fild01]
;1779; -> Ktullanux [ice_dun03]

--- Mini ---
"""

DEFAULT_HOLY = """--- Comum ---
;12;19; -> Cavaleiro do Abismo [gefenia04]
;13;75; -> Papel [ama_dun02]

--- MVP ---
;1492; -> Samurai Encarnado [ama_dun03]
;1112; -> Drake [treasure02]
;1623; -> RSX-0806 [ein_dun02]
;1157; -> Faraó [in_sphinx5]
;1038; -> Osíris [moc_pryd04]
;1373; -> Senhor dos Mortos [niflheim]
;1272; -> Senhor das Trevas [gl_chyard, gld_dun04]
;1871; -> Bispo Decadente [abbey02]
;1039; -> Bafomé [prt_maze03]
;1917; -> Morocc Ferido [moc_fild22]
;1389; -> Drácula [gef_dun01]
;1046; -> Doppelganger [gef_dun02, gld_dun02]
;1583; -> Tao Gunka [beach_dun]
;1719; -> Detardeurus [abyss03]
;1734; -> Kiel D-01 [kh_dun02]
;2022; -> Sombra de Nidhogg
;1647; -> Algoz Eremes [lhz_dun03]
;1785; -> Atroce [ra_fild02, ra_fild03, ra_fild04, ve_fild01, ve_fild02]

--- Mini ---
;1582; -> Deviling [pay_fild04, yuno_fild03]
;1302; -> Ilusão das Trevas [gld_dun04, gl_church]
"""

DEFAULT_DARK = """--- Comum ---
;17;13; -> Acidus Dorada [abyss_03]

--- MVP ---
;1751; -> Valquíria Randrige [odin_tem03]
;1685; -> Vesper [jupe_core]
;1649; -> Suma-Sacerdote Margar [lhz_dun03]

--- Mini ---
;1096; -> Angeling [pay_fild04, xmas_dun01, yuno_fild03]
;1388; -> Archangeling [yuno_fild05]
;1765; -> Valquíria [odin_tem02, odin_tem03]
"""

DEFAULT_GHOST = """--- Comum ---

--- MVP ---
;1768; -> Pesar Noturno [ra_san05]
;1873; -> Beelzebub [abbey03]
;1418; -> Serpente Suprema [gon_dun03]
;1651; -> Arquimaga Kathryne [lhz_dun03]

--- Mini ---
;1120; -> Ghostring [pay_fild04, treasure02, prt_maze03, gld_dun04]
"""


class PainelAutoElement(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self.cbox_macro: CboxMacro = CboxMacro(self, AUTO_ELEMENT)
        self._config_layout()
        APP_CONTROLLER.updated_job.connect(self.update_auto_elements)

    def _config_layout(self):
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.layout.setSpacing(10)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.layout.addWidget(self.cbox_macro)
        APP_CONTROLLER.added_auto_element.connect(self._on_add_auto_element)
        self.update_auto_elements(APP_CONTROLLER.job)

    def update_auto_elements(self, job):
        clear_layout(self.layout.takeAt(1))
        (vbox, scroll) = build_scroll_vbox()
        while job is not None:
            has_auto_element = False
            active_auto_elements = APP_CONTROLLER.job_auto_elements[job.id]
            vbox_hotkey = QVBoxLayout()
            vbox_hotkey.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
            for macro in MACRO_MAP.values():
                if macro.id not in [a_macro.id for a_macro in active_auto_elements]:
                    continue
                has_auto_element = True
                vbox_hotkey.addWidget(self._build_auto_elements_inputs(macro, job.id))
            if has_auto_element:
                vbox.addWidget(build_label_info(job.name))
                vbox.addLayout(vbox_hotkey)
            job = job.previous_job
        self.layout.addWidget(scroll)

    def _build_auto_elements_inputs(self, macro: Macro, job_id):
        mob_ids_key_base = f"{AUTO_ELEMENT}:{macro.id}:{MOB_IDS}"
        widget = QWidget()
        vbox = QVBoxLayout(widget)
        hbox = QHBoxLayout()
        hbox.setSpacing(5)
        hbox.setAlignment(Qt.AlignmentFlag.AlignLeft)
        hbox.addWidget(self._build_auto_element_icon(macro, job_id))
        text = CONFIG_FILE.read(mob_ids_key_base) or self._get_default_text(macro.id)
        mob_text = QPlainTextEdit(text)
        mob_text.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.change_mob_id(mob_ids_key_base, mob_text)
        mob_text.textChanged.connect(lambda: self.change_mob_id(mob_ids_key_base, mob_text))
        label = QLabel(macro.name)
        label.setObjectName(macro.id)
        hbox.addWidget(label)
        hbox.addWidget(mob_text)
        vbox.addLayout(hbox)
        vbox.addWidget(build_hr())
        return widget

    def _get_default_text(self, macro_id):
        return {
            ELEMENT_FIRE.id: DEFAULT_FIRE,
            ELEMENT_WATER.id: DEFAULT_WATER,
            ELEMENT_GROUND.id: DEFAULT_GROUND,
            ELEMENT_WIND.id: DEFAULT_WIND,
            ELEMENT_HOLY.id: DEFAULT_HOLY,
            ELEMENT_DARK.id: DEFAULT_DARK,
            ELEMENT_GHOST.id: DEFAULT_GHOST,
        }[macro_id]

    def change_mob_id(self, mob_ids_key_base, mob_text):
        CONFIG_FILE.update(mob_ids_key_base, mob_text.toPlainText())

    def _build_auto_element_icon(self, macro: Macro, job_id) -> QFrame:
        frame = QFrame()
        icon = build_icon(macro.icon, macro.id, 25, frame)
        icon.move(9, 9)
        frame.setFixedSize(35, 40)
        btn_delete = QPushButton(frame)
        btn_delete.move(0, 0)
        btn_delete.setIcon(QIcon(ICON_DELETE))
        btn_delete.setIconSize(QSize(10, 10))
        btn_delete.setContentsMargins(0, 0, 0, 0)
        btn_delete.clicked.connect(lambda: self._on_remove_auto_element(job_id, macro))
        btn_delete.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        return frame

    def _active_auto_element(self, job_id, macro: Macro, active=True):
        self.update_auto_elements(APP_CONTROLLER.job)
        CONFIG_FILE.update_config(active, [job_id, AUTO_ELEMENT, macro.id, ACTIVE])
        self.cbox_macro.build_cbox(APP_CONTROLLER.job)

    def _on_add_auto_element(self, job_id, macro: Macro):
        APP_CONTROLLER.job_auto_elements[job_id].append(macro)
        self._active_auto_element(job_id, macro)
        APP_CONTROLLER.status_toggle.setFocus()

    def _on_remove_auto_element(self, job_id, macro: Macro):
        APP_CONTROLLER.job_auto_elements[job_id].remove(macro)
        self._active_auto_element(job_id, macro, False)
