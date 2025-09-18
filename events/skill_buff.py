import time
from events.base_event import BaseEvent, Priority
from util.antibot import has_antibot, check_antibot_and_log
from util.competitive import has_competitive_instance, check_competitive_and_log

from service.config_file import CONFIG_FILE, HALTER_LEAD, KEY, SKILL_BUFF, WAITING
from service.keyboard import KEYBOARD


class SkillBuff(BaseEvent):

    def __init__(self, game_event, name=f"{SKILL_BUFF}", prop_seq=[SKILL_BUFF], priority=Priority.HIGH):
        super().__init__(game_event, name, prop_seq, priority)

    def check_condition(self) -> bool:
        from gui.app_controller import APP_CONTROLLER

        super().check_condition()
        
        # Verifica se o antibot está ativo
        if check_antibot_and_log(self.game_event, "SkillBuff"):
            return False
            
        # Verifica se está em instância competitiva
        if check_competitive_and_log(self.game_event, "SkillBuff"):
            return False
            
        if HALTER_LEAD in self.game_event.char.item_buffs:
            return False
        (job_id, buff_id, _) = self.game_event.char.next_skill_buff_to_use(APP_CONTROLLER.job_buff_skills, self.prop_seq)
        if buff_id is None:
            return False
        is_valid_map = CONFIG_FILE.is_valid_map(self.game_event, [job_id, *self.prop_seq])
        is_blocked_in_city = CONFIG_FILE.is_blocked_in_city(self.game_event, [APP_CONTROLLER.job.id, *self.prop_seq])
        is_block_chat_waiting = CONFIG_FILE.is_block_chat_open(self.game_event, WAITING)
        return is_valid_map and not is_blocked_in_city and not is_block_chat_waiting

    def execute_action(self):
        from gui.app_controller import APP_CONTROLLER

        super().execute_action()
        (job_id, buff_id, _) = self.game_event.char.next_skill_buff_to_use(APP_CONTROLLER.job_buff_skills, self.prop_seq)
        if buff_id is None:
            return
        self.game_event.char.index_last_time_buff[buff_id] = time.time()
        base_prop_seq = [job_id, *self.prop_seq, buff_id]
        KEYBOARD.press_key(CONFIG_FILE.get_value([*base_prop_seq, KEY]))
        time.sleep(CONFIG_FILE.get_delay(base_prop_seq, 0.2))
