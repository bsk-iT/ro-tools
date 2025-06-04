import os
import sys


def resource_path(relative_path: str) -> str:
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


PATH_ICON = resource_path("assets/icon/")
PATH_ITEM = resource_path("assets/items/")

ICON_KEYBOARD = resource_path(PATH_ICON + "keyboard.png")
ICON_QUICK = resource_path(PATH_ICON + "quick.png")
ICON_MAP = resource_path(PATH_ICON + "map.png")
ICON_REFRESH = resource_path(PATH_ICON + "refresh.png")
ICON_ON = resource_path(PATH_ICON + "on.png")
ICON_OFF = resource_path(PATH_ICON + "off.png")

IMG_RED_POTION = resource_path(PATH_ITEM + "red_potion.gif")
IMG_BLUE_POTION = resource_path(PATH_ITEM + "blue_potion.gif")
IMG_YGG = resource_path(PATH_ITEM + "ygg.png")
