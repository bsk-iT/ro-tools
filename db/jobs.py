class Job:
    def __init__(
        self,
        job_id,
        job_name,
        previous_job=None,
        atk_skills=[],
        buff_skills=[],
        buff_items=[],
    ):
        self.job_id = job_id
        self.job_name = job_name
        self.previous_job = previous_job
        self.atk_skills = atk_skills
        self.buff_skills = buff_skills
        self.buff_items = buff_items


NOVICE = Job(0, "Aprendiz")
SWORDMAN = Job(1, "Espadachim", NOVICE)
MAGICIAN = Job(2, "Mago", NOVICE)
ARCHER = Job(3, "Arqueiro", NOVICE)
ACOLYTE = Job(4, "Noviço", NOVICE)
MERCHANT = Job(5, "Mercador", NOVICE)
THIEF = Job(6, "Gatuno", NOVICE)
KNIGHT = Job(7, "Cavaleiro", SWORDMAN)
PRIEST = Job(8, "Sacerdote", ACOLYTE)
WIZARD = Job(9, "Bruxo", MAGICIAN)
BLACKSMITH = Job(10, "Ferreiro", MERCHANT)
HUNTER = Job(11, "Caçador", ARCHER)
ASSASSIN = {
    "buff_skills": THIEF["buff_items"],
    "atk_skills": THIEF["atk_skills"],
    "buff_items": THIEF["buff_skills"],
}
KNIGHT_PECO = KNIGHT
CRUSADER = {
    "buff_skills": SWORDMAN["buff_items"],
    "atk_skills": SWORDMAN["atk_skills"],
    "buff_items": SWORDMAN["buff_skills"],
}
MONK = {
    "buff_skills": ACOLYTE["buff_items"],
    "atk_skills": ACOLYTE["atk_skills"],
    "buff_items": ACOLYTE["buff_skills"],
}
SAGE = {
    "buff_skills": MAGICIAN["buff_items"],
    "atk_skills": MAGICIAN["atk_skills"],
    "buff_items": MAGICIAN["buff_skills"],
}
ROGUE = {
    "buff_skills": THIEF["buff_items"],
    "atk_skills": THIEF["atk_skills"],
    "buff_items": THIEF["buff_skills"],
}
ALCHEMIST = {
    "buff_skills": MERCHANT["buff_items"],
    "atk_skills": MERCHANT["atk_skills"],
    "buff_items": MERCHANT["buff_skills"],
}
BARD = {
    "buff_skills": ARCHER["buff_items"],
    "atk_skills": ARCHER["atk_skills"],
    "buff_items": ARCHER["buff_skills"],
}
DANCER = {
    "buff_skills": ARCHER["buff_items"],
    "atk_skills": ARCHER["atk_skills"],
    "buff_items": ARCHER["buff_skills"],
}
CRUSADER_PECO = CRUSADER
SUPERNOVICE = {
    "buff_skills": NOVICE["buff_items"],
    "atk_skills": NOVICE["atk_skills"],
    "buff_items": NOVICE["buff_skills"],
}
GUNSLINGER = {
    "buff_skills": NOVICE["buff_items"],
    "atk_skills": NOVICE["atk_skills"],
    "buff_items": NOVICE["buff_skills"],
}
NINJA = {
    "buff_skills": NOVICE["buff_items"],
    "atk_skills": NOVICE["atk_skills"],
    "buff_items": NOVICE["buff_skills"],
}
LORD_KNIGHT = {
    "buff_skills": KNIGHT["buff_items"],
    "atk_skills": KNIGHT["atk_skills"],
    "buff_items": KNIGHT["buff_skills"],
}
HIGH_PRIEST = {
    "buff_skills": PRIEST["buff_items"],
    "atk_skills": PRIEST["atk_skills"],
    "buff_items": PRIEST["buff_skills"],
}
HIGH_WIZARD = {
    "buff_skills": WIZARD["buff_items"],
    "atk_skills": WIZARD["atk_skills"],
    "buff_items": WIZARD["buff_skills"],
}
WHITESMITH = {
    "buff_skills": BLACKSMITH["buff_items"],
    "atk_skills": BLACKSMITH["atk_skills"],
    "buff_items": BLACKSMITH["buff_skills"],
}
SNIPER = {
    "buff_skills": HUNTER["buff_items"],
    "atk_skills": HUNTER["atk_skills"],
    "buff_items": HUNTER["buff_skills"],
}
ASSASSIN_CROSS = {
    "buff_skills": ASSASSIN["buff_items"],
    "atk_skills": ASSASSIN["atk_skills"],
    "buff_items": ASSASSIN["buff_skills"],
}
LORD_KNIGHT_PECO = LORD_KNIGHT
PALADIN = {
    "buff_skills": CRUSADER["buff_items"],
    "atk_skills": CRUSADER["atk_skills"],
    "buff_items": CRUSADER["buff_skills"],
}
CHAMPION = {
    "buff_skills": MONK["buff_items"],
    "atk_skills": MONK["atk_skills"],
    "buff_items": MONK["buff_skills"],
}
SCHOLAR = {
    "buff_skills": SAGE["buff_items"],
    "atk_skills": SAGE["atk_skills"],
    "buff_items": SAGE["buff_skills"],
}
STALKER = {
    "buff_skills": ROGUE["buff_items"],
    "atk_skills": ROGUE["atk_skills"],
    "buff_items": ROGUE["buff_skills"],
}
BIOCHEMIST = {
    "buff_skills": ALCHEMIST["buff_items"],
    "atk_skills": ALCHEMIST["atk_skills"],
    "buff_items": ALCHEMIST["buff_skills"],
}
MINSTREL = {
    "buff_skills": BARD["buff_items"],
    "atk_skills": BARD["atk_skills"],
    "buff_items": BARD["buff_skills"],
}
GYPSY = {
    "buff_skills": DANCER["buff_items"],
    "atk_skills": DANCER["atk_skills"],
    "buff_items": DANCER["buff_skills"],
}
PALADIN_PECO = PALADIN
RUNE_KNIGHT = {
    "buff_skills": LORD_KNIGHT["buff_items"],
    "atk_skills": LORD_KNIGHT["atk_skills"],
    "buff_items": LORD_KNIGHT["buff_skills"],
}
WARLOCK = {
    "buff_skills": HIGH_WIZARD["buff_items"],
    "atk_skills": HIGH_WIZARD["atk_skills"],
    "buff_items": HIGH_WIZARD["buff_skills"],
}
RANGER = {
    "buff_skills": SNIPER["buff_items"],
    "atk_skills": SNIPER["atk_skills"],
    "buff_items": SNIPER["buff_skills"],
}
ARCH_BISHOP = {
    "buff_skills": HIGH_PRIEST["buff_items"],
    "atk_skills": HIGH_PRIEST["atk_skills"],
    "buff_items": HIGH_PRIEST["buff_skills"],
}
MECHANIC = {
    "buff_skills": WHITESMITH["buff_items"],
    "atk_skills": WHITESMITH["atk_skills"],
    "buff_items": WHITESMITH["buff_skills"],
}
GUILLOTINE_CROSS = {
    "buff_skills": ASSASSIN_CROSS["buff_items"],
    "atk_skills": ASSASSIN_CROSS["atk_skills"],
    "buff_items": ASSASSIN_CROSS["buff_skills"],
}
ROYAL_GUARD = {
    "buff_skills": PALADIN["buff_items"],
    "atk_skills": PALADIN["atk_skills"],
    "buff_items": PALADIN["buff_skills"],
}
SORCERER = {
    "buff_skills": SCHOLAR["buff_items"],
    "atk_skills": SCHOLAR["atk_skills"],
    "buff_items": SCHOLAR["buff_skills"],
}
MAESTRO = {
    "buff_skills": MINSTREL["buff_items"],
    "atk_skills": MINSTREL["atk_skills"],
    "buff_items": MINSTREL["buff_skills"],
}
WANDERER = {
    "buff_skills": GYPSY["buff_items"],
    "atk_skills": GYPSY["atk_skills"],
    "buff_items": GYPSY["buff_skills"],
}
SURA = {
    "buff_skills": CHAMPION["buff_items"],
    "atk_skills": CHAMPION["atk_skills"],
    "buff_items": CHAMPION["buff_skills"],
}
GENETIC = {
    "buff_skills": BIOCHEMIST["buff_items"],
    "atk_skills": BIOCHEMIST["atk_skills"],
    "buff_items": BIOCHEMIST["buff_skills"],
}
SHADOW_CHASER = {
    "buff_skills": STALKER["buff_items"],
    "atk_skills": STALKER["atk_skills"],
    "buff_items": STALKER["buff_skills"],
}
RUNE_KNIGHT_PECO = RUNE_KNIGHT
ROYAL_GUARD_PECO = ROYAL_GUARD
RANGER_WOLF = RANGER
MECHANIC_GEAR = MECHANIC
RUNE_KNIGHT_PECO_2 = RUNE_KNIGHT
RUNE_KNIGHT_PECO_3 = RUNE_KNIGHT
RUNE_KNIGHT_PECO_4 = RUNE_KNIGHT
RUNE_KNIGHT_PECO_5 = RUNE_KNIGHT
MOUNT = None

