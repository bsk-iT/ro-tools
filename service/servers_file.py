from typing import List
from service.file import File

# Properties
HP_OFFSET = "hp_offset"
X_POS_OFFSET = "x_pos_offset"
MAP_OFFSET = "map_offset"
JOB_OFFSET = "job_offset"
CHAT_OFFSET = "chat_offset"
ENTITY_LIST_OFFSET = "entity_list_offset"
ABRACADABRA_ADDRESS = "abracadabra_address"
BG = "bg"
WOE = "woe"
PVP = "pvp"
PVM = "pvm"
CITY = "city"
SKILL_BUFF = "skill_buff"
ITEM_BUFF = "item_buff"
STATUS_DEBUFF = "status_debuff"
LINKS = "links"
VOTE = "vote"
NAME = "name"
URL = "url"
TYPE = "type"


TYPE_MAPS = ["BG", "WoE", "PvP", "PvM"]


class ServersFile(File):
    def __init__(self, file_path):
        super().__init__(file_path)

    def get_value(self, prop: str) -> List[str]:
        from gui.app_controller import APP_CONTROLLER

        return self.read(f"{APP_CONTROLLER.process_name}:{prop}")


SERVERS_FILE = ServersFile("servers.json")
