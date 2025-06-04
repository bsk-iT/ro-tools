from abc import abstractmethod
from enum import Enum
import threading
import time

from config.app import APP_MONITORING_DELAY
from service.event import EventType, Resource


class Priority(Enum):
    REALTIME = 4
    HIGH = 3
    NORMAL = 2
    LOW = 1


class BaseEvent:
    def __init__(self, game, name, event_type: EventType, resource: Resource, priority=Priority.LOW):
        self.game = game
        self.name = name
        self.priority = priority
        self.event_type = event_type
        self.resource = resource
        self.running = False

    def start(self):
        threading.Thread(target=self.run, name=self.name, daemon=True).start()

    def stop(self):
        self.running = False

    def run(self):
        self.running = True
        time.sleep(APP_MONITORING_DELAY)
        self.execute_action()
        while self.running and self.check_condition():
            self.execute_action()
        self.running = False

    @abstractmethod
    def check_condition(self) -> bool:
        self.game.sync_game_data()
        return False

    @abstractmethod
    def execute_action(self):
        pass
