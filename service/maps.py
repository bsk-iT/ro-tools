from typing import List
from service.file import MAPS_FILE


class Maps:

    def list_by_type(self, map_type: str) -> List[str]:
        return MAPS_FILE.read(map_type)


MAPS = Maps()
