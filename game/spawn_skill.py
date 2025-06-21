from config.icon import PATH_SPAWN_SKILL, get_image


class SpawnSkill:
    def __init__(self, _id, name, is_clicked=True):
        self.id = _id
        self.name = name
        self.is_clicked = is_clicked
        self.icon = get_image(PATH_SPAWN_SKILL, self.id)


# Novice
ATTACK_1 = SpawnSkill("attack_1", "Ataque 1")
ATTACK_2 = SpawnSkill("attack_2", "Ataque 2")
ATTACK_3 = SpawnSkill("attack_3", "Ataque 3")
ATTACK_4 = SpawnSkill("attack_4", "Ataque 4")
NV_FIRSTAID = SpawnSkill("nv_firstaid", "Primeiros Socorros", False)

# Swordman
SM_BASH = SpawnSkill("sm_bash", "Golpe Fulminante")
SM_PROVOKE = SpawnSkill("sm_provoke", "Provocar")

# Mage
MG_FIREBOLT = SpawnSkill("mg_firebolt", "Lança de Fogo")
MG_FIREBALL = SpawnSkill("mg_fireball", "Bolas de Fogo")
MG_FIREWALL = SpawnSkill("mg_firewall", "Barreira de Fogo")
MG_COLDBOLT = SpawnSkill("mg_coldbolt", "Lanças de Gelo")
MG_FROSTDIVER = SpawnSkill("mg_frostdiver", "Rajada Congelante")
MG_LIGHTNINGBOLT = SpawnSkill("mg_lightningbolt", "Relâmpago")
MG_THUNDERSTORM = SpawnSkill("mg_thunderstorm", "Tempestade de Raios")
MG_NAPALMBEAT = SpawnSkill("mg_napalmbeat", "Ataque Espiritual")
MG_SOULSTRIKE = SpawnSkill("mg_soulstrike", "Espíritos Anciões")
MG_SAFETYWALL = SpawnSkill("mg_safetywall", "Escudo Mágico")
MG_STONECURSE = SpawnSkill("mg_stonecurse", "Petrificar")

# Thief
TF_SPRINKLESAND = SpawnSkill("tf_sprinklesand", "Chutar Areia")
TF_BACKSLIDING = SpawnSkill("tf_backsliding", "Recuar", False)
TF_PICKSTONE = SpawnSkill("tf_pickstone", "Procurar Pedras", False)
TF_THROWSTONE = SpawnSkill("tf_throwstone", "Arremessar Pedra")
TF_POISON = SpawnSkill("tf_poison", "Envenenar")
TF_DETOXIFY = SpawnSkill("tf_detoxify", "Desintoxicar")
TF_STEAL = SpawnSkill("tf_steal", "Furto")

# Merchant
MC_MAMMONITE = SpawnSkill("mc_mammonite", "Mammonita")
MC_CARTREVOLUTION = SpawnSkill("mc_cartrevolution", "Cavalo-de-Pau")

# Acolyte
AL_BLESSING = SpawnSkill("al_blessing", "Bênção")
AL_HEAL = SpawnSkill("al_heal", "Curar")
AL_CURE = SpawnSkill("al_cure", "Medicar")
AL_INCAGI = SpawnSkill("al_incagi", "Aumentar Agilidade")
AL_DECAGI = SpawnSkill("al_decagi", "Diminuir Agilidade")
AL_PNEUMA = SpawnSkill("al_pneuma", "Escudo Sagrado")
AL_HOLYWATER = SpawnSkill("al_holywater", "Aqua Benedicta", False)
AL_HOLYLIGHT = SpawnSkill("al_holylight", "Luz Divina")

# Archer
AC_DOUBLE = SpawnSkill("ac_double", "Rajada de Flechas")
AC_SHOWER = SpawnSkill("ac_shower", "Chuva de Flechas")
AC_CHARGEARROW = SpawnSkill("ac_chargearrow", "Disparo Violento")

# Knight
KN_BOWLINGBASH = SpawnSkill("kn_bowlingbash", "Impacto de Tyr")
KN_PIERCE = SpawnSkill("kn_pierce", "Perfurar")
KN_SPEARSTAB = SpawnSkill("kn_spearstab", "Estocada")
KN_SPEARBOOMERANG = SpawnSkill("kn_spearboomerang", "Lança Bumerangue")
KN_BRANDISHSPEAR = SpawnSkill("kn_brandishspear", "Brandir Lança")
KN_CHARGEATK = SpawnSkill("kn_chargeatk", "Avanço Ofensivo")

