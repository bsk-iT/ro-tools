from service.memory import MEMORY
from service.offsets import Offsets


class Char:

    def current_map(self) -> str:
        try:
            return "prontera"
        except BaseException:
            return ""

    def hp(self) -> int:
        try:
            return MEMORY.process.read_int(MEMORY.hp_address + Offsets.HP)
        except BaseException:
            return 0

    def max_hp(self) -> int:
        try:
            return MEMORY.process.read_int(MEMORY.hp_address + Offsets.MAX_HP)
        except BaseException:
            return 0

    def sp(self) -> int:
        try:
            return MEMORY.process.read_int(MEMORY.hp_address + Offsets.SP)
        except BaseException:
            return 0

    def max_sp(self) -> int:
        try:
            return MEMORY.process.read_int(MEMORY.hp_address + Offsets.MAX_SP)
        except BaseException:
            return 0

    def hp_percent(self) -> int:
        max_hp = self.max_hp()
        if max_hp == 0:
            return 100
        return int(self.hp() * 100 / self.max_hp())

    def sp_percent(self) -> int:
        max_sp = self.max_sp()
        if max_sp == 0:
            return 100
        return int(self.sp() * 100 / self.max_sp())


CHAR = Char()
