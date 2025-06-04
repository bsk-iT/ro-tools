from game.buffs import Buff


class SkillAutoBuff(Buff):
    def __init__(self, buff_id, name, icon=None):
        super().__init__(buff_id, name, icon)