# Crusader
CR_HOLYCROSS = SpawnSkill("cr_holycross", "Crux Divinum")
CR_GRANDCROSS = SpawnSkill("cr_grandcross", "Crux Magnum")
CR_DEVOTION = SpawnSkill("cr_devotion", "Redenção")
CR_SHIELDCHARGE = SpawnSkill("cr_shieldcharge", "Punição Divina")
CR_SHIELDBOOMERANG = SpawnSkill("cr_shieldboomerang", "Escudo Bumerangue")
CR_PROVIDENCE = SpawnSkill("cr_providence", "Divina Providência")

# Wizard
WZ_EARTHSPIKE = SpawnSkill("wz_earthspike", "Coluna de Pedra")
WZ_QUAGMIRE = SpawnSkill("wz_quagmire", "Pântano dos Mortos")
WZ_HEAVENDRIVE = SpawnSkill("wz_heavendrive", "Fúria da Terra")
WZ_FROSTNOVA = SpawnSkill("wz_frostnova", "Congelar", False)
WZ_ICEWALL = SpawnSkill("wz_icewall", "Barreira de Gelo")
WZ_STORMGUST = SpawnSkill("wz_stormgust", "Nevasca")
WZ_WATERBALL = SpawnSkill("wz_waterball", "Esfera d'Água")
WZ_METEOR = SpawnSkill("wz_meteor", "Chuva de Meteoros")
WZ_SIGHTRASHER = SpawnSkill("wz_sightrasher", "Supernova", False)
WZ_FIREPILLAR = SpawnSkill("wz_firepillar", "Coluna de Fogo")
WZ_JUPITEL = SpawnSkill("wz_jupitel", "Trovão de Júpiter")
WZ_VERMILION = SpawnSkill("wz_vermilion", "Ira de Thor")

# Sage
SA_ABRACADABRA = SpawnSkill("sa_abracadabra", "Abracadabra", False)
SA_CASTCANCEL = SpawnSkill("sa_castcancel", "Cancelar Magia", False)
SA_VIOLENTGALE = SpawnSkill("sa_violentgale", "Furacão")
SA_VOLCANO = SpawnSkill("sa_volcano", "Vulcão")
SA_DELUGE = SpawnSkill("sa_deluge", "Dilúvio")
SA_FLAMELAUNCHER = SpawnSkill("sa_flamelauncher", "Encantar com Chama")
SA_FROSTWEAPON = SpawnSkill("sa_frostweapon", "Encantar com Geada")
SA_LIGHTNINGLOADER = SpawnSkill("sa_lightningloader", "Encantar com Ventania")
SA_SEISMICWEAPON = SpawnSkill("sa_seismicweapon", "Encantar com Terremoto")
SA_SPELLBREAKER = SpawnSkill("sa_spellbreaker", "Desconcentrar")
SA_DISPELL = SpawnSkill("sa_dispell", "Desencantar")
SA_LANDPROTECTOR = SpawnSkill("sa_landprotector", "Proteger Terreno")
SA_ELEMENT = SpawnSkill("sa_element", "Mudança Elemental")

# Assassin
AS_SONICBLOW = SpawnSkill("as_sonicblow", "Lâminas Destruidoras")
AS_GRIMTOOTH = SpawnSkill("as_grimtooth", "Tocaia")
AS_ENCHANTPOISON = SpawnSkill("as_enchantpoison", "Envenenar Arma")
AS_VENOMDUST = SpawnSkill("as_venomdust", "Névoa Tóxica")
AS_SPLASHER = SpawnSkill("as_splasher", "Explosão Tóxica")
AS_VENOMKNIFE = SpawnSkill("as_venomknife", "Faca Envenenada")

# Rogue
RG_BACKSTAP = SpawnSkill("rg_backstap", "Apunhalar")
RG_RAID = SpawnSkill("rg_raid", "Ataque Surpresa", False)
RG_INTIMIDATE = SpawnSkill("rg_intimidate", "Rapto")
RG_STEALCOIN = SpawnSkill("rg_stealcoin", "Afanar")
RG_STRIPARMOR = SpawnSkill("rg_striparmor", "Remover Armadura")
RG_STRIPHELM = SpawnSkill("rg_striphelm", "Remover Capacete")
RG_STRIPSHIELD = SpawnSkill("rg_stripshield", "Remover Escudo")
RG_STRIPWEAPON = SpawnSkill("rg_stripweapon", "Remover Arma")
RG_CLOSECONFINE = SpawnSkill("rg_closeconfine", "Confinamento")

