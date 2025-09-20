from config.icon import PATH_BUFF_SKILL, PATH_ITEM, PATH_DEBUFF, get_image


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
        self.icon = get_image(PATH_DEBUFF, self.id)
        self.recover_status = recover_status


# ----- Item -----
ABRASIVE = Item("abrasive", "Abrasivo")
ACARAJE = Item("acaraje", "Acarajé")
ACCURACY_SCROLL = Item("accuracy_scroll", "Pergaminho de Precisão")
AGI_BISCUIT = Item("agi_biscuit", "Palitos de Baunilha")
AGI_FOOD = Item("agi_food_nv10", "AGI Food")
ALOE_VERA = Item("aloe_vera", "Aloe Vera")
ALMIGHTY = Item("almighty", "Elixir Ultra Milagroso")
ASPERSIO_SCROLL = Item("holy_enchant_scroll", "Conversor Elemental Sagrado")
ASSUMPTIO_SCROLL = Item("assumptio_scroll", "Pergaminho de Assumptio")
AWAKENING_POTION = Item("awakening_potion", "Poção do Despertar")
BERSERK_POTION = Item("berserk_potion", "Poção da Fúria Selvagem")
BLESS_SCROLL = Item("bless_scroll", "Scroll de Benção")
BLUE_HERB_ACTIVADOR = Item("blue_herb_activator", "Ativador de Erva Azul")
BOVINE_POTION = Item("bovine_potion", "Poção do Bovino Furioso")
BURNT_INCENSE = Item("burnt_incense", "Incenso Queimado")
CASH_FOOD = Item("cash_food", "Comida Premium")
CAT_CAN = Item("cat_can", "Khiskas Sache")
CELERMINE = Item("celermine", "Suco Celular Enriquecido")
COMBAT_MANUAL_BASE = Item("combat_manual_base", "Manual de Combate")
COMBAT_MANUAL_CLASSES = Item("combat_manual_class", "Manual de Combate de Classe")
COMBAT_PILL = Item("combat_pill", "Pílula de Combate")
CONCENTRATION_POTION = Item("concentration_potion", "Poção da Concentração")
DARK_ENCHANT_SCROLL = Item("dark_enchant_scroll", "Conversor Elemental Sombrio")
DARK_WATER = Item("dark_water", "Água Amaldiçoada")
DEX_BISCUIT = Item("dex_biscuit", "Palitos de Limão")
DEX_FOOD = Item("dex_food_nv10", "DEX Food")
DRAGON_POTION = Item("dragon_potion", "Poção do Dragão Místico")
DROWSINESS_BOX = Item("drowsiness_box", "Caixa da Sonolência")
EARTH_ENCHANT_SCROLL = Item("earth_enchant_scroll", "Conversor Elemental Terra")
EDEN_SCROLL = Item("eden_scroll", "Pergaminho do Éden", 0, True)
ELVIRA_CANDY = Item("elvira_candy", "Doce de Elvira")
FIRE_ENCHANT_SCROLL = Item("fire_enchant_scroll", "Conversor Elemental Fogo")
FLEE_SCROLL = Item("flee_scroll", "Pergaminho de Esquiva")
GHP = Item("ghp", "Poção Grande de HP")
GHOST_ENCHANT_SCROLL = Item("ghost_enchant_scroll", "Conversor Elemental Fantasma")
GLOOM_BOX = Item("gloom_box", "Caixa da Escuridão", 1, True)
GOLDEN_X = Item("golden_x", "Poção X Dourada")
GSP = Item("gsp", "Poção Grande de SP")
GUARANA = Item("guarana", "Bala de Guaraná")
GUYAK_POTION = Item("guyak_potion", "Poção de Guyak", 2, True)
HALOHALO = Item("halohalo", "Salada de Frutas Tropicais")
HALTER_LEAD = Item("halter_lead", "Rédeas")
HE_BUBBLE_GUM = Item("he_bubble_gum", "Goma de Mascar")
INC_AGI_UP_SCROLL = Item("inc_agi_up_scroll", "Scroll de Aumentar Agilidade", 0, True)
INT_BISCUIT = Item("int_biscuit", "Palitos de Chocolate")
INT_FOOD = Item("int_food_nv10", "INT Food")
LUK_BISCUIT = Item("luk_biscuit", "Palitos de Morango")
LUK_FOOD = Item("luk_food_nv10", "LUK Food")
LUX_AMINA = Item("lux_amina", "Lux Amina Rune")
MANA_PLUS = Item("mana_plus", "Poção do Furor Mágico")
MEGA_RESIST_POTION = Item("mega_resist_potion", "Poção de Mega Resistência")
MENTAL_POTION = Item("mental_potion", "Poção Mental")
MOB_TRANSFORM = Item("mob_transform", "Transformação de Monstro")
OH_HOLY_NIGHT = Item("oh_holy_night", "Caixinha Noite Feliz")
PAIN_KILLER = Item("pain_killer", "Analgésico")
PERG_ABELHA = Item("perg_abelha", "Pergaminho de Abelha Rainha")
PERG_ANGELING = Item("perg_angeling", "Pergaminho de Angeling")
PERG_GHOSTRING = Item("perg_ghostring", "Pergaminho de Ghostring")
PERG_ORCHEROIL = Item("perg_orcheroil", "Pergaminho de Orc Herói")
PERG_SENHORORC = Item("perg_senhororc", "Pergaminho de Senhor dos Orcs")
PERG_TAOGUNKA = Item("perg_taogunka", "Pergaminho de Tao Gunka")
POISON = Item("poison", "Garrafa de Veneno")
RED_BOOSTER_POTION = Item("red_booster_potion", "Elixir Rubro")
RED_HERB_ACTIVADOR = Item("red_herb_activator", "Ativador de Erva Vermelha")
REGENERATION = Item("regeneration", "Poção de Regeneração")
RESENTMENT_BOX = Item("resentment_box", "Caixa do Ressentimento")
RESIST_PROPERTY_EARTH = Item("resist_property_earth", "Poção Anti-Terra")
RESIST_PROPERTY_FIRE = Item("resist_property_fire", "Poção Anti-Fogo")
RESIST_PROPERTY_WATER = Item("resist_property_water", "Poção Anti-Água")
RESIST_PROPERTY_WIND = Item("resist_property_wind", "Poção Anti-Vento")
SPELLBREAKER = Item("spellbreaker", "Suco de Gato")
SPEED_POTION = Item("speed_potion", "Poção do Vento", 0, True)
STR_BISCUIT = Item("str_biscuit", "Palitos de Laranja")
STR_FOOD = Item("str_food_nv10", "STR Food")
SUNLIGHT_BOX = Item("sunlight_box", "Caixa da Luz do Sol")
SWING_K = Item("swing_k", "Poção do Furor Físico")
THUNDER_BOX = Item("thunder_box", "Caixa do Trovão")
VITATA_POTION = Item("vitata_potion", "Poção Vitata")
VIT_BISCUIT = Item("vit_biscuit", "Palitos de Cassis")
VIT_FOOD = Item("vit_food_nv10", "VIT Food")
WATER_ENCHANT_SCROLL = Item("water_enchant_scroll", "Conversor Elemental Água")
WIND_ENCHANT_SCROLL = Item("wind_enchant_scroll", "Conversor Elemental Vento")


