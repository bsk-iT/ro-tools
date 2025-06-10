from abc import abstractmethod
from enum import Enum
import threading
import time
from typing import List

from service.config_file import SKILL_SPAWNNER


class Priority(Enum):
    REALTIME = 4
    HIGH = 3
    NORMAL = 2
    LOW = 1


class BaseEvent:
    def __init__(self, game, name, prop_seq: List[str], priority=Priority.LOW):
        self.game = game
        self.name = name
        self.priority = priority
        self.prop_seq = prop_seq
        self.running = False

    def start(self):
        threading.Thread(target=self.run, name=self.name, daemon=True).start()

    def stop(self):
        self.running = False

    def run(self):
        self.running = True
        if self.name not in [SKILL_SPAWNNER]:
            time.sleep(0.1)
        self.execute_action()
        while self.running and self.check_condition():
            self.execute_action()
        self.running = False

    @abstractmethod
    def check_condition(self) -> bool:
        if self.name not in [SKILL_SPAWNNER]:
            self.game.sync_game_data()
        return False

    @abstractmethod
    def execute_action(self):
        pass
