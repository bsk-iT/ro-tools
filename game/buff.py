from config.icon import PATH_BUFF_SKILL, PATH_ITEM, get_image


class Buff:
    def __init__(self, id, name, priority=0):
        self.id = id
        self.name = name
        self.icon = None
        self.priority = priority

    def __str__(self):
        return self.name


class Item(Buff):
    def __init__(self, buff_id, name, priority=0):
        super().__init__(buff_id, name, priority)
        self.icon = get_image(PATH_ITEM, self.id)


class Skill(Buff):
    def __init__(self, buff_id, name, priority=0):
        super().__init__(buff_id, name, priority)
        self.icon = get_image(PATH_BUFF_SKILL, self.id)


class Debuff(Buff):
    def __init__(self, buff_id, name, recover_status, priority=0):
        super().__init__(buff_id, name, priority)
        self.icon = get_image(PATH_ITEM, self.id)
        self.recover_status = recover_status


# ----- Item -----
BLESS_SCROLL = Item("bless_scroll", "Scroll de Benção")
INC_AGI_UP_SCROLL = Item("inc_agi_up_scroll", "Scroll de Aumentar Agilidade")
CONCENTRATION_POTION = Item("concentration_potion", "Poção da Concentração")
AWAKENING_POTION = Item("awakening_potion", "Poção do Despertar")
BERSERK_POTION = Item("berserk_potion", "Poção da Fúria")
RESENTMENT_BOX = Item("resentment_box", "Caixa do Ressentimento")
THUNDER_BOX = Item("thunder_box", "Caixa do Trovão")
ALOE_VERA = Item("aloe_vera", "Aloe Vera")
PAIN_KILLER = Item("pain_killer", "Analgésico")

ITEM_BUFF_MAP = {
    "bless_scroll": BLESS_SCROLL,
    "inc_agi_up_scroll": INC_AGI_UP_SCROLL,
    "concentration_potion": CONCENTRATION_POTION,
    "awakening_potion": AWAKENING_POTION,
    "berserk_potion": BERSERK_POTION,
    "resentment_box": RESENTMENT_BOX,
    "thunder_box": THUNDER_BOX,
    "aloe_vera": ALOE_VERA,
    "pain_killer": PAIN_KILLER,
}

ITEM_BUFF_GROUP = {
    "APSD Potion": [CONCENTRATION_POTION, AWAKENING_POTION, BERSERK_POTION],
    "Caixas": [RESENTMENT_BOX, THUNDER_BOX],
    "Consumíveis": [ALOE_VERA, PAIN_KILLER],
    "Buff - Scrolls": [BLESS_SCROLL, INC_AGI_UP_SCROLL],
}

# ----- Item cura debuff -----
BLIND = "blind"
CONFUSION = "confusion"
CURSE = "curse"
POISON = "poison"
SILENCE = "silence"
HALLUCINATION = "hallucination"
HALLUCINATION_WALK = "hallucination_walk"
SILENCE = "silence"

PANACEA = Debuff("panacea", "Panacea", [BLIND, CONFUSION, CURSE, POISON, SILENCE, HALLUCINATION, HALLUCINATION_WALK])
GREEN_POTION = Debuff("green_potion", "Poção Verde", [BLIND, CONFUSION, POISON, SILENCE], 1)
GREEN_HERB = Debuff("green_herb", "Erva Verde", [POISON], 2)

ITEM_DEBUFF_GROUP = {
    "Básico": [PANACEA, GREEN_POTION, GREEN_HERB],
}

ITEM_DEBUFF_MAP = {
    "panacea": PANACEA,
    "green_potion": GREEN_POTION,
    "green_herb": GREEN_HERB,
}

# ----- Skill -----

# Swordman
SM_MAGNUM = Skill("sm_magnum", "Impacto Explosivo")
SM_ENDURE = Skill("sm_endure", "Vigor", 1)
SM_AUTOBERSERK = Skill("sm_autoberserk", "Instinto de Sobrevivência")

# Mage
MG_ENERGYCOAT = Skill("mg_energycoat", "Proteção Arcana")

# Merchat
MC_LOUD = Skill("mc_loud", "Grito de Guerra", 5)

# Acolyte
AL_ANGELUS = Skill("al_angelus", "Angelus")

# Archer
AC_CONCENTRATION = Skill("ac_concentration", "Concentrar", 5)

# Knight
KN_TWOHANDQUICKEN = Skill("kn_twohandquicken", "Rapidez com Duas Mãos")
KN_ONEHAND = Skill("kn_onehand", "Rapidez com Uma Mão")

