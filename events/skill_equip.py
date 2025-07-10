from events.base_event import BaseEvent, Priority

from events.macro_event import MacroEvent
from service.config_file import CONFIG_FILE, HALTER_LEAD, MACRO, SKILL_EQUIP, WAITING


class SkillEquip(BaseEvent):

    def __init__(self, game_event, name=f"{SKILL_EQUIP}", prop_seq=[SKILL_EQUIP], priority=Priority.REALTIME):
        super().__init__(game_event, name, prop_seq, priority)
        self.macro_event = MacroEvent(self.game_event)

    def check_condition(self) -> bool:
        from gui.app_controller import APP_CONTROLLER

        super().check_condition()
        if HALTER_LEAD in self.game_event.char.item_buffs:
            return False
        (job_id, buff_id, _) = self.game_event.char.next_skill_buff_to_use(APP_CONTROLLER.job_equip_skills, self.prop_seq)
        if buff_id is None:
            return False
        is_valid_map = CONFIG_FILE.is_valid_map(self.game_event, [job_id, *self.prop_seq])
        is_blocked_in_city = CONFIG_FILE.is_blocked_in_city(self.game_event, [APP_CONTROLLER.job.id, *self.prop_seq])
        is_block_chat_waiting = CONFIG_FILE.is_block_chat_open(self.game_event, WAITING)
        return is_valid_map and not is_blocked_in_city and not is_block_chat_waiting

    def execute_action(self):
        from gui.app_controller import APP_CONTROLLER

        super().execute_action()
        (job_id, buff_id, _) = self.game_event.char.next_skill_buff_to_use(APP_CONTROLLER.job_equip_skills, self.prop_seq)
        if buff_id is None:
            return
        macro_id = CONFIG_FILE.get_value([job_id, *self.prop_seq, buff_id, MACRO])
        self.macro_event.start(macro_id)
