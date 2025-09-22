from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QHBoxLayout, QFrame, QPushButton, QLabel, QPlainTextEdit
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon

from config.icon import ICON_DELETE
from game.macro import ELEMENT_DARK, ELEMENT_FIRE, ELEMENT_GHOST, ELEMENT_EARTH, ELEMENT_HOLY, ELEMENT_WATER, ELEMENT_WIND, MACRO_MAP, Macro
from gui.app_controller import APP_CONTROLLER
from gui.widget.cbox_macro import CboxMacro
from service.config_file import ACTIVE, AUTO_ELEMENT, CONFIG_FILE, MOB_IDS
from util.widgets import build_hr, build_icon, build_label_info, build_scroll_vbox, clear_layout

DEFAULT_FIRE = """--- Cheffênia ---

Tier S:
;2087; -> Queen Scaraba [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20202; -> Mestre-Ferreiro Howard [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]

Tier A:
;20194; -> Senhor dos Orcs [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]

Tier B:
;20181; -> Amon Ra [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20200; -> General Tartaruga [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20191; -> Maya [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;21284; -> E Cowraiders1 [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;21285; -> E Cowraiders2 [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;3749; -> E Cowraiders3 [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20239; -> Gorynynch [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20195; -> Orc Herói [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;21281; -> Outono Ancestral [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]

Tier C:
;20236; -> Lady Branca [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
"""

DEFAULT_WATER = """--- Cheffênia ---

Tier S:
;20220; -> Ifrit [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20201; -> Lorde Seyren [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20227; -> Criador Flamel [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]

Tier A:
;20243; -> Skoll [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;21301; -> Presa Flamejante [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]

Tier B:
;20215; -> Egnigem Cenia [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20187; -> Eddga [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20193; -> Flor do Luar [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20240; -> Boitata [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20189; -> Besouro-Ladrão Dourado [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;21282; -> Verão Ancestral [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]

Tier C:
;20247; -> Mestre Chen [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
"""

DEFAULT_EARTH = """--- Cheffênia ---

Tier S:
;20225; -> Atiradora de Elite Cecil [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20248; -> Menestrel Alphochio [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]

Tier A:
;20228; -> Cigana Trentini [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]

Tier B:
;20192; -> Abelha-Rainha [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20190; -> Cavaleiro da Tempestade [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20236; -> Lady Tanee [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;21280; -> Primavera Ancestral [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]

Tier C:
;20236; -> Lady Branca [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
"""

DEFAULT_WIND = """--- Cheffênia ---

Tier S:
;20233; -> Kraken [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20221; -> Ktullanux [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]

Tier B:
;20188; -> Hatii [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20251; -> Polvo Gigante [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;21283; -> Inverno Ancestral [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;2538; -> Rei Poring [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]

Tier C:
;20247; -> Mestre Chen [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
"""

DEFAULT_HOLY = """--- Cheffênia ---

Tier S:
;2529; -> Rainha Verme [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20180; -> Morroc Ferido [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;21287; -> Amdarais Corrompido [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20203; -> Algoz Eremes [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]

Tier A:
;20216; -> Atroce [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20218; -> Bispo Decadente [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20212; -> Kiel D-01 [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;3659; -> Rei da Noite [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20230; -> Réquiem de Marfim [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;2131; -> Drogon [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20891; -> Venomorfo Perfeito [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;2476; -> Amdarais [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]

Tier B:
;20206; -> Senhor dos Mortos [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20182; -> Bafomé [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20183; -> Senhor das Trevas [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20209; -> Detardeurus [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]

Tier C:
;20185; -> Drácula [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20186; -> Drake [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20197; -> Faraó [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20235; -> Samurai Encarnado [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20184; -> Doppelganger [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20196; -> Osíris [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
"""

DEFAULT_DARK = """--- Cheffênia ---

Tier S:
;20213; -> Valquíria Randgris [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20242; -> Avatar de Freya [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20205; -> Sacerdotisa Margaretha [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20226; -> Paladino Randel [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]

Tier B:
;20211; -> Vesper [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
"""

DEFAULT_GHOST = """--- Cheffênia ---

Tier S:
;20217; -> Belzebu [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20208; -> Naght Sieger [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20244; -> Gioia [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]

Tier A:
;20252; -> Celine Kimi [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20219; -> Pesar Noturno [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20618; -> Detardeurus Esquelético [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20241; -> Groteskia [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20210; -> Memória de Thanatos [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]

Tier B:
;20237; -> Serpente Suprema [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20198; -> Freeoni [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20204; -> Arquimaga Kathryne [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20246; -> Professora Celia [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20253; -> Fenrir [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
;20199; -> Tao Gunka [cheffenia01, cheffenia02, cheffenia03, cheffenia04, cheffenia05, cheffenia06]
"""

DEFAULT_ATTACK_TEAM = """--- IDs de Monstros para Equipes de Ataque ---;1001; -> Escorpião
;1002; -> Aranha
;1004; -> Erva Daninha
"""

DEFAULT_DEFENSE_TEAM = """--- IDs de Monstros para Equipes de Defesa ---

;1087; -> Herói Orc
;1112; -> Drake
;1115; -> Eddga
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
        from game.macro import ATK_1, ATK_2, ATK_3, ATK_4, ATK_5, DEF_1, DEF_2, DEF_3, DEF_4, DEF_5
        
        defaults = {
            ELEMENT_FIRE.id: DEFAULT_FIRE,
            ELEMENT_WATER.id: DEFAULT_WATER,
            ELEMENT_EARTH.id: DEFAULT_EARTH,
            ELEMENT_WIND.id: DEFAULT_WIND,
            ELEMENT_HOLY.id: DEFAULT_HOLY,
            ELEMENT_DARK.id: DEFAULT_DARK,
            ELEMENT_GHOST.id: DEFAULT_GHOST,
            # Equipes de Ataque
            ATK_1.id: DEFAULT_ATTACK_TEAM,
            ATK_2.id: DEFAULT_ATTACK_TEAM,
            ATK_3.id: DEFAULT_ATTACK_TEAM,
            ATK_4.id: DEFAULT_ATTACK_TEAM,
            ATK_5.id: DEFAULT_ATTACK_TEAM,
            # Equipes de Defesa
            DEF_1.id: DEFAULT_DEFENSE_TEAM,
            DEF_2.id: DEFAULT_DEFENSE_TEAM,
            DEF_3.id: DEFAULT_DEFENSE_TEAM,
            DEF_4.id: DEFAULT_DEFENSE_TEAM,
            DEF_5.id: DEFAULT_DEFENSE_TEAM,
        }
        
        return defaults.get(macro_id, "")

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
        if APP_CONTROLLER.status_toggle is not None:
            APP_CONTROLLER.status_toggle.setFocus()

    def _on_remove_auto_element(self, job_id, macro: Macro):
        APP_CONTROLLER.job_auto_elements[job_id].remove(macro)
        self._active_auto_element(job_id, macro, False)
