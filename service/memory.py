from typing import Any
from pymem import Pymem
import win32gui
import win32process
import pywintypes

from service.file import SERVERS_FILE


class Memory:
    def __init__(self) -> None:
        self.process = Pymem()
        self.process_name = None
        self.hp_address = None

    def is_valid(self) -> bool:
        return self.process.process_handle is not None

    def update_process(self, name: str, pid: int) -> None:
        self.process.open_process_from_id(pid)
        self.process_name = name
        self.hp_address = self._get_base_address("hp")

    def get_hwnd(self) -> None:
        if not self.is_valid():
            return None
        hwnds = []

        def enum_windows_callback(hwnd: Any, _: Any) -> None:
            pid = self.process.process_id
            try:
                _, window_pid = win32process.GetWindowThreadProcessId(hwnd)
                if window_pid == pid and win32gui.IsWindowVisible(hwnd):
                    hwnds.append(hwnd)
            except pywintypes.error:
                pass

        win32gui.EnumWindows(enum_windows_callback, None)
        return hwnds[0] if hwnds else None

    def _get_base_address(self, base_name: str) -> int:
        hp_address = SERVERS_FILE.read(f"{self.process_name}:{base_name}")
        return int(hp_address, 16)


MEMORY = Memory()