# Crusader
CR_AUTOGUARD = Skill("cr_autoguard", "Bloqueio")
CR_DEFENDER = Skill("cr_defender", "Aura Sagrada")
CR_SPEARQUICKEN = Skill("cr_spearquicken", "Rapidez com Lança")
CR_REFLECTSHIELD = Skill("cr_reflectshield", "Escudo Refletor")
CR_SHRINK = Skill("cr_shrink", "Escudo Refletor")

# Wizard
WZ_SIGHTBLASTER = Skill("wz_sightblaster", "Explosão Protetora")

# Sage
SA_AUTOSPELL = Skill("sa_autospell", "Desejo Arcano")

# Assassin
AS_CLOAKING = Skill("as_cloaking", "Furtividade")
AS_POISONREACT = Skill("as_poisonreact", "Refletir Veneno")

# Blacksmith
BS_ADRENALINE = Skill("bs_adrenaline", "Adrenalina Pura")
BS_MAXIMIZE = Skill("bs_maximize", "Amplificar Poder")
BS_OVERTHRUST = Skill("bs_overthrust", "Força Violenta")
BS_WEAPONPERFECT = Skill("bs_weaponperfect", "Manejo Perfeito")
BS_ADRENALINE2 = Skill("bs_adrenaline2", "Adrenalina Concentrada")

# Alchemist
AM_RESURRECTHOMUN = Skill("am_resurrecthomun", "Ressuscitar Homunculus")

# Priest
PR_GLORIA = Skill("pr_gloria", "Glória")
PR_MAGNIFICAT = Skill("pr_magnificat", "Magnificat")
PR_IMPOSITIO = Skill("pr_impositio", "Impositio Manus")
PR_SUFFRAGIUM = Skill("pr_suffragium", "Suffragium")

# Monk
MO_EXPLOSIONSPIRITS = Skill("mo_explosionspirits", "Fúria Interior")

# Bard
BD_ADAPTATION = Skill("bd_adaptation", "Aquecimento")

# Lord
LK_AURABLADE = Skill("lk_aurablade", "Lâmina de Aura")
LK_PARRYING = Skill("lk_parrying", "Aparar Golpe")
LK_CONCENTRATION = Skill("lk_concentration", "Dedicação")

# High Wizard
HW_MAGICPOWER = Skill("hw_magicpower", "Amplificação Mística")

# Professor
PF_DOUBLECASTING = Skill("pf_doublecasting", "Lanças Duplas")
PF_MEMORIZE = Skill("pf_memorize", "Presciência")

# Assassin Cross
ASC_EDP = Skill("asc_edp", "Encantar com Veneno Mortal")

# Stalker
ST_REJECTSWORD = Skill("st_rejectsword", "Instinto de Defesa")
ST_PRESERVE = Skill("st_preserve", "Preservar")

# Whiesmith
WS_CARTBOOST = Skill("ws_cartboost", "Impulso no Carrinho")
WS_MELTDOWN = Skill("ws_meltdown", "Golpe Estilhaçante")
WS_OVERTHRUSTMAX = Skill("ws_overthrustmax", "Força Violentíssima")

# High Priest
HP_BASILICA = Skill("hp_basilica", "Basílica")

# Sniper
SN_SIGHT = Skill("sn_sight", "Visão Real", 4)
SN_WINDWALK = Skill("sn_windwalk", "Caminho do Vento")

# Taekwon
TK_READYSTORM = Skill("tk_readystorm", "Postura do Tornado")
TK_READYDOWN = Skill("tk_readydown", "Postura da Patada Voadora")
TK_READYTURN = Skill("tk_readyturn", "Postura da Rasteira")
TK_READYCOUNTER = Skill("tk_readycounter", "Postura do Contrachute")
TK_DODGE = Skill("tk_dodge", "Cambalhota")
TK_SEVENWIND_EARTH = Skill("tk_sevenwind_earth", "Brisa Leve - Terra")
TK_SEVENWIND_WIND = Skill("tk_sevenwind_earth", "Brisa Leve - Vento")
TK_SEVENWIND_WATER = Skill("tk_sevenwind_earth", "Brisa Leve - Água")
TK_SEVENWIND_FIRE = Skill("tk_sevenwind_earth", "Brisa Leve - Fogo")
TK_SEVENWIND_GHOST = Skill("tk_sevenwind_earth", "Brisa Leve - Fantasma")
TK_SEVENWIND_DARK = Skill("tk_sevenwind_earth", "Brisa Leve - Sombrio")
TK_SEVENWIND_HOLY = Skill("tk_sevenwind_earth", "Brisa Leve - Sagrado")

