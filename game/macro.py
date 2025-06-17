from config.icon import ICON_SHIELD, ICON_SWORD, PATH_ITEM, get_image


class Macro:
    def __init__(self, _id, name, icon):
        self.id = _id
        self.name = name
        self.icon = icon


MAX_HOTKEY = 10
ICON_CLIP = get_image(PATH_ITEM, "CLIP")

ATK_1 = Macro("attack_1", "Equipes de Ataque 1", ICON_SWORD)
ATK_2 = Macro("attack_2", "Equipes de Ataque 2", ICON_SWORD)
ATK_3 = Macro("attack_3", "Equipes de Ataque 3", ICON_SWORD)
ATK_4 = Macro("attack_4", "Equipes de Ataque 4", ICON_SWORD)
DEF_1 = Macro("defense_1", "Equipes de Defesa 1", ICON_SHIELD)
DEF_2 = Macro("defense_2", "Equipes de Defesa 2", ICON_SHIELD)
DEF_3 = Macro("defense_3", "Equipes de Defesa 3", ICON_SHIELD)
DEF_4 = Macro("defense_4", "Equipes de Defesa 4", ICON_SHIELD)
SMOKIE = Macro("smokie", "Acessório c/ Fumacento", ICON_CLIP)
HORONG = Macro("horong", "Acessório c/ Horong", ICON_CLIP)
JAGUAR_HAT = Macro("jaguar_hat", "Máscara de Onça-Pintada", get_image(PATH_ITEM, "JAGUAR_HAT"))

MACRO_TYPES = {
    "Ataque": [ATK_1, ATK_2, ATK_3, ATK_4],
    "Defesa": [DEF_1, DEF_2, DEF_3, DEF_4],
    "Outros": [JAGUAR_HAT, SMOKIE, HORONG],
}

MACRO_MAP = {
    "attack_1": ATK_1,
    "attack_2": ATK_2,
    "attack_3": ATK_3,
    "attack_4": ATK_4,
    "defense_1": DEF_1,
    "defense_2": DEF_2,
    "defense_3": DEF_3,
    "defense_4": DEF_4,
    "jaguar_hat": JAGUAR_HAT,
    "smokie": SMOKIE,
    "horong": HORONG,
}
