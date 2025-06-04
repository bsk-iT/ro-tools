from game.buffs import Buff


class ASPDPotion(Buff):
    def __init__(self, buff_id, name, min_lvl, icon=None):
        super().__init__(buff_id, name, icon)
        self.min_lvl = min_lvl

    def __str__(self):
        return self.name


CONCENTRATION_POTION = ASPDPotion(645, "Poção da Concentração", 0)
AWAKENING_POTION = ASPDPotion(656, "Poção do Despertar", 40)
BERSERK_POTION = ASPDPotion(657, "Poção da Fúria", 85)
