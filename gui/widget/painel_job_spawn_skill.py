from itertools import chain
from tkinter import ACTIVE
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QSizePolicy, QScrollArea, QGridLayout, QFrame
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon

from config.icon import ICON_DELETE
from game.spawn_skill import SpawnSkill
from gui.app_controller import APP_CONTROLLER
from gui.widget.cbox_skill import CboxSkill
from gui.widget.input_delay import InputDelay
from gui.widget.input_keybind import InputKeybind
from gui.widget.input_mouse_click import InputMouseClick
from service.config_file import CONFIG_FILE, DELAY, DELAY_ACTIVE, KEY, MOUSE_CLICK, SKILL_SPAWNNER
from util.widgets import build_icon, build_label_info, clear_layout


class PainelJobSpawnSkill(QWidget):

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
        (vbox, scroll) = self._build_scroll_vbox()
        while job is not None:
            has_skill = False 
            vbox_spawn_skill = QVBoxLayout()
            vbox_spawn_skill.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
            for skill in filter(lambda skill: skill in active_spawn_skills, job.spawn_skills):
                has_skill = True
                vbox_spawn_skill.addLayout(self._build_hbox_skill(skill, job.id))
            if has_skill:
                vbox.addWidget(build_label_info(job.name))
                vbox.addLayout(vbox_spawn_skill)
            job = job.previous_job
        self.layout.addWidget(scroll)

    def _build_scroll_vbox(self):
        content_widget = QWidget()
        scroll = QScrollArea()
        scroll.setFixedHeight(300)
        scroll.setWidgetResizable(True)
        scroll.setWidget(content_widget)
        vbox_spawn_skill = QVBoxLayout(content_widget)
        vbox_spawn_skill.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        return (vbox_spawn_skill, scroll)

    def _build_hbox_skill(self, skill: SpawnSkill, job_id):
        hbox = QHBoxLayout()
        hbox.setSpacing(5)
        hbox.setAlignment(Qt.AlignmentFlag.AlignLeft)
        hbox.addWidget(self._build_skill_icon(skill, job_id))
        key_base = f"{SKILL_SPAWNNER}:{job_id}:{skill.id}:"
        hbox.addWidget(InputKeybind(self, key_base + KEY))
        hbox.addWidget(InputMouseClick(self, key_base + MOUSE_CLICK, skill.is_clicked))
        hbox.addWidget(InputDelay(self, key_base + DELAY_ACTIVE, key_base + DELAY))
        return hbox

    def _build_skill_icon(self, skill: SpawnSkill, job_id) -> QFrame:
        frame = QFrame()
        icon = build_icon(skill.icon, skill.id, 5, frame)
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
        APP_CONTROLLER.job_spawn_skills[job_id].append(skill) if active else APP_CONTROLLER.job_spawn_skills[job_id].remove(skill)
        self.update_skills_spawnner()
        CONFIG_FILE.update_config(active, [SKILL_SPAWNNER, job_id, skill.id, ACTIVE])
        self.cbox_skill.build_cbox(APP_CONTROLLER.job)

    def _on_add_skill(self, skill: SpawnSkill, job_id):
        self._active_skill(skill, job_id)
        self.cbox_skill.clearFocus()

    def _on_remove_skill(self, skill: SpawnSkill, job_id):
        self._active_skill(skill, job_id, False)
