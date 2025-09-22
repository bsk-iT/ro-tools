import os
import sys
import warnings

# Suprimir warnings do pygame sobre pkg_resources deprecated
warnings.filterwarnings("ignore", category=UserWarning, module="pygame.pkgdata")

import pygame

pygame.init()
pygame.mixer.init()


def resource_path(relative_path: str) -> str:
    """Get absolute path to resource, works for dev and for PyInstaller"""
    if hasattr(sys, "_MEIPASS"):
        # PyInstaller cria este atributo quando o programa é empacotado
        return os.path.join(getattr(sys, "_MEIPASS"), relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


PATH_ICON = resource_path("assets/icon/")
PATH_ITEM = resource_path("assets/items/")
PATH_SPAWN_SKILL = resource_path("assets/spawn_skill/")
PATH_BUFF_SKILL = resource_path("assets/buff_skill/")
PATH_DEBUFF = resource_path("assets/debuff/")
PATH_JOB_ICON = resource_path("assets/job_icon/")

ICON_KEYBOARD = resource_path(PATH_ICON + "keyboard.png")
ICON_QUICK = resource_path(PATH_ICON + "quick.png")
ICON_MAP = resource_path(PATH_ICON + "map.png")
ICON_REFRESH = resource_path(PATH_ICON + "refresh.png")
ICON_ON = resource_path(PATH_ICON + "on.png")
ICON_OFF = resource_path(PATH_ICON + "off.png")
ICON_DELETE = resource_path(PATH_ICON + "delete.png")
ICON_MOUSE = resource_path(PATH_ICON + "mouse.png")
ICON_SWORD = resource_path(PATH_ICON + "sword.png")
ICON_SHIELD = resource_path(PATH_ICON + "shield.png")
ICON_ARROW_RIGHT = resource_path(PATH_ICON + "arrow_right.png")
ICON_ARROW_DOWN = resource_path(PATH_ICON + "arrow_down.png")
ICON_SONG = resource_path(PATH_ICON + "song.png")
ICON_GITHUB = resource_path(PATH_ICON + "berserk-icon2.png")
ICON_MVP = resource_path(PATH_ICON + "mvp.png")
ICON_TELEPORT = resource_path(PATH_ICON + "teleport.png")
ICON_FLICK = resource_path(PATH_ICON + "flick.png")
ICON_BLOCK_QUAGMIRE = resource_path(PATH_ICON + "block_quagmire.png")
ICON_FOOTPRINT = resource_path(PATH_ICON + "footprint.png")
ICON_TIMER = resource_path(PATH_ICON + "timer.png")
ICON_NOTIFICATION = resource_path(PATH_ICON + "notification.png")
ICON_REPEAT = resource_path(PATH_ICON + "repeat.png")
ICON_CHAT = resource_path(PATH_ICON + "chat.png")

IMG_RED_POTION = resource_path(PATH_ITEM + "red_potion.gif")
IMG_BLUE_POTION = resource_path(PATH_ITEM + "blue_potion.gif")
IMG_YGG = resource_path(PATH_ITEM + "ygg_berry.png")


def get_image(path: str, file_name: str):
    return resource_path(f"{path}{file_name}.png")


def play_sfx(sfx_name):
    from service.config_file import CONFIG_FILE
    
    # Verifica se os sons estão habilitados
    try:
        sounds_enabled = CONFIG_FILE.get_value(['sounds', 'enabled'])
        if not sounds_enabled:
            return
    except:
        # Se não conseguir ler a configuração, assume que está habilitado
        pass
    
    # Apenas permite sons 'on' e 'off'
    if sfx_name not in ['on', 'off']:
        return
        
    try:
        pygame.mixer.music.load(resource_path(f"assets/sfx/{sfx_name}.wav"))
        pygame.mixer.music.play()
    except:
        pass  # Ignora erros de som silenciosamente
