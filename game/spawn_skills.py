from config.icon import PATH_SPAWN_SKILL, get_image


class SpawnSkill:
    def __init__(self, _id, name, is_clicked=True):
        self.id = _id
        self.name = name
        self.is_clicked = is_clicked
        self.icon = get_image(PATH_SPAWN_SKILL, self.id)


# Novice
ATTACK_1 = SpawnSkill("ATTACK_1", "Skill de Ataque 1")
ATTACK_2 = SpawnSkill("ATTACK_2", "Skill de Ataque 2")
ATTACK_3 = SpawnSkill("ATTACK_3", "Skill de Ataque 3")
ATTACK_4 = SpawnSkill("ATTACK_4", "Skill de Ataque 4")
NV_FIRSTAID = SpawnSkill("NV_FIRSTAID", "Primeiros Socorros")

# Swordman
SM_BASH = SpawnSkill("SM_BASH", "Golpe Fulminante")
SM_PROVOKE = SpawnSkill("SM_PROVOKE", "Provocar")

# Mage
MG_FIREBOLT = SpawnSkill("MG_FIREBOLT", "Lança de Fogo")
MG_FIREBALL = SpawnSkill("MG_FIREBALL", "Bolas de Fogo")
MG_FIREWALL = SpawnSkill("MG_FIREWALL", "Barreira de Fogo")
MG_COLDBOLT = SpawnSkill("MG_COLDBOLT", "Lanças de Gelo")
MG_FROSTDIVER = SpawnSkill("MG_FROSTDIVER", "Rajada Congelante")
MG_LIGHTNINGBOLT = SpawnSkill("MG_LIGHTNINGBOLT", "Relâmpago")
MG_THUNDERSTORM = SpawnSkill("MG_THUNDERSTORM", "Tempestade de Raios")
MG_NAPALMBEAT = SpawnSkill("MG_NAPALMBEAT", "Ataque Espiritual")
MG_SOULSTRIKE = SpawnSkill("MG_SOULSTRIKE", "Espíritos Anciões")
MG_SAFETYWALL = SpawnSkill("MG_SAFETYWALL", "Escudo Mágico")
MG_STONECURSE = SpawnSkill("MG_STONECURSE", "Petrificar")

# Thief
TF_SPRINKLESAND = SpawnSkill("TF_SPRINKLESAND", "Petrificar")
TF_BACKSLIDING = SpawnSkill("TF_BACKSLIDING", "Recuar", False)
TF_PICKSTONE = SpawnSkill("TF_PICKSTONE", "Procurar Pedras", False)
TF_THROWSTONE = SpawnSkill("TF_THROWSTONE", "Arremessar Pedra")
TF_POISON = SpawnSkill("TF_POISON", "Envenenar")
TF_DETOXIFY = SpawnSkill("TF_DETOXIFY", "Desintoxicar")
TF_STEAL = SpawnSkill("TF_STEAL", "Furto")

# Merchant
MC_MAMMONITE = SpawnSkill("MC_MAMMONITE", "Mammonita")
MC_CARTREVOLUTION = SpawnSkill("MC_CARTREVOLUTION", "Cavalo-de-Pau")

# Acolyte
AL_BLESSING = SpawnSkill("AL_BLESSING", "Bênção")
AL_HEAL = SpawnSkill("AL_HEAL", "Curar")
AL_CURE = SpawnSkill("AL_CURE", "Medicar")
AL_INCAGI = SpawnSkill("AL_INCAGI", "Aumentar Agilidade")
AL_DECAGI = SpawnSkill("AL_DECAGI", "Diminuir Agilidade")
AL_PNEUMA = SpawnSkill("AL_PNEUMA", "Escudo Sagrado")
AL_HOLYWATER = SpawnSkill("AL_HOLYWATER", "Aqua Benedicta", False)
AL_HOLYLIGHT = SpawnSkill("AL_HOLYLIGHT", "Luz Divina")