CLASSES = {
    0: NOVICE,
    4001: NOVICE,
    1: SWORDMAN,
    4002: SWORDMAN,
    2: MAGICIAN,
    4003: SWORDMAN,
    3: ARCHER,
    4004: ARCHER,
    4: ACOLYTE,
    4005: ACOLYTE,
    5: MERCHANT,
    4006: MERCHANT,
    6: THIEF,
    4007: THIEF,
    7: KNIGHT,
    4008: LORD_KNIGHT,
    4060: RUNE_KNIGHT,
    8: PRIEST,
    4009: HIGH_PRIEST,
    4063: ARCH_BISHOP,
    9: WIZARD,
    4010: HIGH_WIZARD,
    4061: WARLOCK,
    10: BLACKSMITH,
    4011: WHITESMITH,
    4064: MECHANIC,
    4087: MECHANIC_GEAR,
    11: HUNTER,
    4012: SNIPER,
    4062: RANGER,
    4085: RANGER_WOLF,
    12: ASSASSIN,
    4013: ASSASSIN_CROSS,
    4065: GUILLOTINE_CROSS,
    13: KNIGHT_PECO,
    4014: LORD_KNIGHT_PECO,
    4081: RUNE_KNIGHT_PECO,
    4089: RUNE_KNIGHT_PECO_2,
    4091: RUNE_KNIGHT_PECO_3,
    4093: RUNE_KNIGHT_PECO_4,
    4095: RUNE_KNIGHT_PECO_5,
    14: CRUSADER,
    4015: PALADIN,
    4073: ROYAL_GUARD,
    15: MONK,
    4016: CHAMPION,
    4077: SURA,
    16: SAGE,
    4017: SCHOLAR,
    4074: SORCERER,
    17: ROGUE,
    4018: STALKER,
    4079: SHADOW_CHASER,
    18: ALCHEMIST,
    4019: BIOCHEMIST,
    4078: GENETIC,
    19: BARD,
    4020: MINSTREL,
    4075: MAESTRO,
    20: DANCER,
    4021: GYPSY,
    4076: WANDERER,
    21: CRUSADER_PECO,
    4022: PALADIN_PECO,
    4083: ROYAL_GUARD_PECO,
    23: SUPERNOVICE,
    24: GUNSLINGER,
    25: NINJA,
    4136: MOUNT,
    4154: MOUNT,
    4157: MOUNT,
    4164: MOUNT,
    4183: MOUNT,
    4184: MOUNT,
    4185: MOUNT,
    4186: MOUNT,
    4187: MOUNT,
    4188: MOUNT,
    4189: MOUNT,
    4200: MOUNT,
    4204: MOUNT,
}
