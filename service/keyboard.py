import time
import win32api
import win32con
import ctypes
from typing import List, Any, Set

from config.app import APP_DELAY
from service.config_file import CONFIG_FILE, DRIVE, KEYBOARD_TYPE, PHYSICAL, VIRTUAL
from service.memory import MEMORY
from util.widgets import is_interception_available

QT_TO_VK = {
    "Ctrl": win32con.VK_CONTROL,
    "Alt": win32con.VK_MENU,
    "Shift": win32con.VK_SHIFT,
    "Meta": win32con.VK_LWIN,
    "Space": win32con.VK_SPACE,
    "Enter": win32con.VK_RETURN,
}


class Keyboard:
    def __init__(self):
        self._check_interception()
        self._pressed_keys = {}
        self._simulating_keys: Set[int] = set()
        if is_interception_available():
            from interception import Interception

            self._interception = Interception()
            self._keyboard_id = self._interception.keyboard

    def _check_interception(self):
        try:
            from interception import Interception

            self.interception_avaliable = True
        except Exception as e:
            self.interception_avaliable = False

    def is_simulating_key(self, key: str) -> bool:
        vk_code = self._key_to_vk(key)
        return vk_code in self._simulating_keys if vk_code is not None else False

    def press_key(self, key_sequence: str) -> None:
        if not key_sequence:
            return
        vk_codes = self._key_sequence_to_vk(key_sequence)
        for vk in vk_codes:
            self._key_event(vk, False)
        for vk in reversed(vk_codes):
            self._key_event(vk, True)

    def add_pressed_key(self, key_sequence: str) -> bool:
        if not key_sequence:
            return
        vk_codes = self._key_sequence_to_vk(key_sequence)
        now = time.time()
        for vk in vk_codes:
            self._pressed_keys[vk] = now

    def was_key_pressed_recently(self, key_sequence: str, threshold: float = 0.5) -> bool:
        if not key_sequence:
            return False
        vk_codes = self._key_sequence_to_vk(key_sequence)
        now = time.time()
        return any(vk in self._pressed_keys and now - self._pressed_keys[vk] <= threshold for vk in vk_codes)

    def _key_event(self, vk_code: Any, is_key_up: bool) -> None:
        time.sleep(APP_DELAY)
        keyboard_type = CONFIG_FILE.get_value([KEYBOARD_TYPE])

        if keyboard_type == PHYSICAL:
            action = win32con.KEYEVENTF_KEYUP if is_key_up else 0
            win32api.keybd_event(vk_code, 0, action, 0)
        elif keyboard_type == VIRTUAL and MEMORY.is_valid():
            action = win32con.WM_KEYUP if is_key_up else win32con.WM_KEYDOWN
            ctypes.windll.user32.PostMessageW(MEMORY.get_hwnd(), action, vk_code, 0)
        elif keyboard_type == DRIVE:
            if not is_key_up:
                self._simulating_keys.add(vk_code)
            self._send_interception(vk_code, is_key_up)
            if is_key_up:
                self._simulating_keys.discard(vk_code)

    def _send_interception(self, vk_code: int, is_key_up: bool) -> None:
        from interception import KeyStroke, KeyFlag

        scan_code = ctypes.windll.user32.MapVirtualKeyW(vk_code, 0)
        if scan_code == 0:
            return

        flag = KeyFlag.KEY_UP if is_key_up else KeyFlag.KEY_DOWN
        stroke = KeyStroke(scan_code, flag)
        self._interception.send(self._keyboard_id, stroke)

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
