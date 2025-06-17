from typing import Any
import pymem
import win32gui
import win32process
import pywintypes

from service.servers_file import CHAT_OFFSET, HP_OFFSET, JOB_OFFSET, MAP_OFFSET, SERVERS_FILE


class Memory:
    def __init__(self) -> None:
        self.process = pymem.Pymem()
        self.process_handle = self.process.process_handle
        self.base_address = None
        self.hp_address = None
        self.map_address = None
        self.job_address = None
        self.chat_address = None

    def is_valid(self) -> bool:
        return self.process.process_handle is not None

    def update_process(self, name: str, pid: int) -> None:
        self.process.open_process_from_id(pid)
        self.sync_addresses(name)

    def sync_addresses(self, name):
        module = pymem.process.module_from_name(self.process.process_handle, name)
        hp_offset = int(SERVERS_FILE.get_value(HP_OFFSET), 16)
        map_offset = int(SERVERS_FILE.get_value(MAP_OFFSET), 16)
        job_offset = int(SERVERS_FILE.get_value(JOB_OFFSET), 16)
        chat_offset = int(SERVERS_FILE.get_value(CHAT_OFFSET), 16)
        self.base_address = module.lpBaseOfDll
        self.hp_address = self.get_address([hp_offset])
        self.map_address = self.get_address([map_offset])
        self.job_address = self.get_address([job_offset])
        self.chat_address = self.get_address([chat_offset])

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

    def get_address(self, offsets, address=None):
        address = self.base_address if address is None else address
        for offset in offsets[:-1]:
            address = self.process.read_uint(address + offset)
        return address + offsets[-1]


MEMORY = Memory()
