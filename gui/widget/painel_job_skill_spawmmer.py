from itertools import chain
from tkinter import ACTIVE
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QSizePolicy, QFrame
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon

from config.icon import ICON_DELETE, ICON_SHIELD, ICON_SWORD
from game.spawn_skill import SpawnSkill
from gui.app_controller import APP_CONTROLLER
from gui.widget.cbox_skill import CboxSkill
from gui.widget.input_delay import InputDelay
from gui.widget.input_keybind import InputKeybind
from gui.widget.input_mouse_click import InputMouseClick
from gui.widget.input_swap import InputSwap
from service.config_file import CONFIG_FILE, KEY, SKILL_SPAWMMER
from util.widgets import build_hr, build_icon, build_label_info, build_scroll_vbox, clear_layout


class PainelJobSkillSpawmmer(QWidget):

    def __init__(self, parent, cbox_job):
        super().__init__(parent)
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self.cbox_skill: CboxSkill = CboxSkill(self, cbox_job)
        self._config_layout()
        cbox_job.updated_job.connect(lambda job: self.update_skills_spawnner())

    def _config_layout(self):
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.layout.addWidget(self.cbox_skill)
        self.update_skills_spawnner()
        self.cbox_skill.updated_skill.connect(self._on_add_skill)

    def update_skills_spawnner(self):
        clear_layout(self.layout.takeAt(1))
        job = APP_CONTROLLER.job
        active_spawn_skills = list(chain.from_iterable(APP_CONTROLLER.job_spawn_skills.values()))
        (vbox, scroll) = build_scroll_vbox()
        while job is not None:
            has_skill = False
            vbox_spawn_skill = QVBoxLayout()
            vbox_spawn_skill.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
            for skill in filter(lambda skill: skill in active_spawn_skills, job.spawn_skills):
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
        key_base = f"{SKILL_SPAWMMER}:{job_id}:{skill.id}:"
        hbox.addWidget(InputKeybind(self, key_base + KEY, True))
        hbox.addWidget(InputMouseClick(self, key_base, skill.is_clicked))
        hbox.addWidget(InputDelay(self, key_base))
        hbox.addWidget(InputSwap(self, "atk", key_base, ICON_SWORD))
        hbox.addWidget(InputSwap(self, "def", key_base, ICON_SHIELD))
        vbox.addLayout(hbox)
        vbox.addWidget(build_hr())
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
        APP_CONTROLLER.update_skill_spawmmer(skill, active)
        self.update_skills_spawnner()
        CONFIG_FILE.update_config(active, [SKILL_SPAWMMER, job_id, skill.id, ACTIVE])
        self.cbox_skill.build_cbox(APP_CONTROLLER.job)

    def _on_add_skill(self, skill: SpawnSkill, job_id):
        self._active_skill(skill, job_id)
        self.cbox_skill.clearFocus()

    def _on_remove_skill(self, skill: SpawnSkill, job_id):
        self._active_skill(skill, job_id, False)