ITEM_BUFF_MAP = {
    "abrasive": ABRASIVE,
    "acaraje": ACARAJE,
    "accuracy_scroll": ACCURACY_SCROLL,
    "agi_biscuit": AGI_BISCUIT,
    "agi_food": AGI_FOOD,
    "almighty": ALMIGHTY,
    "assumptio_scroll": ASSUMPTIO_SCROLL,
    "awakening_potion": AWAKENING_POTION,
    "berserk_potion": BERSERK_POTION,
    "bless_scroll": BLESS_SCROLL,
    "blue_herb_activator": BLUE_HERB_ACTIVADOR,
    "bovine_potion": BOVINE_POTION,
    "burnt_incense": BURNT_INCENSE,
    "cash_food": CASH_FOOD,
    "cat_can": CAT_CAN,
    "celermine": CELERMINE,
    "combat_manual_base": COMBAT_MANUAL_BASE,
    "combat_manual_class": COMBAT_MANUAL_CLASSES,
    "combat_pill": COMBAT_PILL,
    "concentration_potion": CONCENTRATION_POTION,
    "dark_enchant_scroll": DARK_ENCHANT_SCROLL,
    "dark_water": DARK_WATER,
    "dex_biscuit": DEX_BISCUIT,
    "dex_food": DEX_FOOD,
    "dragon_potion": DRAGON_POTION,
    "drowsiness_box": DROWSINESS_BOX,
    "earth_enchant_scroll": EARTH_ENCHANT_SCROLL,
    "eden_scroll": EDEN_SCROLL,
    "elvira_candy": ELVIRA_CANDY,
    "fire_enchant_scroll": FIRE_ENCHANT_SCROLL,
    "flee_scroll": FLEE_SCROLL,
    "ghp": GHP,
    "ghost_enchant_scroll": GHOST_ENCHANT_SCROLL,
    "gloom_box": GLOOM_BOX,
    "golden_x": GOLDEN_X,
    "gsp": GSP,
    "guarana": GUARANA,
    "guyak_potion": GUYAK_POTION,
    "halohalo": HALOHALO,
    "halter_lead": HALTER_LEAD,
    "he_bubble_gum": HE_BUBBLE_GUM,
    "holy_enchant_scroll": ASPERSIO_SCROLL,
    "inc_agi_up_scroll": INC_AGI_UP_SCROLL,
    "int_biscuit": INT_BISCUIT,
    "int_food": INT_FOOD,
    "luk_biscuit": LUK_BISCUIT,
    "luk_food": LUK_FOOD,
    "lux_amina": LUX_AMINA,
    "mana_plus": MANA_PLUS,
    "mega_resist_potion": MEGA_RESIST_POTION,
    "mental_potion": MENTAL_POTION,
    "mob_transform": MOB_TRANSFORM,
    "oh_holy_night": OH_HOLY_NIGHT,
    "pain_killer": PAIN_KILLER,
    "perg_abelha": PERG_ABELHA,
    "perg_angeling": PERG_ANGELING,
    "perg_ghostring": PERG_GHOSTRING,
    "perg_orcheroil": PERG_ORCHEROIL,
    "perg_senhororc": PERG_SENHORORC,
    "perg_taogunka": PERG_TAOGUNKA,
    "poison": POISON,
    "red_booster_potion": RED_BOOSTER_POTION,
    "red_herb_activator": RED_HERB_ACTIVADOR,
    "regeneration": REGENERATION,
    "resentment_box": RESENTMENT_BOX,
    "resist_property_earth": RESIST_PROPERTY_EARTH,
    "resist_property_fire": RESIST_PROPERTY_FIRE,
    "resist_property_water": RESIST_PROPERTY_WATER,
    "resist_property_wind": RESIST_PROPERTY_WIND,
    "speed_potion": SPEED_POTION,
    "spellbreaker": SPELLBREAKER,
    "str_biscuit": STR_BISCUIT,
    "str_food": STR_FOOD,
    "sunlight_box": SUNLIGHT_BOX,
    "swing_k": SWING_K,
    "thunder_box": THUNDER_BOX,
    "vitata_potion": VITATA_POTION,
    "vit_biscuit": VIT_BISCUIT,
    "vit_food": VIT_FOOD,
    "water_enchant_scroll": WATER_ENCHANT_SCROLL,
    "wind_enchant_scroll": WIND_ENCHANT_SCROLL,
}

