import threading
import time
from typing import Any

from config.action import Action
from config.app import APP_ACTION_DELAY, APP_MONITORING_DELAY
from db.char import CHAR
from db.item import Item
from service.file import CONFIG_FILE
from service.keyboard import KEYBOARD
from service.memory import MEMORY
from service.maps import MAPS


class AutoPot:

    def __init__(self) -> None:
        self.running = False

    def run(self) -> None:
        self.running = True
        threading.Thread(target=self.monitoring_loop, args=(CHAR.hp_percent, Item.HP_POTION), daemon=True).start()
        threading.Thread(target=self.monitoring_loop, args=(CHAR.sp_percent, Item.SP_POTION), daemon=True).start()

    def monitoring_loop(self, char_percent: int, item: Item) -> None:
        while self.running:
            if not MEMORY.is_valid():
                time.sleep(APP_MONITORING_DELAY)
                continue
            self.monitoring(char_percent, item)

    def monitoring(self, char_percent: Any, item: Item) -> None:
        if not self._is_valid_map(item):
            time.sleep(APP_MONITORING_DELAY)
            return
        percent = self.getConfig(item, Action.PERCENT)
        key = self.getConfig(item, Action.KEY)
        if not percent or not key:
            time.sleep(APP_MONITORING_DELAY)
            return
        if char_percent() < percent:
            print(f"Potting {item}!")
            KEYBOARD.press_key(key)
            time.sleep(self._get_delay(item))
            return
        time.sleep(APP_MONITORING_DELAY)

    def _get_delay(self, item: Item) -> float:
        delay_item = self.getConfig(item, Action.DELAY)
        delay_item = delay_item if self.getConfig(item, Action.DELAY_ACTIVE) and delay_item else APP_ACTION_DELAY
        return delay_item

    def _is_valid_map(self, item: Item) -> bool:
        map_active = self.getConfig(item, Action.MAP_ACTIVE)
        if not map_active:
            return True
        map_type = self.getConfig(item, Action.MAP)
        return CHAR.current_map() in MAPS.list_by_type(map_type)

    def stop(self) -> None:
        self.running = False

    def getConfigKey(self, item: Item, action: Action) -> str:
        return f"auto_pot:{item.value}:{action.value}"

    def getConfig(self, item: Item, action: Action = None) -> Any:
        return CONFIG_FILE.read(self.getConfigKey(item, action))


AUTO_POT = AutoPot()
