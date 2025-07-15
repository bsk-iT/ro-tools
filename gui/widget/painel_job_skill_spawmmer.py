from itertools import chain
from tkinter import ACTIVE
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QSizePolicy, QFrame, QLabel
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon

from config.icon import ICON_DELETE, ICON_SHIELD, ICON_SWORD
from game.spawn_skill import SA_ABRACADABRA, SA_CASTCANCEL, SpawnSkill
from gui.app_controller import APP_CONTROLLER
from gui.widget.cbox_skill import CboxSkill
from gui.widget.input_delay import InputDelay
from gui.widget.input_keybind import InputKeybind
from gui.widget.input_mouse_click import InputMouseClick
from gui.widget.input_mouse_flick import InputMouseFlick
from gui.widget.input_mvp import InputMvp
from gui.widget.input_pet import InputPet
from gui.widget.input_swap import InputSwap
from service.config_file import CONFIG_FILE, KEY, SKILL_SPAWMMER
from util.widgets import build_hr, build_icon, build_label, build_label_info, build_scroll_vbox, clear_layout


class PainelJobSkillSpawmmer(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self.cbox_skill: CboxSkill = CboxSkill(self)
        self._config_layout()
        APP_CONTROLLER.updated_job.connect(self.update_skills_spawnner)

    def _config_layout(self):
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.layout.setSpacing(10)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.layout.addWidget(self.cbox_skill)
        self.update_skills_spawnner()
        APP_CONTROLLER.added_skill_spawmmer.connect(self._on_add_skill)

    def update_skills_spawnner(self, _=None):
        clear_layout(self.layout.takeAt(1))
        job = APP_CONTROLLER.job
        active_spawn_skills = list(chain.from_iterable(APP_CONTROLLER.job_spawn_skills.values()))
        (vbox, scroll) = build_scroll_vbox()
        while job is not None:
            has_skill = False
            vbox_spawn_skill = QVBoxLayout()
            vbox_spawn_skill.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
            for skill in job.spawn_skills:
                if skill.id not in [a_skill.id for a_skill in active_spawn_skills]:
                    continue
                has_skill = True
                vbox_spawn_skill.addWidget(self._build_skill_inputs(skill, job.id))
            if has_skill:
                vbox.addWidget(build_label_info(job.name))
                vbox.addLayout(vbox_spawn_skill)
            job = job.previous_job
        self.layout.addWidget(scroll)

    def _build_skill_inputs(self, skill: SpawnSkill, job_id):
        widget = QWidget()
        vbox = QVBoxLayout(widget)
        hbox = QHBoxLayout()
        hbox.setSpacing(5)
        hbox.setAlignment(Qt.AlignmentFlag.AlignLeft)
        hbox.addWidget(self._build_skill_icon(skill, job_id))
        key_base = f"{job_id}:{SKILL_SPAWMMER}:{skill.id}:"
        is_abracadabra = skill.id == SA_ABRACADABRA.id
        is_cast_cancel = skill.id == SA_CASTCANCEL.id
        hbox.addWidget(InputKeybind(self, key_base + KEY, True))
        if not is_abracadabra and not is_cast_cancel:
            hbox.addWidget(InputMouseClick(self, key_base, skill.is_clicked))
            hbox.addWidget(InputMouseFlick(self, key_base))
        hbox.addWidget(InputDelay(self, key_base))
        if is_abracadabra:
            hbox.addWidget(InputMvp(self, key_base))
            hbox.addWidget(InputPet(self, key_base))
        if not is_abracadabra  and not is_cast_cancel:
            hbox.addWidget(InputSwap(self, "atk", key_base, ICON_SWORD))
            hbox.addWidget(InputSwap(self, "def", key_base, ICON_SHIELD))
        vbox.addLayout(hbox)
        if is_abracadabra:
            vbox.addWidget(self._build_info_abracadabra())
        vbox.addWidget(build_hr())
        return widget

    def _build_info_abracadabra(self):
        widget = QWidget()
        vbox = QVBoxLayout(widget)
        vbox.setSpacing(0)
        label_1 = QLabel("Autocast ATIVO")
        label_1.setStyleSheet("color: green; font-size: 10px;")
        label_1.setWordWrap(True)
        vbox.addWidget(label_1)
        vbox.addWidget(build_label('Ao clicar na tecla da skill "Abracadabra" inicia automatização, clicar novamente ou encontrar a skill selecionada acima irá parar automatização.', 10, True))
        label_2 = QLabel('Para melhor eficiência configurar skill "Cancelar Magia"')
        label_2.setStyleSheet("color: red; font-size: 10px;")
        label_2.setWordWrap(True)
        vbox.addWidget(label_2)
        return widget

    def _build_skill_icon(self, skill: SpawnSkill, job_id) -> QFrame:
        frame = QFrame()
        icon = build_icon(skill.icon, skill.id, 25, frame)
        icon.move(9, 9)
        frame.setFixedSize(35, 40)
        btn_delete = QPushButton(frame)
        btn_delete.move(0, 0)
        btn_delete.setIcon(QIcon(ICON_DELETE))
        btn_delete.setIconSize(QSize(10, 10))
        btn_delete.setContentsMargins(0, 0, 0, 0)
        btn_delete.clicked.connect(lambda: self._on_remove_skill(skill, job_id))
        btn_delete.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        return frame

    def _active_skill(self, skill: SpawnSkill, job_id, active=True):
        APP_CONTROLLER.update_skill_spawmmer(job_id, skill, active)
        self.update_skills_spawnner()
        CONFIG_FILE.update_config(active, [job_id, SKILL_SPAWMMER, skill.id, ACTIVE])
        self.cbox_skill.build_cbox(APP_CONTROLLER.job)

    def _on_add_skill(self, job_id, skill: SpawnSkill):
        self._active_skill(skill, job_id)
        APP_CONTROLLER.status_toggle.setFocus()

    def _on_remove_skill(self, skill: SpawnSkill, job_id):
        self._active_skill(skill, job_id, False)
