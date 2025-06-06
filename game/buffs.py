from config.icon import PATH_BUFF_ASPD, PATH_BUFF_ITEM, PATH_BUFF_SKILL, get_image


class Buff:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.icon = None

    def __str__(self):
        return self.name


class ASPD(Buff):
    def __init__(self, buff_id, name, min_lvl):
        super().__init__(buff_id, name)
        self.min_lvl = min_lvl
        self.icon = get_image(PATH_BUFF_ASPD, self.id)


class Item(Buff):
    def __init__(self, buff_id, name):
        super().__init__(buff_id, name)
        self.icon = get_image(PATH_BUFF_ITEM, self.id)


class Skill(Buff):
    def __init__(self, buff_id, name):
        super().__init__(buff_id, name)
        self.icon = get_image(PATH_BUFF_SKILL, self.id)


# ---- ASPD ----
CONCENTRATION_POTION = ASPD("CONCENTRATION_POTION", "Poção da Concentração", 0)
AWAKENING_POTION = ASPD("AWAKENING_POTION", "Poção do Despertar", 40)
BERSERK_POTION = ASPD("BERSERK_POTION", "Poção da Fúria", 85)

ASPD_BUFF_MAP = {
    "CONCENTRATION_POTION": CONCENTRATION_POTION,
    "AWAKENING_POTION": AWAKENING_POTION,
    "BERSERK_POTION": BERSERK_POTION,
}


# ----- Item -----
BLESS_SCROLL = Item("BLESS_SCROLL", "Scroll de Benção")
AGI_UP_SCROLL = Item("AGI_UP_SCROLL", "Scroll de Agilidade")

ITEM_BUFF_MAP = {
    "BLESS_SCROLL": BLESS_SCROLL,
    "AGI_UP_SCROLL": AGI_UP_SCROLL,
}


# ----- Skill -----

# Swordman
SM_MAGNUM = Skill("SM_MAGNUM", "Impacto Explosivo")
SM_ENDURE = Skill("SM_ENDURE", "Provocar")
SM_AUTOBERSERK = Skill("SM_AUTOBERSERK", "Instinto de Sobrevivência")

# Mage
MG_ENERGYCOAT = Skill("MG_ENERGYCOAT", "Proteção Arcana")

# Merchat
MC_LOUD = Skill("MC_LOUD", "Grito de Guerra")

# Acolyte
AL_ANGELUS = Skill("AL_ANGELUS", "Angelus")

# Archer
AC_CONCENTRATION = Skill("AC_CONCENTRATION", "Concentrar")

# Knight
KN_TWOHANDQUICKEN = Skill("KN_TWOHANDQUICKEN", "Rapidez com Duas Mãos")
KN_ONEHAND = Skill("KN_ONEHAND", "Rapidez com Uma Mão")

# Crusader
CR_AUTOGUARD = Skill("CR_AUTOGUARD", "Bloqueio")
CR_DEFENDER = Skill("CR_DEFENDER", "Aura Sagrada")
CR_SPEARQUICKEN = Skill("CR_SPEARQUICKEN", "Rapidez com Lança")
CR_REFLECTSHIELD = Skill("CR_REFLECTSHIELD", "Escudo Refletor")
CR_SHRINK = Skill("CR_SHRINK", "Escudo Refletor")

# Wizard
WZ_SIGHTBLASTER = Skill("WZ_SIGHTBLASTER", "Explosão Protetora")

# Sage
SA_AUTOSPELL = Skill("SA_AUTOSPELL", "Desejo Arcano")

# Assassin
AS_CLOAKING = Skill("AS_CLOAKING", "Furtividade")
AS_POISONREACT = Skill("AS_POISONREACT", "Refletir Veneno")

# Blacksmith
BS_ADRENALINE = Skill("BS_ADRENALINE", "Adrenalina Pura")
BS_MAXIMIZE = Skill("BS_MAXIMIZE", "Amplificar Poder")
BS_OVERTHRUST = Skill("BS_OVERTHRUST", "Força Violenta")
BS_WEAPONPERFECT = Skill("BS_WEAPONPERFECT", "Manejo Perfeito")
BS_ADRENALINE2 = Skill("BS_ADRENALINE2", "Adrenalina Concentrada")

# Alchemist
AM_RESURRECTHOMUN = Skill("AM_RESURRECTHOMUN", "Ressuscitar Homunculus")

# Monk
FURY = Skill("FURY", "Fúria Interior")


AUTO_BUFF_MAP = {
    "SM_MAGNUM": SM_MAGNUM,
    "SM_ENDURE": SM_ENDURE,
    "SM_AUTOBERSERK": SM_AUTOBERSERK,
    "MG_ENERGYCOAT": MG_ENERGYCOAT,
    "MC_LOUD": MC_LOUD,
    "AL_ANGELUS": AL_ANGELUS,
    "AC_CONCENTRATION": AC_CONCENTRATION,
    "KN_TWOHANDQUICKEN": KN_TWOHANDQUICKEN,
    "KN_ONEHAND": KN_ONEHAND,
    "CR_AUTOGUARD": CR_AUTOGUARD,
    "CR_DEFENDER": CR_DEFENDER,
    "CR_SPEARQUICKEN": CR_SPEARQUICKEN,
    "CR_REFLECTSHIELD": CR_REFLECTSHIELD,
    "CR_SHRINK": CR_SHRINK,
    "WZ_SIGHTBLASTER": WZ_SIGHTBLASTER,
    "SA_AUTOSPELL": SA_AUTOSPELL,
    "AS_CLOAKING": AS_CLOAKING,
    "AS_POISONREACT": AS_POISONREACT,
    "BS_ADRENALINE": BS_ADRENALINE,
    "BS_MAXIMIZE": BS_MAXIMIZE,
    "BS_OVERTHRUST": BS_OVERTHRUST,
    "BS_WEAPONPERFECT": BS_WEAPONPERFECT,
    "BS_ADRENALINE2": BS_ADRENALINE2,
    "AM_RESURRECTHOMUN": AM_RESURRECTHOMUN,
    "FURY": FURY,
}
