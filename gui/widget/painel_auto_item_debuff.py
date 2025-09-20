from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QHBoxLayout, QFrame, QPushButton, QCheckBox
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon

from config.icon import ICON_DELETE
from game.buff import ITEM_DEBUFF_GROUP, Buff, Buff
from game.jobs import Job
from gui.app_controller import APP_CONTROLLER
from gui.widget.cbox_item import CboxItem
from gui.widget.input_keybind import InputKeybind
from gui.widget.input_map_criteria import InputMapCriteria
from service.config_file import ACTIVE, AUTO_ITEM, CITY_BLOCK, CONFIG_FILE, ITEM_DEBUFF, KEY
from util.widgets import build_hr, build_icon, build_label_info, build_scroll_vbox, clear_layout


class PainelAutoItemDebuff(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self.cbox_item: CboxItem = CboxItem(self, ITEM_DEBUFF)
        self._config_layout()
        APP_CONTROLLER.updated_job.connect(self.update_item_debuffs)

    def _config_layout(self):
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.layout.setSpacing(10)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.layout.addWidget(self.cbox_item)
        self.update_item_debuffs(APP_CONTROLLER.job)
        APP_CONTROLLER.added_item_debuff.connect(self._on_add_skill)

    def update_item_debuffs(self, job: Job):
        clear_layout(self.layout.takeAt(2))
        clear_layout(self.layout.takeAt(1))
        self.layout.addWidget(self._build_config(job))
        self.cbox_item.build_cbox()
        (vbox, scroll) = build_scroll_vbox()
        for group, items in ITEM_DEBUFF_GROUP.items():
            has_item = False
            vbox_item_debuff = QVBoxLayout()
            vbox_item_debuff.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
            for item in items:
                if item.id not in [a_item.id for a_item in APP_CONTROLLER.job_item_debuffs]:
                    continue
                has_item = True
                vbox_item_debuff.addWidget(self._build_item_inputs(job, item))
            if has_item:
                vbox.addWidget(build_label_info(group))
                vbox.addLayout(vbox_item_debuff)
        self.layout.addWidget(scroll)

    def _build_item_inputs(self, job: Job, item: Buff):
        widget = QWidget()
        vbox = QVBoxLayout(widget)
        hbox = QHBoxLayout()
        hbox.setSpacing(5)
        hbox.setAlignment(Qt.AlignmentFlag.AlignLeft)
        hbox.addWidget(self._build_item_icon(job, item))
        key_base = f"{job.id}:{AUTO_ITEM}:{ITEM_DEBUFF}:{item.id}:"
        hbox.addWidget(InputKeybind(self, key_base + KEY))
        hbox.addWidget(InputMapCriteria(self, key_base))
        vbox.addLayout(hbox)
        vbox.addWidget(build_hr())
        return widget

    def _build_item_icon(self, job: Job, item: Buff) -> QFrame:
        frame = QFrame()
        icon_path = item.icon if item.icon is not None else ""
        icon = build_icon(icon_path, item.id, 25, frame)
        icon.move(9, 9)
        frame.setFixedSize(35, 40)
        btn_delete = QPushButton(frame)
        btn_delete.move(0, 0)
        btn_delete.setIcon(QIcon(ICON_DELETE))
        btn_delete.setIconSize(QSize(10, 10))
        btn_delete.setContentsMargins(0, 0, 0, 0)
        btn_delete.clicked.connect(lambda: self._on_remove_item(job, item))
        btn_delete.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        return frame

    def _active_skill(self, job: Job, item: Buff, active=True):
        self.update_item_debuffs(job)
        CONFIG_FILE.update_config(active, [job.id, AUTO_ITEM, ITEM_DEBUFF, item.id, ACTIVE])
        self.cbox_item.build_cbox()

    def _on_add_skill(self, item: Buff):
        APP_CONTROLLER.job_item_debuffs.append(item)
        self._active_skill(APP_CONTROLLER.job, item)
        if APP_CONTROLLER.status_toggle is not None:
            APP_CONTROLLER.status_toggle.setFocus()

    def _on_remove_item(self, job: Job, item: Buff):
        APP_CONTROLLER.job_item_debuffs.remove(item)
        self._active_skill(job, item, False)

    def _build_config(self, job: Job):
        widget = QWidget()
        vbox = QVBoxLayout(widget)
        vbox.setContentsMargins(0, 0, 0, 0)
        hbox_city = QHBoxLayout()
        check_city = QCheckBox("Bloquear uso em cidades?")
        city_block = CONFIG_FILE.get_value([job.id, AUTO_ITEM, ITEM_DEBUFF, CITY_BLOCK])
        check_city.setChecked(True if city_block else False)
        check_city.stateChanged.connect(lambda state: self._update_city_block(state, job))
        hbox_city.addWidget(check_city)
        vbox.addLayout(hbox_city)
        return widget

    def _update_city_block(self, state, job: Job):
        CONFIG_FILE.update_config(state == 2, [job.id, AUTO_ITEM, ITEM_DEBUFF, CITY_BLOCK])