# Gunslinger
GS_GATLINGFEVER = Skill("gs_gatlingfever", "Ataque Gatling")
GS_ADJUSTMENT = Skill("gs_adjustment", "Pânico do Justiceiro")
GS_INCREASING = Skill("gs_increasing", "Aumentar Precisão")
GS_MAGICALBULLET = Skill("gs_magicalbullet", "Bala Mágica")

# Ninja
NJ_UTSUSEMI = Skill("nj_utsusemi", "Troca de Pele")
NJ_BUNSINJYUTSU = Skill("nj_bunsinjyutsu", "Imagem Falsa")
NJ_NEN = Skill("nj_nen", "Aura Ninja")

EQUIP_BUFFS = [MC_LOUD]

AUTO_BUFF_MAP = {
    "sm_magnum": SM_MAGNUM,
    "sm_endure": SM_ENDURE,
    "sm_autoberserk": SM_AUTOBERSERK,
    "mg_energycoat": MG_ENERGYCOAT,
    "mc_loud": MC_LOUD,
    "al_angelus": AL_ANGELUS,
    "ac_concentration": AC_CONCENTRATION,
    "kn_twohandquicken": KN_TWOHANDQUICKEN,
    "kn_onehand": KN_ONEHAND,
    "cr_autoguard": CR_AUTOGUARD,
    "cr_defender": CR_DEFENDER,
    "cr_spearquicken": CR_SPEARQUICKEN,
    "cr_reflectshield": CR_REFLECTSHIELD,
    "cr_shrink": CR_SHRINK,
    "wz_sightblaster": WZ_SIGHTBLASTER,
    "sa_autospell": SA_AUTOSPELL,
    "as_cloaking": AS_CLOAKING,
    "as_poisonreact": AS_POISONREACT,
    "bs_adrenaline": BS_ADRENALINE,
    "bs_maximize": BS_MAXIMIZE,
    "bs_overthrust": BS_OVERTHRUST,
    "bs_weaponperfect": BS_WEAPONPERFECT,
    "bs_adrenaline2": BS_ADRENALINE2,
    "am_resurrecthomun": AM_RESURRECTHOMUN,
    "pr_gloria": PR_GLORIA,
    "pr_magnificat": PR_MAGNIFICAT,
    "pr_impositio": PR_IMPOSITIO,
    "pr_suffragium": PR_SUFFRAGIUM,
    "mo_explosionspirits": MO_EXPLOSIONSPIRITS,
    "bd_adaptation": BD_ADAPTATION,
    "lk_aurablade": LK_AURABLADE,
    "lk_parrying": LK_PARRYING,
    "lk_concentration": LK_CONCENTRATION,
    "hw_magicpower": HW_MAGICPOWER,
    "pf_doublecasting": PF_DOUBLECASTING,
    "pf_memorize": PF_MEMORIZE,
    "asc_edp": ASC_EDP,
    "st_rejectsword": ST_REJECTSWORD,
    "st_preserve": ST_PRESERVE,
    "ws_cartboost": WS_CARTBOOST,
    "ws_meltdown": WS_MELTDOWN,
    "ws_overthrustmax": WS_OVERTHRUSTMAX,
    "hp_basilica": HP_BASILICA,
    "sn_sight": SN_SIGHT,
    "sn_windwalk": SN_WINDWALK,
    "tk_readystorm": TK_READYSTORM,
    "tk_readydown": TK_READYDOWN,
    "tk_readyturn": TK_READYTURN,
    "tk_readycounter": TK_READYCOUNTER,
    "tk_dodge": TK_DODGE,
    "tk_sevenwind_earth": TK_SEVENWIND_EARTH,
    "tk_sevenwind_wind": TK_SEVENWIND_WIND,
    "tk_sevenwind_water": TK_SEVENWIND_WATER,
    "tk_sevenwind_fire": TK_SEVENWIND_FIRE,
    "tk_sevenwind_ghost": TK_SEVENWIND_GHOST,
    "tk_sevenwind_dark": TK_SEVENWIND_DARK,
    "tk_sevenwind_holy": TK_SEVENWIND_HOLY,
    "gs_gatlingfever": GS_GATLINGFEVER,
    "gs_adjustment": GS_ADJUSTMENT,
    "gs_increasing": GS_INCREASING,
    "gs_magicalbullet": GS_MAGICALBULLET,
    "nj_utsusemi": NJ_UTSUSEMI,
    "nj_bunsinjyutsu": NJ_BUNSINJYUTSU,
    "nj_nen": NJ_NEN,
}
