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
        threading.Thread(target=self.monitoring_loop, args=(Item.HP_POTION), daemon=True).start()
        threading.Thread(target=self.monitoring_loop, args=(Item.SP_POTION), daemon=True).start()
        threading.Thread(target=self.monitoring_loop, args=(Item.YGG), daemon=True).start()

    def monitoring_loop(self, item: Item) -> None:
        while self.running:
            if not MEMORY.is_valid():
                time.sleep(APP_MONITORING_DELAY)
                continue
            self.monitoring(item)

    def monitoring(self, item: Item) -> None:
        if not self._is_valid_map(item):
            time.sleep(APP_MONITORING_DELAY)
            return
        key = self.getConfig(item, Action.KEY)
        is_rule_reached = self._ygg_rule(item, key) if item == Item.YGG else self._potion_rule(item, key)
        if is_rule_reached:
            print(f"Potting {item}!")
            KEYBOARD.press_key(key)
            time.sleep(self._get_delay(item))
            return
        time.sleep(APP_MONITORING_DELAY)

    def _potion_rule(self, item: Item, key: str):
        percent = self.getConfig(item, Action.PERCENT)
        ygg_percent = self.getConfig(Item.YGG, Action.HP_PERCENT) if item == Item.HP_POTION else self.getConfig(Item.YGG, Action.SP_PERCENT)
        char_percent = CHAR.hp_percent() if item == Item.HP_POTION else CHAR.sp_percent()
        if not percent or not key or not char_percent or char_percent <= ygg_percent:
            return False
        return char_percent <= percent

    def _ygg_rule(self, item: Item, key: str):
        hp_percent = self.getConfig(item, Action.HP_PERCENT)
        sp_percent = self.getConfig(item, Action.SP_PERCENT)
        key = self.getConfig(item, Action.KEY)
        if not key or (not hp_percent and not sp_percent):
            return False
        return CHAR.hp_percent() <= hp_percent or CHAR.sp_percent() <= sp_percent

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