# Blacksmith
BS_HAMMERFALL = SpawnSkill("bs_hammerfall", "Martelo de Thor")
BS_REPAIRWEAPON = SpawnSkill("bs_repairweapon", "Consertar Armas")
BS_GREED = SpawnSkill("bs_greed", "Ganância")

# Alchemist
AM_DEMONSTRATION = SpawnSkill("am_demonstration", "Fogo Grego")
AM_ACIDTERROR = SpawnSkill("am_acidterror", "Terror Ácido")
AM_CANNIBALIZE = SpawnSkill("am_cannibalize", "Criar Monstro Planta")
AM_SPHEREMINE = SpawnSkill("am_spheremine", "Criar Esfera Marinha")
AM_POTIONPITCHER = SpawnSkill("am_potionpitcher", "Arremessar Poção")
AM_CP_HELM = SpawnSkill("am_cp_helm", "Revestir Capacete")
AM_CP_WEAPON = SpawnSkill("am_cp_weapon", "Revestir Arma")
AM_CP_ARMOR = SpawnSkill("am_cp_armor", "Revestir Armadura")
AM_CP_SHIELD = SpawnSkill("am_cp_shield", "Revestir Escudo")
AM_BERSERKPITCHER = SpawnSkill("am_berserkpitcher", "Arremessar Poção da Fúria Selvagem")

# Priest
PR_KYRIE = SpawnSkill("pr_kyrie", "Kyrie Eleison")
PR_IMPOSITIO = SpawnSkill("pr_impositio", "Impositio Manus")
PR_SUFFRAGIUM = SpawnSkill("pr_suffragium", "Suffragium")
PR_ASPERSIO = SpawnSkill("pr_aspersio", "Aspersio")
PR_BENEDICTIO = SpawnSkill("pr_benedictio", "B. S. Sacramenti")
PR_MAGNUS = SpawnSkill("pr_magnus", "Magnus Exorcismus")
PR_LEXDIVINA = SpawnSkill("pr_lexdivina", "Lex Divina")
PR_TURNUNDEAD = SpawnSkill("pr_turnundead", "Esconjurar")
PR_LEXAETERNA = SpawnSkill("pr_lexaeterna", "Lex Aeterna")
PR_STRECOVERY = SpawnSkill("pr_strecovery", "Graça Divina")
PR_SLOWPOISON = SpawnSkill("pr_slowpoison", "Retardar Veneno")
ALL_RESURRECTION = SpawnSkill("all_resurrection", "Ressuscitar")
PR_SANCTUARY = SpawnSkill("pr_sanctuary", "Santuário")
PR_REDEMPTIO = SpawnSkill("pr_redemptio", "Martírio", False)

# Monk
MO_EXTREMITYFIST = SpawnSkill("mo_extremityfist", "Punho Supremo de Asura")
MO_INVESTIGATE = SpawnSkill("mo_investigate", "Impacto Psíquico")
MO_BODYRELOCATION = SpawnSkill("mo_bodyrelocation", "Passo Etéreo")
MO_ABSORBSPIRITS = SpawnSkill("mo_absorbspirits", "Absorver Esferas Espirituais")
MO_CALLSPIRITS = SpawnSkill("mo_callspirits", "Invocar Esfera Espiritual", False)
MO_FINGEROFFENSIVE = SpawnSkill("mo_fingeroffensive", "Disparo de Esferas Espirituais")
MO_KITRANSLATION = SpawnSkill("mo_kitranslation", "Concessão Espiritual")
MO_BALKYOUNG = SpawnSkill("mo_balkyoung", "Punhos Intensos")

# Hunter
HT_LANDMINE = SpawnSkill("ht_landmine", "Armadilha Atordoante")
HT_FREEZINGTRAP = SpawnSkill("ht_freezingtrap", "Armadilha Congelante")
HT_BLASTMINE = SpawnSkill("ht_blastmine", "Instalar Mina")
HT_CLAYMORETRAP = SpawnSkill("ht_claymoretrap", "Armadilha Explosiva")
HT_SKIDTRAP = SpawnSkill("ht_skidtrap", "Armadilha Escorregadia")
HT_FLASHER = SpawnSkill("ht_flasher", "Armadilha Luminosa")
HT_SHOCKWAVE = SpawnSkill("ht_shockwave", "Armadilha Extenuante")
HT_SANDMAN = SpawnSkill("ht_sandman", "Armadilha Sonífera")
HT_BLITZBEAT = SpawnSkill("ht_blitzbeat", "Ataque Aéreo")
HT_DETECTING = SpawnSkill("ht_detecting", "Alerta")
HT_REMOVETRAP = SpawnSkill("ht_removetrap", "Remover Armadilha")
HT_SPRINGTRAP = SpawnSkill("ht_springtrap", "Desativar Armadilha")
HT_PHANTASMIC = SpawnSkill("ht_phantasmic", "Flecha Ilusória")
HT_POWER = SpawnSkill("ht_power", "Ataque da Fera")

