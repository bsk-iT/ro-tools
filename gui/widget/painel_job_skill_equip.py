from PyQt6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QHBoxLayout, QFrame, QPushButton, QCheckBox
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon

from config.icon import ICON_DELETE
from game.buff import EQUIP_BUFFS, Buff
from gui.app_controller import APP_CONTROLLER
from gui.widget.cbox_macro_select import CboxMacroSelect
from gui.widget.cbox_skill import CboxSkill
from gui.widget.input_map_criteria import InputMapCriteria
from service.config_file import ACTIVE, CITY_BLOCK, CONFIG_FILE, MACRO, SKILL_EQUIP
from util.widgets import build_hr, build_icon, build_label_info, build_scroll_vbox, clear_layout


class PainelJobEquipBuff(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self.cbox_skill: CboxSkill = CboxSkill(self, SKILL_EQUIP)
        self._config_layout()
        APP_CONTROLLER.updated_job.connect(self.update_skill_equips)

    def _config_layout(self):
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.layout.setSpacing(10)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.layout.addWidget(self.cbox_skill)
        self.update_skill_equips(APP_CONTROLLER.job)
        APP_CONTROLLER.added_skill_equip.connect(self._on_add_skill)

    def _build_check_block_city(self, job):
        check_city = QCheckBox("Bloquear uso em cidades?")
        city_block = CONFIG_FILE.get_value([job.id, SKILL_EQUIP, CITY_BLOCK])
        check_city.setChecked(True if city_block else False)
        check_city.checkStateChanged.connect(lambda state: self._update_city_block(job, state))
        return check_city

    def _update_city_block(self, job, state):
        CONFIG_FILE.update_config(state.value == 2, [job.id, SKILL_EQUIP, CITY_BLOCK])

    def update_skill_equips(self, job):
        clear_layout(self.layout.takeAt(2))
        clear_layout(self.layout.takeAt(1))
        self.layout.addWidget(self._build_check_block_city(job))
        buff_equips_added = []
        (vbox, scroll) = build_scroll_vbox()
        while job is not None:
            has_skill = False
            vbox_skill_equip = QVBoxLayout()
            active_buff_equips = APP_CONTROLLER.job_equip_skills[job.id]
            vbox_skill_equip.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
            for skill in EQUIP_BUFFS:
                if skill.id not in [a_skill.id for a_skill in active_buff_equips]:
                    continue
                buff_equips_added.append(skill)
                has_skill = True
                vbox_skill_equip.addWidget(self._build_skill_inputs(skill, job.id))
            if has_skill:
                vbox.addWidget(build_label_info(job.name))
                vbox.addLayout(vbox_skill_equip)
            job = job.previous_job
        self.layout.addWidget(scroll)

    def _build_skill_inputs(self, skill: Buff, job_id):
        widget = QWidget()
        vbox = QVBoxLayout(widget)
        hbox = QHBoxLayout()
        hbox.setSpacing(5)
        hbox.setAlignment(Qt.AlignmentFlag.AlignLeft)
        hbox.addWidget(self._build_skill_icon(skill, job_id))
        key_base = f"{job_id}:{SKILL_EQUIP}:{skill.id}:"
        hbox.addWidget(CboxMacroSelect(self, key_base + MACRO))
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
        self.update_skill_equips(APP_CONTROLLER.job)
        CONFIG_FILE.update_config(active, [job_id, SKILL_EQUIP, skill.id, ACTIVE])
        self.cbox_skill.build_cbox(APP_CONTROLLER.job)

    def _on_add_skill(self, job_id, skill: Buff):
        APP_CONTROLLER.job_equip_skills[job_id].append(skill)
        self._active_skill(skill, job_id)
        APP_CONTROLLER.status_toggle.setFocus()

    def _on_remove_skill(self, skill: Buff, job_id):
        APP_CONTROLLER.job_equip_skills[job_id].remove(skill)
        self._active_skill(skill, job_id, False)
