from enum import Enum
from typing import List
from service.file import File


class PropServer(Enum):
    HP_OFFSET = "hp_offset"
    MAP_OFFSET = "map_offset"
    BG = "bg"
    WOE = "woe"
    PVP = "pvp"
    PVM = "pvm"
    CITY = "city"
    BUFFS = "buffs"


TYPE_MAPS = ["BG", "WoE", "PvP", "PvM", "Cidade"]


class ServersFile(File):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.buffs = {}

    def get_value(self, process_name: str, prop_server: PropServer) -> List[str]:
        return self.read(f"{process_name}:{prop_server.value}")

    def syn_data(self, process_name: str):
        self.buffs = self.get_value(process_name, PropServer.BUFFS)


SERVERS_FILE = ServersFile("servers.json")
