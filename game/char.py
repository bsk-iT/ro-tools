from itertools import chain
import os

from game.jobs import JOB_MAP, Job
from gui.app_controller import APP_CONTROLLER
from service.config_file import ITEM_BUFF
from service.memory import MEMORY
from service.offsets import Offsets
from service.servers_file import SKILL_BUFF, SERVERS_FILE, STATUS_DEBUFF
from util.number import calculate_percent


class Char:

    def __init__(self):
        self.update()

    def reset(self):
        self.current_map = ""
        self.job_id = 0
        self.hp = 0
        self.hp_max = 0
        self.hp_percent = 0
        self.sp = 0
        self.sp_max = 0
        self.sp_percent = 0
        self.raw_buffs = []

    def update(self):
        try:
            self.hp = MEMORY.process.read_int(MEMORY.hp_address)
            self.hp_max = MEMORY.process.read_int(MEMORY.hp_address + Offsets.MAX_HP)
            self.hp_percent = calculate_percent(self.hp, self.hp_max)
            self.sp = MEMORY.process.read_int(MEMORY.hp_address + Offsets.SP)
            self.sp_max = MEMORY.process.read_int(MEMORY.hp_address + Offsets.MAX_SP)
            self.sp_percent = calculate_percent(self.sp, self.sp_max)
            self.current_map = MEMORY.process.read_string(MEMORY.map_address)
            self.job_id = MEMORY.process.read_int(MEMORY.job_address)
            self.raw_buffs = self._get_buffs()
            self.skill_buffs = self._get_id_buffs(SKILL_BUFF)
            self.item_buffs = self._get_id_buffs(ITEM_BUFF)
            self.status_debuff = self._get_id_buffs(STATUS_DEBUFF)
            self.job = JOB_MAP.get(self.job_id, self.job_id)
            self.chat_bar_enabled = MEMORY.process.read_bool(MEMORY.chat_address)
            self.monitoring_job_change_gui()
            os.system("cls")
            print(self)
        except BaseException:
            self.reset()

    def _get_id_buffs(self, resource):
        skill_buffs = []
        for buff in self.raw_buffs:
            skill_buff = SERVERS_FILE.get_value(resource).get(str(buff), None)
            if not skill_buff:
                continue
            skill_buffs.append(skill_buff)
        return skill_buffs

    def next_item_buff_to_use(self, list_items) -> bool:
        for item in list_items:
            if item.id not in self.item_buffs:
                return item
        return None

    def next_item_debuff_to_use(self, list_items) -> bool:
        items_to_use = []
        for item in list_items:
            for status in item.recover_status:
                if status in self.status_debuff:
                    items_to_use.append(item)
        if len(items_to_use) == 0:
            return None
        return sorted(items_to_use, key=lambda item: item.priority, reverse=True)[0]

    def next_skill_buff_to_use(self, list_buff) -> bool:
        buffs_to_use = []
        for job, buffs in list_buff.items():
            for buff in buffs:
                if buff.id not in self.skill_buffs:
                    buffs_to_use.append((job, buff.id, buff.priority))
        if len(buffs_to_use) == 0:
            return None
        return sorted(buffs_to_use, key=lambda x: x[2], reverse=True)[0]

    def monitoring_job_change_gui(self):
        if APP_CONTROLLER.job.id != JOB_MAP[self.job_id].id and isinstance(self.job, Job):
            APP_CONTROLLER.updated_job.emit(self.job)

    def _get_buffs(self):
        buffs = []
        buff_index = 0
        while True:
            buff = MEMORY.process.read_int(MEMORY.hp_address + Offsets.BUFF_LIST + (0x4 * buff_index))
            if buff == -1:
                break
            buffs.append(buff)
            buff_index += 1
        return buffs

    def __str__(self):
        return f"""
            HP: {self.hp}/{self.hp_max}
            SP: {self.sp}/{self.sp_max}
            JOB: {self.job}
            MAP: {self.current_map}
            RAW BUFFS: {self.raw_buffs}
            SKILL_BUFFS: {self.skill_buffs}
            ITEM_BUFFS: {self.item_buffs}
            STATUS_DEBUFF: {self.status_debuff}
            CHAT_BAR_ENABLED: {self.chat_bar_enabled}
        """
