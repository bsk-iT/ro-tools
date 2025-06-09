import os
import sys


def resource_path(relative_path: str) -> str:
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


PATH_ICON = resource_path("assets/icon/")
PATH_ITEM = resource_path("assets/items/")
PATH_SPAWN_SKILL = resource_path("assets/spawn_skill/")
PATH_BUFF_ASPD = resource_path("assets/buff_aspd/")
PATH_BUFF_ITEM = resource_path("assets/buff_item/")
PATH_BUFF_SKILL = resource_path("assets/buff_skill/")
PATH_JOB_ICON = resource_path("assets/job_icon/")

ICON_KEYBOARD = resource_path(PATH_ICON + "keyboard.png")
ICON_QUICK = resource_path(PATH_ICON + "quick.png")
ICON_MAP = resource_path(PATH_ICON + "map.png")
ICON_REFRESH = resource_path(PATH_ICON + "refresh.png")
ICON_ON = resource_path(PATH_ICON + "on.png")
ICON_OFF = resource_path(PATH_ICON + "off.png")
ICON_DELETE = resource_path(PATH_ICON + "delete.png")

IMG_RED_POTION = resource_path(PATH_ITEM + "red_potion.gif")
IMG_BLUE_POTION = resource_path(PATH_ITEM + "blue_potion.gif")
IMG_YGG = resource_path(PATH_ITEM + "ygg.png")


def get_image(path: str, file_name: str):
    return resource_path(f"{path}{file_name}.png")