# Bard
BA_FROSTJOKE = SpawnSkill("ba_frostjoke", "Piada Infame", False)
BA_MUSICALSTRIKE = SpawnSkill("ba_musicalstrike", "Flecha Melódica")
BA_PANGVOICE = SpawnSkill("ba_pangvoice", "Voz Dolorosa")

# Dancer
DC_SCREAM = SpawnSkill("dc_scream", "Escândalo", False)
DC_THROWARROW = SpawnSkill("dc_throwarrow", "Estilingue")
DC_WINKCHARM = SpawnSkill("dc_winkcharm", "Piscadela")

# Lord
LK_SPIRALPIERCE = SpawnSkill("lk_spiralpierce", "Perfurar em Espiral")
LK_HEADCRUSH = SpawnSkill("lk_headcrush", "Golpe Traumático")
LK_JOINTBEAT = SpawnSkill("lk_jointbeat", "Ataque Vital")

# Paladin
PA_SHIELDCHAIN = SpawnSkill("pa_shieldchain", "Choque Rápido")
PA_PRESSURE = SpawnSkill("pa_pressure", "Gloria Domini")

# High Wizard
HW_GANBANTEIN = SpawnSkill("hw_ganbantein", "Ganbantein")
HW_GRAVITATION = SpawnSkill("hw_gravitation", "Campo Gravitacional")
HW_NAPALMVULCAN = SpawnSkill("hw_napalmvulcan", "Vulcão Napalm")
HW_MAGICCRASHER = SpawnSkill("hw_magiccrasher", "Esmagamento Mágico")

# Professor
PF_FOGWALL = SpawnSkill("pf_fogwall", "Bruma Ofuscante")
PF_SPIDERWEB = SpawnSkill("pf_spiderweb", "Prisão de Teia")
PF_HPCONVERSION = SpawnSkill("pf_hpconversion", "Indulgir", False)
PF_SOULCHANGE = SpawnSkill("pf_soulchange", "Exalar Alma")
PF_MINDBREAKER = SpawnSkill("pf_mindbreaker", "Enlouquecedor")
PF_SOULBURN = SpawnSkill("pf_soulburn", "Sifão de Alma")

# Assassin Cross
ASC_METEORASSAULT = SpawnSkill("asc_meteorassault", "Impacto Meteoro", False)
ASC_BREAKER = SpawnSkill("asc_breaker", "Destruidor de Almas")

# Stalker
ST_FULLSTRIP = SpawnSkill("st_fullstrip", "Remoção Total")

# Whitesmith
WS_CARTTERMINATION = SpawnSkill("ws_carttermination", "Choque do Carrinho")

# Biochemist
CR_ACIDDEMONSTRATION = SpawnSkill("cr_aciddemonstration", "Bomba Ácida")
CR_SLIMPITCHER = SpawnSkill("cr_slimpitcher", "Arremessar Poção Compacta")
CR_FULLPROTECTION = SpawnSkill("cr_fullprotection", "Proteção Química Total")

# High Priest
HP_ASSUMPTIO = SpawnSkill("hp_assumptio", "Assumptio")

# Champion
CH_PALMSTRIKE = SpawnSkill("ch_palmstrike", "Golpe da Palma em Fúria")

# Sniper
SN_SHARPSHOOTING = SpawnSkill("sn_sharpshooting", "Tiro Preciso")
SN_FALCONASSAULT = SpawnSkill("sn_falconassault", "Assalto do Falcão")

# Clown / Gypsy
CG_ARROWVULCAN = SpawnSkill("cg_arrowvulcan", "Vulcão de Flechas")
CG_TAROTCARD = SpawnSkill("cg_tarotcard", "Destino nas Cartas")

# Taekwon
TK_JUMPKICK = SpawnSkill("tk_jumpkick", "Chute Aéreo")