ITEM_BUFF_GROUP = {
    "Poções": [
        GHP, GSP, CONCENTRATION_POTION, AWAKENING_POTION, BERSERK_POTION, SPEED_POTION,
        RED_HERB_ACTIVADOR, BLUE_HERB_ACTIVADOR, SWING_K, MANA_PLUS, SPELLBREAKER, MENTAL_POTION,
        VITATA_POTION, RED_BOOSTER_POTION, BOVINE_POTION, DRAGON_POTION, REGENERATION,
        GOLDEN_X, MEGA_RESIST_POTION, GUYAK_POTION, CELERMINE, POISON
    ],
    "Caixas": [
        RESENTMENT_BOX, THUNDER_BOX, DROWSINESS_BOX, GLOOM_BOX, SUNLIGHT_BOX
    ],
    "Consumíveis": [
        ALOE_VERA, PAIN_KILLER, ABRASIVE, CAT_CAN, CASH_FOOD, COMBAT_PILL, ACARAJE, HALOHALO, GUARANA, ALMIGHTY, OH_HOLY_NIGHT, ELVIRA_CANDY
    ],
    "Scrolls": [
        BLESS_SCROLL, INC_AGI_UP_SCROLL, ASPERSIO_SCROLL,
        EDEN_SCROLL, ASSUMPTIO_SCROLL, FLEE_SCROLL, ACCURACY_SCROLL,
        PERG_GHOSTRING, PERG_ANGELING, PERG_TAOGUNKA, PERG_SENHORORC, PERG_ORCHEROIL, PERG_ABELHA
    ],
    "Elemento - Arma": [
        FIRE_ENCHANT_SCROLL, WATER_ENCHANT_SCROLL, WIND_ENCHANT_SCROLL, EARTH_ENCHANT_SCROLL, ASPERSIO_SCROLL, DARK_ENCHANT_SCROLL, GHOST_ENCHANT_SCROLL, DARK_WATER
    ],
    "Elemento - Resistência": [
        RESIST_PROPERTY_WATER, RESIST_PROPERTY_EARTH, RESIST_PROPERTY_FIRE, RESIST_PROPERTY_WIND, MEGA_RESIST_POTION
    ],
    "Comidas": [
        STR_FOOD, AGI_FOOD, VIT_FOOD, INT_FOOD, DEX_FOOD, LUK_FOOD,
        STR_BISCUIT, AGI_BISCUIT, VIT_BISCUIT, INT_BISCUIT, DEX_BISCUIT, LUK_BISCUIT
    ],
    "Manuais e Runes": [
        COMBAT_MANUAL_BASE, COMBAT_MANUAL_CLASSES, LUX_AMINA
    ],
    "Doces e Gomas": [
        HE_BUBBLE_GUM
    ],
    "Incensos e Transformações": [
        BURNT_INCENSE, MOB_TRANSFORM
    ],
}

