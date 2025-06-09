from tkinter import ACTIVE
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QSizePolicy, QScrollArea, QGridLayout, QFrame
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon

from config.icon import ICON_DELETE
from game.spawn_skill import SpawnSkill
from gui.app_controller import APP_CONTROLLER
from gui.widget.cbox_skill import CboxSkill
from gui.widget.input_keybind import InputKeybind
from service.config_file import CONFIG_FILE, SKIL_SPAWNNER
from util.widgets import build_icon, build_label_info, build_label_subtitle, clear_layout


class PainelSpawnSkill(QWidget):

    def __init__(self, parent, cbox_job):
        super().__init__(parent)
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self.cbox_skill: CboxSkill = CboxSkill(self, cbox_job)
        self._config_layout()
        cbox_job.updated_job.connect(lambda job: self.update_grid_skill_spawnner())

    def _config_layout(self):
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(build_label_subtitle("Skill Spawnner"))
        self.layout.addWidget(self.cbox_skill)
        self.update_grid_skill_spawnner()
        self.cbox_skill.updated_skill.connect(self._on_add_skill)

    def update_grid_skill_spawnner(self, columns=3):
        clear_layout(self.layout.takeAt(2))
        job = APP_CONTROLLER.job
        vbox = QVBoxLayout()
        while job is not None:
            has_skill = False
            (grid_spawn_skill, scroll) = self._build_scroll_grid()
            spawn_skills = filter(lambda skill: skill in APP_CONTROLLER.spawn_skills, job.spawn_skills)
            for index, skill in enumerate(spawn_skills):
                has_skill = True
                row = index // columns
                col = index % columns
                grid_spawn_skill.addLayout(self._build_hbox_skill(skill, job.id), row, col)
            if has_skill:
                vbox.addWidget(build_label_info(job.name))
                vbox.addWidget(scroll)
            job = job.previous_job
        self.layout.addLayout(vbox)

    def _build_scroll_grid(self):
        content_widget = QWidget()
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setWidget(content_widget)
        grid_spawn_skill = QGridLayout(content_widget)
        grid_spawn_skill.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        grid_spawn_skill.setHorizontalSpacing(20)
        return (grid_spawn_skill, scroll)

    def _build_hbox_skill(self, skill: SpawnSkill, job_id):
        hbox = QHBoxLayout()
        hbox.setSpacing(5)
        hbox.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        hbox.addWidget(self._build_skill_icon(skill, job_id))
        hbox.addWidget(InputKeybind(self, skill.id))
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
        APP_CONTROLLER.spawn_skills.append(skill) if active else APP_CONTROLLER.spawn_skills.remove(skill)
        self.update_grid_skill_spawnner()
        CONFIG_FILE.update_config(active, [SKIL_SPAWNNER, job_id, skill.id, ACTIVE])
        self.cbox_skill.build_cbox(APP_CONTROLLER.job)

    def _on_add_skill(self, skill: SpawnSkill, job_id):
        self._active_skill(skill, job_id)

    def _on_remove_skill(self, skill: SpawnSkill, job_id):
        self._active_skill(skill, job_id, False)
