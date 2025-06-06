from functools import reduce
from typing import Any, List
import win32con
import win32api
import time
import ctypes

from config.app import APP_DELAY
from service.config_file import CONFIG_FILE, PropConfig
from service.memory import MEMORY

QT_TO_VK = {
    "Ctrl": win32con.VK_CONTROL,
    "Alt": win32con.VK_MENU,
    "Shift": win32con.VK_SHIFT,
    "Meta": win32con.VK_LWIN,
    "Space": win32con.VK_SPACE,
    "Enter": win32con.VK_RETURN,
}


class Keyboard:
    def press_key(self, key_sequence: str) -> None:
        if not key_sequence:
            return
        vk_codes = self._key_sequence_to_vk(key_sequence)
        [self._key_event(vk_code, False) for vk_code in vk_codes]
        [self._key_event(vk_code, True) for vk_code in vk_codes[::-1]]

    def is_key_pressed(self, vk_codes: List[Any]) -> bool:
        return reduce(
            lambda result, vk_code: result and win32api.GetAsyncKeyState(vk_code) & 0x8000 != 0,
            vk_codes,
            True,
        )

    def _key_event(self, vk_code: Any, is_key_up: bool) -> None:
        time.sleep(APP_DELAY)
        if CONFIG_FILE.get_value(PropConfig.KEYBOARD_TYPE) == "physical":
            action = win32con.KEYEVENTF_KEYUP if is_key_up else 0
            win32api.keybd_event(vk_code, 0, action, 0)
            return
        if CONFIG_FILE.get_value(PropConfig.KEYBOARD_TYPE) == "virtual" and MEMORY.is_valid():
            action = win32con.WM_KEYUP if is_key_up else win32con.WM_KEYDOWN
            ctypes.windll.user32.PostMessageW(MEMORY.get_hwnd(), action, vk_code, 0)

    def _key_sequence_to_vk(self, key_sequence: str) -> List[Any]:
        vk_keys = []
        for key in key_sequence.split("+"):
            key = key.strip()
            vk_keys.append(self._key_to_vk(key))
        return [vk for vk in vk_keys if vk is not None]

    def _key_to_vk(self, key: str) -> Any:
        if key in QT_TO_VK:
            return QT_TO_VK[key]
        if len(key) == 1 and key.isalnum():
            return ord(key.upper())
        if key.startswith("F") and key[1:].isdigit():
            return getattr(win32con, f"VK_{key.upper()}", None)
        return None


KEYBOARD = Keyboard()
