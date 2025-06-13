from abc import abstractmethod
from enum import Enum
import threading
import time
from typing import List


class Priority(Enum):
    REALTIME = 4
    HIGH = 3
    NORMAL = 2
    LOW = 1


class BaseEvent:
    def __init__(self, game_event, name, prop_seq: List[str], priority=Priority.LOW):
        self.game_event = game_event
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
        time.sleep(0.1)
        self.execute_action()
        while self.running and self.check_condition():
            self.execute_action()
        self.running = False

    @abstractmethod
    def check_condition(self) -> bool:
        self.game_event.sync_game_data()
        return False

    @abstractmethod
    def execute_action(self):
        pass
