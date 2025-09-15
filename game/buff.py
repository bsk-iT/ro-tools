from config.icon import PATH_BUFF_SKILL, PATH_ITEM, get_image


class Buff:
    def __init__(self, id, name, priority=0, block_quagmire=False, buff_timer=0):
        self.id = id
        self.name = name
        self.icon = None
        self.priority = priority
        self.block_quagmire = block_quagmire
        self.buff_timer = buff_timer

    def __str__(self):
        return self.name


class Item(Buff):
    def __init__(self, buff_id, name, priority=0, block_quagmire=False, buff_timer=0):
        super().__init__(buff_id, name, priority, block_quagmire, buff_timer)
        self.icon = get_image(PATH_ITEM, self.id)


class Skill(Buff):
    def __init__(self, buff_id, name, priority=0, block_quagmire=False, buff_timer=0):
        super().__init__(buff_id, name, priority, block_quagmire, buff_timer)
        self.icon = get_image(PATH_BUFF_SKILL, self.id)


class Debuff(Buff):
    def __init__(self, buff_id, name, recover_status, priority=0, block_quagmire=False, buff_timer=0):
        super().__init__(buff_id, name, priority, block_quagmire, buff_timer)
        self.icon = get_image(PATH_ITEM, self.id)
        self.recover_status = recover_status


# ----- Item -----
BLESS_SCROLL = Item("bless_scroll", "Scroll de Benção")
INC_AGI_UP_SCROLL = Item("inc_agi_up_scroll", "Scroll de Aumentar Agilidade", 0, True)
CONCENTRATION_POTION = Item("concentration_potion", "Poção da Concentração")
AWAKENING_POTION = Item("awakening_potion", "Poção do Despertar")
BERSERK_POTION = Item("berserk_potion", "Poção da Fúria")
RESENTMENT_BOX = Item("resentment_box", "Caixa do Ressentimento")
THUNDER_BOX = Item("thunder_box", "Caixa do Trovão")
DROWSINESS_BOX = Item("drowsiness_box", "Caixa da Sonolência")
GLOOM_BOX = Item("gloom_box", "Caixa da Escuridão", 0, True)
SUNLIGHT_BOX = Item("sunlight_box", "Caixa da Luz do Sol")
ALOE_VERA = Item("aloe_vera", "Aloe Vera")
PAIN_KILLER = Item("pain_killer", "Analgésico")
ASPERSION_SCROLL = Item("aspersion", "Aspersion")
SPEED_POTION = Item("speed_potion", "Poção do Vento")
FIRE_ENCHANT_SCROLL = Item("fire_enchant_scroll", "Conversor Elemental Fogo")
WATER_ENCHANT_SCROLL = Item("water_enchant_scroll", "Conversor Elemental Água")
GROUND_ENCHANT_SCROLL = Item("ground_enchant_scroll", "Conversor Elemental Terra")
WIND_ENCHANT_SCROLL = Item("wind_enchant_scroll", "Conversor Elemental Vento")
DARK_WATER = Item("dark_water", "Água Amaldiçoada")
ABRASIVE = Item("abrasive", "Abrasivo")
RESIST_PROPERTY_WATER = Item("resist_property_water", "Poção Anti-Água")
RESIST_PROPERTY_GROUND = Item("resist_property_ground", "Poção Anti-Terra")
RESIST_PROPERTY_FIRE = Item("resist_property_fire", "Poção Anti-Fogo")
RESIST_PROPERTY_WIND = Item("resist_property_wind", "Poção Anti-Vento")
STR_FOOD = Item("str_food", "STR Food")
AGI_FOOD = Item("agi_food", "AGI Food")
VIT_FOOD = Item("vit_food", "VIT Food")
INT_FOOD = Item("int_food", "INT Food")
DEX_FOOD = Item("dex_food", "DEX Food")
LUK_FOOD = Item("luk_food", "LUK Food")
HALTER_LEAD = Item("halter_lead", "Rédeas")
ITEM_1 = Item("item_1", "Item 1")
ITEM_2 = Item("item_2", "Item 2")
ITEM_3 = Item("item_3", "Item 3")
ITEM_4 = Item("item_4", "Item 4")

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
    "aspersion": ASPERSION_SCROLL,
    "speed_potion": SPEED_POTION,
    "fire_enchant_scroll": FIRE_ENCHANT_SCROLL,
    "water_enchant_scroll": WATER_ENCHANT_SCROLL,
    "wind_enchant_scroll": WIND_ENCHANT_SCROLL,
    "ground_enchant_scroll": GROUND_ENCHANT_SCROLL,
    "dark_water": DARK_WATER,
    "drowsiness_box": DROWSINESS_BOX,
    "gloom_box": GLOOM_BOX,
    "sunlight_box": SUNLIGHT_BOX,
    "abrasive": ABRASIVE,
    "resist_property_water": RESIST_PROPERTY_WATER,
    "resist_property_ground": RESIST_PROPERTY_GROUND,
    "resist_property_fire": RESIST_PROPERTY_FIRE,
    "resist_property_wind": RESIST_PROPERTY_WIND,
    "str_food": STR_FOOD,
    "agi_food": AGI_FOOD,
    "vit_food": VIT_FOOD,
    "int_food": INT_FOOD,
    "dex_food": DEX_FOOD,
    "luk_food": LUK_FOOD,
    "halter_lead": HALTER_LEAD,
    "item_1": ITEM_1,
    "item_2": ITEM_2,
    "item_3": ITEM_3,
    "item_4": ITEM_4
}

