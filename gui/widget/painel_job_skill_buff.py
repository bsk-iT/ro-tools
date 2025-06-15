from itertools import chain
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QHBoxLayout, QFrame, QPushButton
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon

from config.icon import ICON_DELETE
from game.buff import Buff
from gui.app_controller import APP_CONTROLLER
from gui.widget.cbox_skill import CboxSkill
from gui.widget.input_delay import InputDelay
from gui.widget.input_keybind import InputKeybind
from gui.widget.input_map_criteria import InputMapCriteria
from service.config_file import ACTIVE, CONFIG_FILE, KEY, SKILL_BUFF
from util.widgets import build_hr, build_icon, build_label_info, build_scroll_vbox, clear_layout


class PainelJobSkillBuff(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self.cbox_skill: CboxSkill = CboxSkill(self, SKILL_BUFF)
        self._config_layout()
        APP_CONTROLLER.updated_job.connect(self.update_buff_skills)

    def _config_layout(self):
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.layout.addWidget(self.cbox_skill)
        self.update_buff_skills(APP_CONTROLLER.job)
        APP_CONTROLLER.added_skill_buff.connect(self._on_add_skill)

    def update_buff_skills(self, job):
        clear_layout(self.layout.takeAt(1))
        active_buff_skills = list(chain.from_iterable(APP_CONTROLLER.job_buff_skills.values()))
        (vbox, scroll) = build_scroll_vbox()
        while job is not None:
            has_skill = False
            vbox_buff_skill = QVBoxLayout()
            vbox_buff_skill.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
            for skill in job.buff_skills:
                if skill.id not in [a_skill.id for a_skill in active_buff_skills]:
                    continue
                has_skill = True
                vbox_buff_skill.addWidget(self._build_skill_inputs(skill, job.id))
            if has_skill:
                vbox.addWidget(build_label_info(job.name))
                vbox.addLayout(vbox_buff_skill)
            job = job.previous_job
        self.layout.addWidget(scroll)

    def _build_skill_inputs(self, skill: Buff, job_id):
        widget = QWidget()
        vbox = QVBoxLayout(widget)
        hbox = QHBoxLayout()
        hbox.setSpacing(5)
        hbox.setAlignment(Qt.AlignmentFlag.AlignLeft)
        hbox.addWidget(self._build_skill_icon(skill, job_id))
        key_base = f"{SKILL_BUFF}:{job_id}:{skill.id}:"
        hbox.addWidget(InputKeybind(self, key_base + KEY, True))
        hbox.addWidget(InputDelay(self, key_base))
        hbox.addWidget(InputMapCriteria(self, key_base))
        vbox.addLayout(hbox)
        vbox.addWidget(build_hr())
        return widget

    def _build_skill_icon(self, skill: Buff, job_id) -> QFrame:
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

    def _active_skill(self, skill: Buff, job_id, active=True):
        self.update_buff_skills(APP_CONTROLLER.job)
        CONFIG_FILE.update_config(active, [SKILL_BUFF, job_id, skill.id, ACTIVE])
        self.cbox_skill.build_cbox(APP_CONTROLLER.job)

    def _on_add_skill(self, skill: Buff, job_id):
        APP_CONTROLLER.job_buff_skills[job_id].append(skill)
        self._active_skill(skill, job_id)
        APP_CONTROLLER.status_toggle.setFocus()

    def _on_remove_skill(self, skill: Buff, job_id):
        APP_CONTROLLER.job_buff_skills[job_id].remove(skill)
        self._active_skill(skill, job_id, False)
