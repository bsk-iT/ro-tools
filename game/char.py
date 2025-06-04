import os
from game.buffs import BUFF_MAP
from game.jobs import JOB_MAP
from service.memory import MEMORY
from service.offsets import Offsets
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
            self.hp = MEMORY.process.read_int(MEMORY.get_address(Offsets.HP))
            self.hp_max = MEMORY.process.read_int(MEMORY.get_address(Offsets.MAX_HP))
            self.hp_percent = calculate_percent(self.hp, self.hp_max)
            self.sp = MEMORY.process.read_int(MEMORY.get_address(Offsets.SP))
            self.sp_max = MEMORY.process.read_int(MEMORY.get_address(Offsets.MAX_SP))
            self.sp_percent = calculate_percent(self.sp, self.sp_max)
            self.current_map = MEMORY.process.read_string(MEMORY.get_address(Offsets.MAP))
            self.job_id = MEMORY.process.read_int(MEMORY.get_address(Offsets.JOB_ID))
            self.buffs = self._get_buffs()
            os.system("cls")
            print(self)
        except BaseException:
            self.reset()

    def _get_buffs(self):
        buffs = []
        buff_index = 0
        while True:
            buff = MEMORY.process.read_int(MEMORY.get_address(Offsets.BUFF_LIST) + 0x4 * buff_index)
            if buff == -1:
                break
            buffs.append(buff)
            buff_index += 1
        return buffs

    def __str__(self):
        return f'HP: {self.hp}/{self.hp_max}\nSP: {self.sp}/{self.sp_max}\nJOB: {JOB_MAP.get(self.job_id, self.job_id) if JOB_MAP[self.job_id] else "Montaria"}\nMAP: {self.current_map}\nbuffs:{[BUFF_MAP.get(buff, buff).__str__()  for buff in self.buffs]}'