ITEM_BUFF_GROUP = {
    "APSD Potion": [CONCENTRATION_POTION, AWAKENING_POTION, BERSERK_POTION],
    "Caixas": [RESENTMENT_BOX, THUNDER_BOX, DROWSINESS_BOX, GLOOM_BOX, SUNLIGHT_BOX],
    "Consumíveis": [ALOE_VERA, PAIN_KILLER, SPEED_POTION, ABRASIVE],
    "Scrolls": [BLESS_SCROLL, INC_AGI_UP_SCROLL],
    "Elemento - Arma": [FIRE_ENCHANT_SCROLL, WATER_ENCHANT_SCROLL, WIND_ENCHANT_SCROLL, GROUND_ENCHANT_SCROLL, DARK_WATER],
    "Elemento - Resistência": [RESIST_PROPERTY_WATER, RESIST_PROPERTY_GROUND, RESIST_PROPERTY_FIRE, RESIST_PROPERTY_WIND],
    "Comidas": [STR_FOOD, AGI_FOOD, VIT_FOOD, INT_FOOD, DEX_FOOD, LUK_FOOD],
    "Outros": [ITEM_1, ITEM_2, ITEM_3, ITEM_4]
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
QUAGMIRE = "quagmire"

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
AC_CONCENTRATION = Skill("ac_concentration", "Concentrar", 5, True)

# Knight
KN_TWOHANDQUICKEN = Skill("kn_twohandquicken", "Rapidez com Duas Mãos", 0, True)
KN_ONEHAND = Skill("kn_onehand", "Rapidez com Uma Mão", 0, True)

# Crusader
CR_AUTOGUARD = Skill("cr_autoguard", "Bloqueio")
CR_DEFENDER = Skill("cr_defender", "Aura Sagrada")
CR_SPEARQUICKEN = Skill("cr_spearquicken", "Rapidez com Lança", 0, True)
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
BS_ADRENALINE = Skill("bs_adrenaline", "Adrenalina Pura", 0, True)
BS_MAXIMIZE = Skill("bs_maximize", "Amplificar Poder")
BS_OVERTHRUST = Skill("bs_overthrust", "Força Violenta")
BS_WEAPONPERFECT = Skill("bs_weaponperfect", "Manejo Perfeito")
BS_ADRENALINE2 = Skill("bs_adrenaline2", "Adrenalina Concentrada", 0, True)

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
BA_POEMBRAGI = Skill("ba_poembragi", "Poema de Bragi", buff_timer=180)
BA_ASSASSINCROSS = Skill("ba_assassincross", "Crepúsculo Sangrento", buff_timer=180)
BA_APPLEIDUN = Skill("ba_appleidun", "Maçãs de Idun", buff_timer=180)
BA_WHISTLE = Skill("ba_whistle", "Assovio", buff_timer=180)

# Dancer
DC_DONTFORGETME = Skill("dc_dontforgetme", "Não me Abandones", buff_timer=60)
DC_SERVICEFORYOU = Skill("dc_serviceforyou", "Dança Cigana", buff_timer=180)
DC_FORTUNEKISS = Skill("dc_fortunekiss", "Beijo da Sorte", buff_timer=180)
DC_HUMMING = Skill("dc_humming", "Sibilo", buff_timer=180)

# Duet
BD_ADAPTATION = Skill("bd_adaptation", "Aquecimento")
BD_SIEGFRIED = Skill("bd_siegfried", "Ode a Siegfried - Dueto", buff_timer=180)
BD_RICHMANKIM = Skill("bd_richmankim", "Banquete de Njord - Dueto", buff_timer=180)
BD_DRUMBATTLEFIELD = Skill("bd_drumbattlefield", "Rufar dos Tambores - Dueto", buff_timer=180)
BD_RINGNIBELUNGEN = Skill("bd_ringnibelungen", "Anel dos Nibelungos - Dueto", buff_timer=60)
BD_ETERNALCHAOS = Skill("bd_eternalchaos", "Ritmo Caótico - Dueto", buff_timer=60)
BD_ROKISWEIL = Skill("bd_rokisweil", "Lamento de Loki - Dueto", buff_timer=60)
BD_INTOABYSS = Skill("bd_intoabyss", "Canção Preciosa - Dueto", buff_timer=180)
BD_LULLABY = Skill("bd_lullaby", "Cantiga de Ninar - Dueto")

# Lord
LK_AURABLADE = Skill("lk_aurablade", "Lâmina de Aura")
LK_PARRYING = Skill("lk_parrying", "Aparar Golpe")
LK_CONCENTRATION = Skill("lk_concentration", "Dedicação")
LK_JUSTA = Skill("lk_justa", "Justa")
LK_GIANTGROWTH = Skill("lk_giant_growth", "Força Titânica")
KN_AUTOCOUNTER = Skill("lk_autocounter", "Contra-Ataque")
LK_TENSIONRELAX = Skill("lk_tensionrelax", "Relaxar")
LK_BERSERK = Skill("lk_frenesi", "Frenesi")

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
WS_CARTBOOST = Skill("ws_cartboost", "Impulso no Carrinho", 0, True)
WS_MELTDOWN = Skill("ws_meltdown", "Golpe Estilhaçante")
WS_OVERTHRUSTMAX = Skill("ws_overthrustmax", "Força Violentíssima")

# High Priest
HP_BASILICA = Skill("hp_basilica", "Basílica")

# Sniper
SN_SIGHT = Skill("sn_sight", "Visão Real", 4, True)
SN_WINDWALK = Skill("sn_windwalk", "Caminho do Vento", 0, True)

# Taekwon
TK_SEVENWIND_EARTH = Skill("tk_sevenwind", "Brisa Leve - Terra")
TK_SEVENWIND_WIND = Skill("tk_sevenwind", "Brisa Leve - Vento")
TK_SEVENWIND_WATER = Skill("tk_sevenwind", "Brisa Leve - Água")
TK_SEVENWIND_FIRE = Skill("tk_sevenwind", "Brisa Leve - Fogo")
TK_SEVENWIND_GHOST = Skill("tk_sevenwind", "Brisa Leve - Fantasma")
TK_SEVENWIND_DARK = Skill("tk_sevenwind", "Brisa Leve - Sombrio")
TK_SEVENWIND_HOLY = Skill("tk_sevenwind", "Brisa Leve - Sagrado")

# Gunslinger
GS_GATLINGFEVER = Skill("gs_gatlingfever", "Ataque Gatling")
GS_ADJUSTMENT = Skill("gs_adjustment", "Pânico do Justiceiro")
GS_INCREASING = Skill("gs_increasing", "Aumentar Precisão")

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
    "lk_justa": LK_JUSTA,
    "lk_giant_growth": LK_GIANTGROWTH,
    "lk_autocounter": KN_AUTOCOUNTER,
    "lk_tensionrelax": LK_TENSIONRELAX,
    "lk_frenesi": LK_BERSERK,
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
    "nj_utsusemi": NJ_UTSUSEMI,
    "nj_bunsinjyutsu": NJ_BUNSINJYUTSU,
    "nj_nen": NJ_NEN,
    "ba_poembragi": BA_POEMBRAGI,
    "ba_assassincross": BA_ASSASSINCROSS,
    "ba_appleidun": BA_APPLEIDUN,
    "ba_whistle": BA_WHISTLE,
    "dc_dontforgetme": DC_DONTFORGETME,
    "dc_serviceforyou": DC_SERVICEFORYOU,
    "dc_fortunekiss": DC_FORTUNEKISS,
    "dc_humming": DC_HUMMING,
    "bd_adaptation": BD_ADAPTATION,
    "bd_siegfried": BD_SIEGFRIED,
    "bd_richmankim": BD_RICHMANKIM,
    "bd_drumbattlefield": BD_DRUMBATTLEFIELD,
    "bd_ringnibelungen": BD_RINGNIBELUNGEN,
    "bd_eternalchaos": BD_ETERNALCHAOS,
    "bd_rokisweil": BD_ROKISWEIL,
    "bd_intoabyss": BD_INTOABYSS,
    "bd_lullaby": BD_LULLABY,
}
