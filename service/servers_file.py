from typing import List
from service.file import File

# Properties
HP_OFFSET = "hp_offset"
MAP_OFFSET = "map_offset"
BG = "bg"
WOE = "woe"
PVP = "pvp"
PVM = "pvm"
CITY = "city"
BUFF_SKILL = "buff_skill"
BUFF_ASPD = "buff_aspd"
BUFF_ITEM = "buff_item"


TYPE_MAPS = ["BG", "WoE", "PvP", "PvM", "Cidade"]


class ServersFile(File):
    def __init__(self, file_path):
        super().__init__(file_path)

    def get_value(self, prop: str) -> List[str]:
        from gui.app_controller import APP_CONTROLLER

        return self.read(f"{APP_CONTROLLER.process_name}:{prop}")


SERVERS_FILE = ServersFile("servers.json")