# Gunslinger
GS_FLING = SpawnSkill("gs_fling", "Atirar Moedas")
GS_CRACKER = SpawnSkill("gs_cracker", "Tiro Bombinha")
GS_TRIPLEACTION = SpawnSkill("gs_tripleaction", "Ataque Triplo")
GS_BULLSEYE = SpawnSkill("gs_bullseye", "Ataque Certeiro")
GS_RAPIDSHOWER = SpawnSkill("gs_rapidshower", "Rajada Certeira")
GS_DESPERADO = SpawnSkill("gs_desperado", "Desperado", False)
GS_TRACKING = SpawnSkill("gs_tracking", "Rastrear o Alvo")
GS_DISARM = SpawnSkill("gs_disarm", "Desarmar")
GS_PIERCINGSHOT = SpawnSkill("gs_piercingshot", "Ferir Alvo")
GS_DUST = SpawnSkill("gs_dust", "Controle de Multidão")
GS_FULLBUSTER = SpawnSkill("gs_fullbuster", "Ataque Total")
GS_SPREADATTACK = SpawnSkill("gs_spreadattack", "Disparo Espalhado")
GS_GROUNDDRIFT = SpawnSkill("gs_grounddrift", "Mina do Justiceiro")
GS_GLITTERIN = SpawnSkill("gs_glitterin", "Cara ou Coroa", False)

# Ninja
NJ_KOUENKA = SpawnSkill("nj_kouenka", "Pétalas Flamejantes")
NJ_KAENSIN = SpawnSkill("nj_kaensin", "Escudo de Chamas", False)
NJ_BAKUENRYU = SpawnSkill("nj_bakuenryu", "Dragão Explosivo")
NJ_ISSEN = SpawnSkill("nj_issen", "Ataque Mortal")
NJ_HYOUSENSOU = SpawnSkill("nj_hyousensou", "Lança Congelante")
NJ_SUITON = SpawnSkill("nj_suiton", "Evasão Aquática")
NJ_HYOUSYOURAKU = SpawnSkill("nj_hyousyouraku", "Grande Floco de Neve", False)
NJ_SYURIKEN = SpawnSkill("nj_syuriken", "Arremessar Shuriken")
NJ_KUNAI = SpawnSkill("nj_kunai", "Arremessar Kunai")
NJ_HUUMA = SpawnSkill("nj_huuma", "Arremessar Huuma")
NJ_ZENYNAGE = SpawnSkill("nj_zenynage", "Chuva de Moedas")
NJ_TATAMIGAESHI = SpawnSkill("nj_tatamigaeshi", "Virar Tatami", False)
NJ_HUUJIN = SpawnSkill("nj_huujin", "Lâmina de Vento")
NJ_RAIGEKISAI = SpawnSkill("nj_raigekisai", "Descarga Elétrica")
NJ_KAMAITACHI = SpawnSkill("nj_kamaitachi", "Brisa Cortante")
NJ_KIRIKAGE = SpawnSkill("nj_kirikage", "Corte das Sombras")
NJ_KASUMIKIRI = SpawnSkill("nj_kasumikiri", "Corte da Névoa")

# Soul Linker
SL_ALCHEMIST = SpawnSkill("sl_alchemist", "Espírito do Alquimista")
SL_ROGUE = SpawnSkill("sl_rogue", "Espírito do Arruaceiro")
SL_BARDDANCER = SpawnSkill("sl_barddancer", "Espírito dos Artistas")
SL_WIZARD = SpawnSkill("sl_wizard", "Espírito do Bruxo")
SL_HUNTER = SpawnSkill("sl_hunter", "Espírito do Caçador")
SL_KNIGHT = SpawnSkill("sl_knight", "Espírito do Cavaleiro")
SL_SOULLINKER = SpawnSkill("sl_soullinker", "Espírito do Espiritualista")
SL_BLACKSMITH = SpawnSkill("sl_blacksmith", "Espírito do Ferreiro")
SL_ASSASIN = SpawnSkill("sl_assasin", "Espírito do Mercenário")
SL_STAR = SpawnSkill("sl_star", "Espírito do Mestre Taekwon")
SL_MONK = SpawnSkill("sl_monk", "Espírito do Monge")
SL_SAGE = SpawnSkill("sl_sage", "Espírito do Sábio")
SL_PRIEST = SpawnSkill("sl_priest", "Espírito do Sacerdote")
SL_SUPERNOVICE = SpawnSkill("sl_supernovice", "Espírito do Superaprendiz")
SL_CRUSADER = SpawnSkill("sl_crusader", "Espírito do Templário")
SL_HIGH = SpawnSkill("sl_high", "Espírito dos Transcendentais")
SL_SMA = SpawnSkill("sl_sma", "Esma")
SL_STIN = SpawnSkill("sl_stin", "Estin")
SL_STUN = SpawnSkill("sl_stun", "Estun")
SL_SKA = SpawnSkill("sl_ska", "Eska")
SL_SKE = SpawnSkill("sl_ske", "Eske")
SL_SWOO = SpawnSkill("sl_swoo", "Eswoo")
SL_KAAHI = SpawnSkill("sl_kaahi", "Kaahi")
SL_KAITE = SpawnSkill("sl_kaite", "Kaite")
SL_KAIZEL = SpawnSkill("sl_kaizel", "Kaizel")
SL_KAUPE = SpawnSkill("sl_kaupe", "Kaupe")

