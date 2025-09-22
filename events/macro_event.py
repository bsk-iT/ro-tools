import threading
import time
from typing import List

from events.base_event import BaseEvent, Priority

from game.macro import MAX_HOTKEY

from service.config_file import ACTIVE, CONFIG_FILE, DELAY, DELAY_ACTIVE, KEY, KNIFE_KEY, MACRO, MOUSE_CLICK, VIOLIN_KEY
from service.keyboard import KEYBOARD
from service.mouse import MOUSE


class MacroEvent(BaseEvent):

    def __init__(self, game_event, name=MACRO, prop_seq=[MACRO], priority=Priority.REALTIME):
        super().__init__(game_event, name, prop_seq, priority)

    def start(self, macro_id, times = 1):
        print(f"🎯 MACRO DEBUG: Tentando iniciar macro '{macro_id}' (times={times})")
        if self.running:
            print(f"❌ MACRO DEBUG: Já está rodando, ignorando '{macro_id}'")
            return
        print(f"✅ MACRO DEBUG: Iniciando thread para '{macro_id}'")
        self.running = True
        threading.Thread(target=self.run, args=(macro_id, times), name=f"{self.name}:{macro_id}", daemon=True).start()

    def run(self, macro_id, times):
        for _ in range(times):
            self.execute_action(macro_id)

    def execute_action(self, macro_id):
        from gui.app_controller import APP_CONTROLLER

        print(f"🎯 MACRO DEBUG: Executando macro '{macro_id}'")
        job_id = APP_CONTROLLER.get_job_id_by(macro_id)
        print(f"🎯 MACRO DEBUG: Job ID encontrado: '{job_id}' para macro '{macro_id}'")
        
        if not macro_id or not job_id:
            print(f"❌ MACRO DEBUG: Macro ou job_id inválido - macro_id='{macro_id}', job_id='{job_id}'")
            self.running = False
            return
            
        prop_seq = [job_id, *self.prop_seq, macro_id]
        print(f"🎯 MACRO DEBUG: Propriedade sequência: {prop_seq}")
        
        self.execute_delay(prop_seq, f"seq_{0}_{DELAY}", f"seq_{0}_{DELAY_ACTIVE}")
        for index in range(1, MAX_HOTKEY):
            mouse_active = CONFIG_FILE.get_value([*prop_seq, f"seq_{index}_{MOUSE_CLICK}"])
            keyboard_active = CONFIG_FILE.get_value([*prop_seq, f"seq_{index}_{ACTIVE}"])
            print(f"🎯 MACRO DEBUG: seq_{index} - mouse_active={mouse_active}, keyboard_active={keyboard_active}")
            
            if not keyboard_active and not mouse_active:
                break
            if "song" in macro_id:
                self._swap_weapon(prop_seq, VIOLIN_KEY)
            if mouse_active:
                MOUSE.click()
            else:
                key = CONFIG_FILE.get_value([*prop_seq, f"seq_{index}_{KEY}"])
                KEYBOARD.press_key(key)
            self.execute_delay(prop_seq, f"seq_{index}_{DELAY}", f"seq_{index}_{DELAY_ACTIVE}")
            if "song" in macro_id:
                self._swap_weapon(prop_seq, KNIFE_KEY)
        self.running = False

    def _swap_weapon(self, prop_seq, weapon_key):
        key = CONFIG_FILE.get_value([*prop_seq, weapon_key])
        KEYBOARD.press_key(key)
        time.sleep(0.12)

    def execute_delay(self, prop_seq: List[str], delay_key, active_key) -> float:
        delay_item = CONFIG_FILE.get_value([*prop_seq, delay_key])
        delay_active = CONFIG_FILE.get_value([*prop_seq, active_key])
        delay = delay_item if (delay_active and delay_item) else 0.1
        time.sleep(delay)
        return delay
