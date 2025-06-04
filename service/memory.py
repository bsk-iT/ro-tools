from typing import Any
import pymem
import win32gui
import win32process
import pywintypes

from service.file import SERVERS_FILE


class Memory:
    def __init__(self) -> None:
        self.process = pymem.Pymem()
        self.process_name = None
        self.base_address = None

    def is_valid(self) -> bool:
        return self.process.process_handle is not None

    def update_process(self, name: str, pid: int) -> None:
        self.process.open_process_from_id(pid)
        self.process_name = name
        module = pymem.process.module_from_name(self.process.process_handle, name)
        self.base_address = module.lpBaseOfDll

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

    def get_address(self, offsets):
        address = self.base_address
        for offset in offsets[:-1]:
            address = self.process.read_uint(address + offset)
        return address + offsets[-1]


MEMORY = Memory()