# Archer
AC_DOUBLE = SpawnSkill("AC_DOUBLE", "Rajada de Flechas")
AC_SHOWER = SpawnSkill("AC_SHOWER", "Chuva de Flechas")
AC_CHARGEARROW = SpawnSkill("AC_CHARGEARROW", "Disparo Violento")

# Knight
KN_BOWLINGBASH = SpawnSkill("KN_BOWLINGBASH", "Impacto de Tyr")
KN_PIERCE = SpawnSkill("KN_PIERCE", "Perfurar")
KN_SPEARSTAB = SpawnSkill("KN_SPEARSTAB", "Estocada")
KN_SPEARBOOMERANG = SpawnSkill("KN_SPEARBOOMERANG", "Lança Bumerangue")
KN_BRANDISHSPEAR = SpawnSkill("KN_BRANDISHSPEAR", "Brandir Lança")
KN_CHARGEATK = SpawnSkill("KN_CHARGEATK", "Avanço Ofensivo")
KN_CHARGEATK = SpawnSkill("KN_CHARGEATK", "Avanço Ofensivo")

# Crusader
CR_HOLYCROSS = SpawnSkill("CR_HOLYCROSS", "Crux Divinum")
CR_GRANDCROSS = SpawnSkill("CR_GRANDCROSS", "Crux Magnum")
CR_GRANDCROSS = SpawnSkill("CR_DEVOTION", "Redenção")
# AL_HEAL
# AL_CURE
CR_SHIELDCHARGE = SpawnSkill("CR_SHIELDCHARGE", "Punição Divina")
CR_SHIELDBOOMERANG = SpawnSkill("CR_SHIELDBOOMERANG", "Escudo Bumerangue")
CR_PROVIDENCE = SpawnSkill("CR_PROVIDENCE", "Divina Providência")

# Wizard
WZ_EARTHSPIKE = SpawnSkill("WZ_EARTHSPIKE", "Coluna de Pedra")
WZ_QUAGMIRE = SpawnSkill("WZ_QUAGMIRE", "Pântano dos Mortos")
WZ_HEAVENDRIVE = SpawnSkill("WZ_HEAVENDRIVE", "Fúria da Terra")
WZ_FROSTNOVA = SpawnSkill("WZ_FROSTNOVA", "Congelar", False)
WZ_ICEWALL = SpawnSkill("WZ_ICEWALL", "Barreira de Gelo")
WZ_STORMGUST = SpawnSkill("WZ_STORMGUST", "Nevasca")
WZ_WATERBALL = SpawnSkill("WZ_WATERBALL", "Esfera d'Água")
WZ_METEOR = SpawnSkill("WZ_METEOR", "Chuva de Meteoros")
WZ_SIGHTRASHER = SpawnSkill("WZ_SIGHTRASHER", "Supernova", False)
WZ_FIREPILLAR = SpawnSkill("WZ_FIREPILLAR", "Coluna de Fogo")
WZ_JUPITEL = SpawnSkill("WZ_JUPITEL", "Trovão de Júpiter")
WZ_VERMILION = SpawnSkill("WZ_VERMILION", "Ira de Thor")

# Sage
SA_ABRACADABRA = SpawnSkill("SA_ABRACADABRA", "Abracadabra", False)
SA_VIOLENTGALE = SpawnSkill("SA_VIOLENTGALE", "Furacão")
SA_VOLCANO = SpawnSkill("SA_VOLCANO", "Vulcão")
SA_DELUGE = SpawnSkill("SA_DELUGE", "Dilúvio")
SA_FLAMELAUNCHER = SpawnSkill("SA_FLAMELAUNCHER", "Encantar com Chama")
SA_FROSTWEAPON = SpawnSkill("SA_FROSTWEAPON", "Encantar com Geada")
SA_LIGHTNINGLOADER = SpawnSkill("SA_LIGHTNINGLOADER", "Encantar com Ventania")
SA_SEISMICWEAPON = SpawnSkill("SA_SEISMICWEAPON", "Encantar com Terremoto")
# WZ_EARTHSPIKE
# WZ_HEAVENDRIVE
SA_SPELLBREAKER = SpawnSkill("SA_SPELLBREAKER", "Desconcentrar")
SA_DISPELL = SpawnSkill("SA_DISPELL", "Desencantar")
SA_LANDPROTECTOR = SpawnSkill("SA_LANDPROTECTOR", "Proteger Terreno")
SA_ELEMENT = SpawnSkill("SA_ELEMENT", "Mudança Elemental")

