import os
from game.jobs import JOB_MAP, Job
from gui.app_controller import APP_CONTROLLER
from service.memory import MEMORY
from service.offsets import Offsets
from service.servers_file import BUFF_SKILL, SERVERS_FILE
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
        self.buffs = []

    def update(self):
        try:
            self.hp = MEMORY.process.read_int(MEMORY.hp_address)
            self.hp_max = MEMORY.process.read_int(MEMORY.hp_address + Offsets.MAX_HP)
            self.hp_percent = calculate_percent(self.hp, self.hp_max)
            self.sp = MEMORY.process.read_int(MEMORY.hp_address + Offsets.SP)
            self.sp_max = MEMORY.process.read_int(MEMORY.hp_address + Offsets.MAX_SP)
            self.sp_percent = calculate_percent(self.sp, self.sp_max)
            self.current_map = MEMORY.process.read_string(MEMORY.map_address)
            self.job_id = MEMORY.process.read_int(MEMORY.hp_address + Offsets.JOB_ID)
            self.buffs = self._get_buffs()
            self.job = JOB_MAP.get(self.job_id, self.job_id)
            self.chat_bar_enabled = MEMORY.process.read_bool(MEMORY.base_address + Offsets.CHAT_BAR_ENABLED)
            if APP_CONTROLLER.job.id != self.job_id and isinstance(self.job, Job):
                APP_CONTROLLER.emit_change_job(self.job)
            os.system("cls")
            print(self)
        except BaseException:
            self.reset()

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
        buff_skills = [SERVERS_FILE.get_value(BUFF_SKILL).get(str(buff), buff) for buff in self.buffs]
        return f"""
            HP: {self.hp}/{self.hp_max}
            SP: {self.sp}/{self.sp_max}
            JOB: {self.job}
            MAP: {self.current_map}
            BUFFS: {buff_skills}
            CHAT_BAR_ENABLED: {self.chat_bar_enabled}
        """