# ----- Item cura debuff -----
BLEEDING = "bleeding"
BLIND = "blind"
BURNING = "burning"
CHAOS = "chaos"
CRITICAL_WOUNDS = "critical_wounds"
CURSE = "curse"
CURSED_FIELD = "cursed_field"
DECREASE_AGI = "decrease_agi"
HOWLING = "howling"
HYPOTHERMIA = "hypothermia"
POISON_STATUS = "poison"
QUAGMIRE = "quagmire"
SILENCE = "silence"
SLEEP = "sleep"
SLOW_CASTING = "slow_casting"
TO_SIT = "to_sit"

GREEN_POTION = Debuff("green_potion", "Poção Verde", [BLIND, CHAOS, POISON_STATUS, SILENCE], 3)
GREEN_HERB = Debuff("green_herb", "Erva Verde", [POISON_STATUS], 4)
ELVIRA_CANDY = Debuff("elvira_candy", "Doce de Elvira", [SLOW_CASTING, CRITICAL_WOUNDS, HYPOTHERMIA, TO_SIT, HOWLING, CURSED_FIELD, BURNING, SLEEP, CHAOS], 1)
PANACEA = Debuff("panacea", "Panacéia", [BLIND, CHAOS, CURSE, POISON_STATUS, SILENCE], 1)
SPEED_POTION = Debuff("speed_potion", "Poção do Vento", [DECREASE_AGI, QUAGMIRE], 2)
GUYAK_POTION = Debuff("guyak_potion", "Poção de Guyak", [DECREASE_AGI, QUAGMIRE], 2)

ITEM_DEBUFF_GROUP = {
    "Consumíveis": [ELVIRA_CANDY, PANACEA, GREEN_POTION, GREEN_HERB, GUYAK_POTION, SPEED_POTION],
}

ITEM_DEBUFF_MAP = {
    "elvira_candy": ELVIRA_CANDY,
    "panacea": PANACEA,
    "green_potion": GREEN_POTION,
    "green_herb": GREEN_HERB,
    "speed_potion": SPEED_POTION,
    "guyak_potion": GUYAK_POTION,
}

# ----- Skill -----

# Swordman
SM_MAGNUM = Skill("sm_magnum", "Impacto Explosivo", 1, False, 180)
SM_ENDURE = Skill("sm_endure", "Vigor", 0, False, 37)
SM_AUTOBERSERK = Skill("sm_autoberserk", "Instinto de Sobrevivência")

# Mage
MG_ENERGYCOAT = Skill("mg_energycoat", "Proteção Arcana")

# Merchat
MC_LOUD = Skill("mc_loud", "Grito de Guerra", 0, False, 300)

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
LK_AURABLADE = Skill("lk_aurablade", "Lâmina de Aura", 3, False, 120)
LK_PARRYING = Skill("lk_parrying", "Aparar Golpe", 0, False, 60)
LK_CONCENTRATION = Skill("lk_concentration", "Dedicação", 2, False, 120)
LK_JUSTA = Skill("lk_justa", "Justa")
LK_GIANTGROWTH = Skill("lk_giant_growth", "Força Titânica", 4, False, 180)
KN_AUTOCOUNTER = Skill("lk_autocounter", "Contra-Ataque", 0, False, 2)
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

EQUIP_BUFFS = []

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