# Assassin
AS_SONICBLOW = SpawnSkill("AS_SONICBLOW", "Lâminas Destruidoras")
AS_GRIMTOOTH = SpawnSkill("AS_GRIMTOOTH", "Tocaia")
AS_ENCHANTPOISON = SpawnSkill("AS_ENCHANTPOISON", "Envenenar Arma")
AS_VENOMDUST = SpawnSkill("AS_VENOMDUST", "Névoa Tóxica")
AS_SPLASHER = SpawnSkill("AS_SPLASHER", "Explosão Tóxica")
AS_VENOMKNIFE = SpawnSkill("AS_VENOMKNIFE", "Faca Envenenada")

# Rogue
RG_BACKSTAP = SpawnSkill("RG_BACKSTAP", "Apunhalar")
RG_RAID = SpawnSkill("RG_RAID", "Ataque Surpresa", False)
RG_INTIMIDATE = SpawnSkill("RG_INTIMIDATE", "Rapto")
RG_STEALCOIN = SpawnSkill("RG_STEALCOIN", "Afanar")
RG_STRIPARMOR = SpawnSkill("RG_STRIPARMOR", "Remover Armadura")
RG_STRIPHELM = SpawnSkill("RG_STRIPHELM", "Remover Capacete")
RG_STRIPSHIELD = SpawnSkill("RG_STRIPSHIELD", "Remover Escudo")
RG_STRIPWEAPON = SpawnSkill("RG_STRIPWEAPON", "Remover Arma")
# HT_REMOVETRAP
# AC_DOUBLE
RG_CLOSECONFINE = SpawnSkill("RG_CLOSECONFINE", "Confinamento")

# Blacksmith
BS_HAMMERFALL = SpawnSkill("BS_HAMMERFALL", "Martelo de Thor")
BS_REPAIRWEAPON = SpawnSkill("BS_REPAIRWEAPON", "Consertar Armas")
BS_GREED = SpawnSkill("BS_GREED", "Ganância")

# Alchemist
AM_DEMONSTRATION = SpawnSkill("AM_DEMONSTRATION", "Fogo Grego")
AM_ACIDTERROR = SpawnSkill("AM_ACIDTERROR", "Terror Ácido")
AM_CANNIBALIZE = SpawnSkill("AM_CANNIBALIZE", "Criar Monstro Planta")
AM_SPHEREMINE = SpawnSkill("AM_SPHEREMINE", "Criar Esfera Marinha")
AM_POTIONPITCHER = SpawnSkill("AM_POTIONPITCHER", "Arremessar Poção")
AM_CP_HELM = SpawnSkill("AM_CP_HELM", "Revestir Capacete")
AM_CP_WEAPON = SpawnSkill("AM_CP_WEAPON", "Revestir Arma")
AM_CP_ARMOR = SpawnSkill("AM_CP_ARMOR", "Revestir Armadura")
AM_CP_SHIELD = SpawnSkill("AM_CP_SHIELD", "Revestir Escudo")
AM_BERSERKPITCHER = SpawnSkill("AM_BERSERKPITCHER", "Arremessar Poção da Fúria Selvagem")

# Hunter
HT_REMOVETRAP = SpawnSkill("HT_REMOVETRAP", "Remover Armadilha")
