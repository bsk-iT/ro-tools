import threading
import time
from typing import List
from config.app import APP_MONITORING_DELAY
from events.auto_antibot_detector import AutoAntibotDetector
from events.auto_competitive_detector import AutoCompetitiveDetector
from events.auto_element import AutoElement
from events.auto_halter_lead import AutoHalterLead
from events.auto_item_buff import AutoItemBuff
from events.auto_item_debuff import AutoItemDebuff
from events.auto_pot_hp import AutoPotHP
from events.auto_pot_sp import AutoPotSP
from events.auto_teleport import AutoTeleport
from events.auto_ygg import AutoYgg
from events.base_event import BaseEvent
from events.skill_buff import SkillBuff
from events.skill_equip import SkillEquip
from game.char import Char


class GameEvent:
    def __init__(self):
        self.char = Char()
        
        # Detectores de proteção com prioridade máxima
        self.antibot_detector = AutoAntibotDetector(self)
        self.competitive_detector = AutoCompetitiveDetector(self)
        
        self.events_item: List[BaseEvent] = [
            AutoPotHP(self),
            AutoPotSP(self),
            AutoYgg(self),
            AutoItemBuff(self),
            AutoItemDebuff(self),
            AutoElement(self),
            AutoHalterLead(self),
            AutoTeleport(self)
        ]
        self.events_skill: List[BaseEvent] = [SkillBuff(self), SkillEquip(self)]
        self.running = False

    def start(self):
        # Inicia os detectores de proteção primeiro
        self.antibot_detector.start()
        self.competitive_detector.start()
        threading.Thread(target=self.run, name="event_controller", daemon=True).start()

    def stop(self):
        self.running = False
        time.sleep(0.2)
        
        # Para os detectores de proteção
        self.antibot_detector.stop()
        self.competitive_detector.stop()
        
        [event.stop() for event in self.events_item]
        [event.stop() for event in self.events_skill]
        
    def stop_all_events(self):
        """Para todos os eventos (usado pelo detector de antibot)"""
        [event.stop() for event in self.events_item]
        [event.stop() for event in self.events_skill]
        print("🛑 Todos os eventos foram parados pelo detector de antibot")

    def run(self):
        self.running = True
        while self.running:
            self.sync_game_data()
            self.monitoring(self.events_item)
            self.monitoring(self.events_skill)
            time.sleep(APP_MONITORING_DELAY)
        self.running = False

    def monitoring(self, events: List[BaseEvent]):
        events_allowed = [event for event in events if event.check_condition()]
        if not events_allowed:
            [event.stop() for event in events]
            return
        max_priority = max(event.priority.value for event in events_allowed)
        for event in events_allowed:
            is_event_priority = event.priority.value == max_priority
            if is_event_priority and not event.running:
                event.start()
            if not is_event_priority:
                event.stop()

    def sync_game_data(self):
        self.char.update()


GAME_EVENT = GameEvent()