SPAWN_SKILL_MAP = {
    "attack_1": ATTACK_1,
    "attack_2": ATTACK_2,
    "attack_3": ATTACK_3,
    "attack_4": ATTACK_4,
    "nv_firstaid": NV_FIRSTAID,
    "sm_bash": SM_BASH,
    "sm_provoke": SM_PROVOKE,
    "mg_firebolt": MG_FIREBOLT,
    "mg_fireball": MG_FIREBALL,
    "mg_firewall": MG_FIREWALL,
    "mg_coldbolt": MG_COLDBOLT,
    "mg_frostdiver": MG_FROSTDIVER,
    "mg_lightningbolt": MG_LIGHTNINGBOLT,
    "mg_thunderstorm": MG_THUNDERSTORM,
    "mg_napalmbeat": MG_NAPALMBEAT,
    "mg_soulstrike": MG_SOULSTRIKE,
    "mg_safetywall": MG_SAFETYWALL,
    "mg_stonecurse": MG_STONECURSE,
    "tf_sprinklesand": TF_SPRINKLESAND,
    "tf_backsliding": TF_BACKSLIDING,
    "tf_pickstone": TF_PICKSTONE,
    "tf_throwstone": TF_THROWSTONE,
    "tf_poison": TF_POISON,
    "tf_detoxify": TF_DETOXIFY,
    "tf_steal": TF_STEAL,
    "mc_mammonite": MC_MAMMONITE,
    "mc_cartrevolution": MC_CARTREVOLUTION,
    "al_blessing": AL_BLESSING,
    "al_heal": AL_HEAL,
    "al_cure": AL_CURE,
    "al_incagi": AL_INCAGI,
    "al_decagi": AL_DECAGI,
    "al_pneuma": AL_PNEUMA,
    "al_holywater": AL_HOLYWATER,
    "al_holylight": AL_HOLYLIGHT,
    "ac_double": AC_DOUBLE,
    "ac_shower": AC_SHOWER,
    "ac_chargearrow": AC_CHARGEARROW,
    "kn_bowlingbash": KN_BOWLINGBASH,
    "kn_pierce": KN_PIERCE,
    "kn_spearstab": KN_SPEARSTAB,
    "kn_spearboomerang": KN_SPEARBOOMERANG,
    "kn_brandishspear": KN_BRANDISHSPEAR,
    "kn_chargeatk": KN_CHARGEATK,
    "cr_holycross": CR_HOLYCROSS,
    "cr_grandcross": CR_GRANDCROSS,
    "cr_devotion": CR_DEVOTION,
    "cr_shieldcharge": CR_SHIELDCHARGE,
    "cr_shieldboomerang": CR_SHIELDBOOMERANG,
    "cr_providence": CR_PROVIDENCE,
    "wz_earthspike": WZ_EARTHSPIKE,
    "wz_quagmire": WZ_QUAGMIRE,
    "wz_heavendrive": WZ_HEAVENDRIVE,
    "wz_frostnova": WZ_FROSTNOVA,
    "wz_icewall": WZ_ICEWALL,
    "wz_stormgust": WZ_STORMGUST,
    "wz_waterball": WZ_WATERBALL,
    "wz_meteor": WZ_METEOR,
    "wz_sightrasher": WZ_SIGHTRASHER,
    "wz_firepillar": WZ_FIREPILLAR,
    "wz_jupitel": WZ_JUPITEL,
    "wz_vermilion": WZ_VERMILION,
    "sa_abracadabra": SA_ABRACADABRA,
    "sa_castcancel": SA_CASTCANCEL,
    "sa_violentgale": SA_VIOLENTGALE,
    "sa_volcano": SA_VOLCANO,
    "sa_deluge": SA_DELUGE,
    "sa_flamelauncher": SA_FLAMELAUNCHER,
    "sa_frostweapon": SA_FROSTWEAPON,
    "sa_lightningloader": SA_LIGHTNINGLOADER,
    "sa_seismicweapon": SA_SEISMICWEAPON,
    "sa_spellbreaker": SA_SPELLBREAKER,
    "sa_dispell": SA_DISPELL,
    "sa_landprotector": SA_LANDPROTECTOR,
    "sa_element": SA_ELEMENT,
    "as_sonicblow": AS_SONICBLOW,
    "as_grimtooth": AS_GRIMTOOTH,
    "as_enchantpoison": AS_ENCHANTPOISON,
    "as_venomdust": AS_VENOMDUST,
    "as_splasher": AS_SPLASHER,
    "as_venomknife": AS_VENOMKNIFE,
    "rg_backstap": RG_BACKSTAP,
    "rg_raid": RG_RAID,
    "rg_intimidate": RG_INTIMIDATE,
    "rg_stealcoin": RG_STEALCOIN,
    "rg_striparmor": RG_STRIPARMOR,
    "rg_striphelm": RG_STRIPHELM,
    "rg_stripshield": RG_STRIPSHIELD,
    "rg_stripweapon": RG_STRIPWEAPON,
    "rg_closeconfine": RG_CLOSECONFINE,
    "bs_hammerfall": BS_HAMMERFALL,
    "bs_repairweapon": BS_REPAIRWEAPON,
    "bs_greed": BS_GREED,
    "am_demonstration": AM_DEMONSTRATION,
    "am_acidterror": AM_ACIDTERROR,
    "am_cannibalize": AM_CANNIBALIZE,
    "am_spheremine": AM_SPHEREMINE,
    "am_potionpitcher": AM_POTIONPITCHER,
    "am_cp_helm": AM_CP_HELM,
    "am_cp_weapon": AM_CP_WEAPON,
    "am_cp_armor": AM_CP_ARMOR,
    "am_cp_shield": AM_CP_SHIELD,
    "am_berserkpitcher": AM_BERSERKPITCHER,
    "pr_kyrie": PR_KYRIE,
    "pr_impositio": PR_IMPOSITIO,
    "pr_suffragium": PR_SUFFRAGIUM,
    "pr_aspersio": PR_ASPERSIO,
    "pr_benedictio": PR_BENEDICTIO,
    "pr_magnus": PR_MAGNUS,
    "pr_lexdivina": PR_LEXDIVINA,
    "pr_turnundead": PR_TURNUNDEAD,
    "pr_lexaeterna": PR_LEXAETERNA,
    "pr_strecovery": PR_STRECOVERY,
    "pr_slowpoison": PR_SLOWPOISON,
    "all_resurrection": ALL_RESURRECTION,
    "pr_sanctuary": PR_SANCTUARY,
    "pr_redemptio": PR_REDEMPTIO,
    "mo_extremityfist": MO_EXTREMITYFIST,
    "mo_investigate": MO_INVESTIGATE,
    "mo_bodyrelocation": MO_BODYRELOCATION,
    "mo_absorbspirits": MO_ABSORBSPIRITS,
    "mo_callspirits": MO_CALLSPIRITS,
    "mo_fingeroffensive": MO_FINGEROFFENSIVE,
    "mo_kitranslation": MO_KITRANSLATION,
    "mo_balkyoung": MO_BALKYOUNG,
    "ht_landmine": HT_LANDMINE,
    "ht_freezingtrap": HT_FREEZINGTRAP,
    "ht_blastmine": HT_BLASTMINE,
    "ht_claymoretrap": HT_CLAYMORETRAP,
    "ht_skidtrap": HT_SKIDTRAP,
    "ht_flasher": HT_FLASHER,
    "ht_shockwave": HT_SHOCKWAVE,
    "ht_sandman": HT_SANDMAN,
    "ht_blitzbeat": HT_BLITZBEAT,
    "ht_detecting": HT_DETECTING,
    "ht_removetrap": HT_REMOVETRAP,
    "ht_springtrap": HT_SPRINGTRAP,
    "ht_phantasmic": HT_PHANTASMIC,
    "ht_power": HT_POWER,
    "ba_frostjoke": BA_FROSTJOKE,
    "ba_musicalstrike": BA_MUSICALSTRIKE,
    "ba_pangvoice": BA_PANGVOICE,
    "dc_scream": DC_SCREAM,
    "dc_throwarrow": DC_THROWARROW,
    "dc_winkcharm": DC_WINKCHARM,
    "lk_spiralpierce": LK_SPIRALPIERCE,
    "lk_headcrush": LK_HEADCRUSH,
    "lk_jointbeat": LK_JOINTBEAT,
    "pa_shieldchain": PA_SHIELDCHAIN,
    "pa_pressure": PA_PRESSURE,
    "hw_ganbantein": HW_GANBANTEIN,
    "hw_gravitation": HW_GRAVITATION,
    "hw_napalmvulcan": HW_NAPALMVULCAN,
    "hw_magiccrasher": HW_MAGICCRASHER,
    "pf_fogwall": PF_FOGWALL,
    "pf_spiderweb": PF_SPIDERWEB,
    "pf_hpconversion": PF_HPCONVERSION,
    "pf_soulchange": PF_SOULCHANGE,
    "pf_mindbreaker": PF_MINDBREAKER,
    "pf_soulburn": PF_SOULBURN,
    "asc_meteorassault": ASC_METEORASSAULT,
    "asc_breaker": ASC_BREAKER,
    "st_fullstrip": ST_FULLSTRIP,
    "ws_carttermination": WS_CARTTERMINATION,
    "cr_aciddemonstration": CR_ACIDDEMONSTRATION,
    "cr_slimpitcher": CR_SLIMPITCHER,
    "cr_fullprotection": CR_FULLPROTECTION,
    "hp_assumptio": HP_ASSUMPTIO,
    "ch_palmstrike": CH_PALMSTRIKE,
    "sn_sharpshooting": SN_SHARPSHOOTING,
    "sn_falconassault": SN_FALCONASSAULT,
    "cg_arrowvulcan": CG_ARROWVULCAN,
    "cg_tarotcard": CG_TAROTCARD,
    "tk_jumpkick": TK_JUMPKICK,
    "gs_fling": GS_FLING,
    "gs_cracker": GS_CRACKER,
    "gs_tripleaction": GS_TRIPLEACTION,
    "gs_bullseye": GS_BULLSEYE,
    "gs_rapidshower": GS_RAPIDSHOWER,
    "gs_desperado": GS_DESPERADO,
    "gs_tracking": GS_TRACKING,
    "gs_disarm": GS_DISARM,
    "gs_piercingshot": GS_PIERCINGSHOT,
    "gs_dust": GS_DUST,
    "gs_fullbuster": GS_FULLBUSTER,
    "gs_spreadattack": GS_SPREADATTACK,
    "gs_grounddrift": GS_GROUNDDRIFT,
    "gs_glitterin": GS_GLITTERIN,
    "nj_kouenka": NJ_KOUENKA,
    "nj_kaensin": NJ_KAENSIN,
    "nj_bakuenryu": NJ_BAKUENRYU,
    "nj_issen": NJ_ISSEN,
    "nj_hyousensou": NJ_HYOUSENSOU,
    "nj_suiton": NJ_SUITON,
    "nj_hyousyouraku": NJ_HYOUSYOURAKU,
    "nj_syuriken": NJ_SYURIKEN,
    "nj_kunai": NJ_KUNAI,
    "nj_huuma": NJ_HUUMA,
    "nj_zenynage": NJ_ZENYNAGE,
    "nj_tatamigaeshi": NJ_TATAMIGAESHI,
    "nj_huujin": NJ_HUUJIN,
    "nj_raigekisai": NJ_RAIGEKISAI,
    "nj_kamaitachi": NJ_KAMAITACHI,
    "nj_kirikage": NJ_KIRIKAGE,
    "nj_kasumikiri": NJ_KASUMIKIRI,
    "sl_alchemist": SL_ALCHEMIST,
    "sl_rogue": SL_ROGUE,
    "sl_barddancer": SL_BARDDANCER,
    "sl_wizard": SL_WIZARD,
    "sl_hunter": SL_HUNTER,
    "sl_knight": SL_KNIGHT,
    "sl_soullinker": SL_SOULLINKER,
    "sl_blacksmith": SL_BLACKSMITH,
    "sl_assasin": SL_ASSASIN,
    "sl_star": SL_STAR,
    "sl_monk": SL_MONK,
    "sl_sage": SL_SAGE,
    "sl_priest": SL_PRIEST,
    "sl_supernovice": SL_SUPERNOVICE,
    "sl_crusader": SL_CRUSADER,
    "sl_high": SL_HIGH,
    "sl_sma": SL_SMA,
    "sl_stin": SL_STIN,
    "sl_stun": SL_STUN,
    "sl_ska": SL_SKA,
    "sl_ske": SL_SKE,
    "sl_swoo": SL_SWOO,
    "sl_kaahi": SL_KAAHI,
    "sl_kaite": SL_KAITE,
    "sl_kaizel": SL_KAIZEL,
    "sl_kaupe": SL_KAUPE,
}
