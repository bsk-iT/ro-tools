from config.icon import PATH_ITEM, get_image


class Macro:
    def __init__(self, _id, name, icon):
        self.id = _id
        self.name = name
        self.icon = icon


ICON_ATK = get_image(PATH_ITEM, "NOVICE_KNIFE")
ICON_DEF = get_image(PATH_ITEM, "NOVICE_GUARD")
ICON_CLIP = get_image(PATH_ITEM, "CLIP")

ATK_1 = Macro("attack_1", "Equipes de Ataque 1", ICON_ATK)
ATK_2 = Macro("attack_2", "Equipes de Ataque 2", ICON_ATK)
ATK_3 = Macro("attack_3", "Equipes de Ataque 3", ICON_ATK)
ATK_4 = Macro("attack_4", "Equipes de Ataque 4", ICON_ATK)
DEF_1 = Macro("defense_1", "Equipes de Defesa 1", ICON_DEF)
DEF_2 = Macro("defense_2", "Equipes de Defesa 2", ICON_DEF)
DEF_3 = Macro("defense_3", "Equipes de Defesa 3", ICON_DEF)
DEF_4 = Macro("defense_4", "Equipes de Defesa 4", ICON_DEF)
SMOKIE = Macro("smokie", "Acessório c/ Fumacento", ICON_CLIP)
HORONG = Macro("horong", "Acessório c/ Horong", ICON_CLIP)

MACRO_TYPES = {
    "Ataque": [ATK_1, ATK_2, ATK_3, ATK_4],
    "Defesa": [DEF_1, DEF_2, DEF_3, DEF_4],
    "Outros": [SMOKIE, HORONG],
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
    "smokie": SMOKIE,
    "horong": HORONG,
}
