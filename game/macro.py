from config.icon import ICON_CHAT, ICON_SHIELD, ICON_SONG, ICON_SWORD, PATH_ITEM, PATH_SPAWN_SKILL, get_image


class Macro:
    def __init__(self, _id, name, icon):
        self.id = _id
        self.name = name
        self.icon = icon


MAX_HOTKEY = 15
ICON_CLIP = get_image(PATH_ITEM, "clip")
ICON_FIRE = get_image(PATH_ITEM, "fire_enchant_scroll")
ICON_WATER = get_image(PATH_ITEM, "water_enchant_scroll")
ICON_GROUND = get_image(PATH_ITEM, "ground_enchant_scroll")
ICON_WIND = get_image(PATH_ITEM, "wind_enchant_scroll")
ICON_HOLY = get_image(PATH_ITEM, "holy_water")
ICON_DARK = get_image(PATH_ITEM, "dark_water")
ICON_GHOST = get_image(PATH_ITEM, "ghost_enchant_scroll")

ATK_1 = Macro("attack_1", "Equipes de Ataque 1", ICON_SWORD)
ATK_2 = Macro("attack_2", "Equipes de Ataque 2", ICON_SWORD)
ATK_3 = Macro("attack_3", "Equipes de Ataque 3", ICON_SWORD)
ATK_4 = Macro("attack_4", "Equipes de Ataque 4", ICON_SWORD)
ELEMENT_FIRE = Macro("element_fire", "Equipes (Fogo)", ICON_FIRE)
ELEMENT_WATER = Macro("element_water", "Equipes (Água)", ICON_WATER)
ELEMENT_GROUND = Macro("element_ground", "Equipes (Terra)", ICON_GROUND)
ELEMENT_WIND = Macro("element_wind", "Equipes (Vento)", ICON_WIND)
ELEMENT_HOLY = Macro("element_holy", "Equipes (Sagrado)", ICON_HOLY)
ELEMENT_DARK = Macro("element_dark", "Equipes (Sombrio)", ICON_DARK)
ELEMENT_GHOST = Macro("element_ghost", "Equipes (Fantasma)", ICON_GHOST)

DEF_1 = Macro("defense_1", "Equipes de Defesa 1", ICON_SHIELD)
DEF_2 = Macro("defense_2", "Equipes de Defesa 2", ICON_SHIELD)
DEF_3 = Macro("defense_3", "Equipes de Defesa 3", ICON_SHIELD)
DEF_4 = Macro("defense_4", "Equipes de Defesa 4", ICON_SHIELD)

SONG_1 = Macro("song_1", "Playlist 1", ICON_SONG)
SONG_2 = Macro("song_2", "Playlist 2", ICON_SONG)
SONG_3 = Macro("song_3", "Playlist 3", ICON_SONG)
SONG_4 = Macro("song_4", "Playlist 4", ICON_SONG)

AM_PHARMACY = Macro("am_pharmacy", "Preparar Poção", get_image(PATH_SPAWN_SKILL, "am_pharmacy"))
WS_WEAPONREFINE = Macro("ws_weaponrefine", "Aprimorar Armamento", get_image(PATH_SPAWN_SKILL, "ws_weaponrefine"))

CHAT = Macro("chat", "NPC Conversa", ICON_CHAT)
SMOKIE = Macro("smokie", "Acessório c/ Fumacento", ICON_CLIP)
HORONG = Macro("horong", "Acessório c/ Horong", ICON_CLIP)
JAGUAR_HAT = Macro("jaguar_hat", "Máscara de Onça-Pintada", get_image(PATH_ITEM, "jaguar_hat"))

MACRO_ELEMENTS = [ELEMENT_FIRE, ELEMENT_WATER, ELEMENT_GROUND, ELEMENT_WIND, ELEMENT_HOLY, ELEMENT_DARK, ELEMENT_GHOST]

MACRO_TYPES = {
    "Ataque": [ATK_1, ATK_2, ATK_3, ATK_4],
    "Elementos": MACRO_ELEMENTS,
    "Defesa": [DEF_1, DEF_2, DEF_3, DEF_4],
    "Songs Clown | Gypsy": [SONG_1, SONG_2, SONG_3, SONG_4],
    "Craft": [AM_PHARMACY, WS_WEAPONREFINE],
    "Outros": [CHAT, JAGUAR_HAT, SMOKIE, HORONG],
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
    "element_fire": ELEMENT_FIRE,
    "element_water": ELEMENT_WATER,
    "element_ground": ELEMENT_GROUND,
    "element_wind": ELEMENT_WIND,
    "element_holy": ELEMENT_HOLY,
    "element_dark": ELEMENT_DARK,
    "element_ghost": ELEMENT_GHOST,
    "song_1": SONG_1,
    "song_2": SONG_2,
    "song_3": SONG_3,
    "song_4": SONG_4,
    "am_pharmacy": AM_PHARMACY,
    "ws_weaponrefine": WS_WEAPONREFINE,
    "jaguar_hat": JAGUAR_HAT,
    "smokie": SMOKIE,
    "horong": HORONG,
    "chat": CHAT
}
