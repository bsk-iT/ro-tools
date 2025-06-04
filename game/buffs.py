class Buff:
    def __init__(self, buff_id, name, icon=None):
        self.buff_id = buff_id
        self.name = name
        self.icon = icon

    def __str__(self):
        return self.name


# Acolyte
BLESS = Buff(10, "Benção")
AGI_UP = Buff(12, "Agilidade")

# Monk
FURY = Buff(86, "Fúria Interior")

# LegionBR - Buffs Icon
ROTD_INSETO = Buff(1506, "ROTD Inseto")
RATE = Buff(1524, "Rate LegionBR")


BUFF_MAP = {10: BLESS, 12: AGI_UP, 86: FURY, 1506: ROTD_INSETO, 1524: RATE}
