import math
import os

from game.buff import QUAGMIRE, Buff
from game.jobs import JOB_MAP, Job
from gui.app_controller import APP_CONTROLLER
from service.config_file import AUTO_ELEMENT, BLOCK_QUAGMIRE, CONFIG_FILE, DEBUG_ACTIVE, ITEM_BUFF, MOB_IDS, MOVIMENT_CELLS, USE_MOVIMENT
from service.memory import MEMORY
from service.offsets import Offsets
from service.servers_file import NAME, SKILL_BUFF, SERVERS_FILE, STATUS_DEBUFF
from util.number import calculate_percent

MAX_ENTITY = 50


class Char:

    def __init__(self):
        self.update()

    def reset(self):
        self.current_map = ""
        self.job_id = 0
        self.hp = 0
        self.hp_max = 0
        self.hp_percent = 0
        self.sp = 0
        self.sp_max = 0
        self.sp_percent = 0
        self.chat_bar_enabled = False
        self.raw_buffs = []
        self.buffs = []
        self.skill_buffs = []
        self.item_buffs = []
        self.status_debuff = []
        self.entity_list = []
        self.job = None
        self.position = (0, 0)
        self.index_last_position_buff = {}
        self.abracadabra_skill = None

    def update(self):
        try:
            self.hp = 0 if MEMORY.hp_address == 0x0 else MEMORY.process.read_int(MEMORY.hp_address)
            self.hp_max = 0 if MEMORY.hp_address == 0x0 else MEMORY.process.read_int(MEMORY.hp_address + Offsets.MAX_HP)
            self.hp_percent = calculate_percent(self.hp, self.hp_max)
            self.sp = 0 if MEMORY.hp_address == 0x0 else MEMORY.process.read_int(MEMORY.hp_address + Offsets.SP)
            self.sp_max = 0 if MEMORY.hp_address == 0x0 else MEMORY.process.read_int(MEMORY.hp_address + Offsets.MAX_SP)
            self.sp_percent = calculate_percent(self.sp, self.sp_max)
            self.current_map = "" if MEMORY.map_address == 0x0 else MEMORY.process.read_string(MEMORY.map_address)
            self.job_id = None if MEMORY.job_address == 0x0 else MEMORY.process.read_int(MEMORY.job_address)
            self.position = self._get_position()
            self.raw_buffs = self._get_buffs()
            self.buffs = self._get_id_buffs_all()
            self.skill_buffs = self._get_id_buffs(SKILL_BUFF)
            self.item_buffs = self._get_id_buffs(ITEM_BUFF)
            self.status_debuff = self._get_id_buffs(STATUS_DEBUFF)
            self.job = JOB_MAP.get(self.job_id, self.job_id)
            self.abracadabra_skill = None if MEMORY.abracadabra_address == 0x0 else MEMORY.process.read_int(MEMORY.abracadabra_address)
            self.chat_bar_enabled = False if MEMORY.chat_address == 0x0 else MEMORY.process.read_bool(MEMORY.chat_address)
            self.monitoring_job_change_gui()
            self.entity_list = self._get_entity_list()
            if CONFIG_FILE.read(DEBUG_ACTIVE):
                APP_CONTROLLER.debug.emit(self.__str__())
        except BaseException:
            self.reset()

    def _get_position(self):
        if MEMORY.x_pos_address == 0x0:
            return (0, 0)
        return (MEMORY.process.read_int(MEMORY.x_pos_address), MEMORY.process.read_int(MEMORY.x_pos_address + Offsets.Y_POSITION))

    def _get_entity_list(self):
        entities = []
        if MEMORY.entity_list_address == 0x0:
            return entities
        entity_count = 0
        try:
            offset_base = MEMORY.process.read_uint(MEMORY.entity_list_address)
            world = MEMORY.process.read_uint(offset_base + Offsets.WORLD)
            entity_list = MEMORY.process.read_uint(world + Offsets.ENTITY_LIST)
            prev_entity = MEMORY.process.read_uint(entity_list + Offsets.PREV_ENTITY)
            entity = MEMORY.process.read_uint(prev_entity + Offsets.NEXT_ENTITY)
            while entity != 0 and entity_count <= MAX_ENTITY:
                mob_id = MEMORY.process.read_uint(entity + Offsets.ENTITY_ID)
                x_pos = MEMORY.process.read_uint(entity + Offsets.ENTITY_POS_X)
                y_pos = MEMORY.process.read_uint(entity + Offsets.ENTITY_POS_Y)
                sprite_name = ""
                distance = 0
                try:
                    sprite_res = MEMORY.process.read_uint(entity + Offsets.ENTITY_SPRITE_RES)
                    sprite_name = MEMORY.process.read_string(sprite_res + Offsets.SPRITE_NAME)
                    sprite_name = sprite_name.strip("\\").replace(".spr", "")
                    sprite_name = sprite_name.replace("_", " ").title()
                    distance = 0 if MEMORY.x_pos_address == 0x0 else math.hypot(x_pos - self.position[0], y_pos - self.position[1])
                    entities.append((mob_id, sprite_name, distance))
                except:
                    pass
                prev_entity = MEMORY.process.read_uint(prev_entity + Offsets.PREV_ENTITY)
                entity = MEMORY.process.read_uint(prev_entity + Offsets.NEXT_ENTITY)
                entity_count += 1
        except:
            pass
        distinct_entities = list({mob_id: (mob_id, sprite_name, distance) for mob_id, sprite_name, distance in entities}.values())
        sorted_entities_by_distance = sorted(distinct_entities, key=lambda entity: entity[2])
        return sorted_entities_by_distance

    def close_chat_bar(self):
        MEMORY.process.write_bool(MEMORY.chat_address, False)

    def _get_id_buffs_all(self):
        buffs = []
        skill_buff_map = SERVERS_FILE.get_value(SKILL_BUFF)
        item_buff_map = SERVERS_FILE.get_value(ITEM_BUFF)
        status_debuff_map = SERVERS_FILE.get_value(STATUS_DEBUFF)
        for raw_buff in self.raw_buffs:
            buff = skill_buff_map.get(str(raw_buff), None) or item_buff_map.get(str(raw_buff), None) or status_debuff_map.get(str(raw_buff), raw_buff)
            buffs.append(buff)
            self.index_last_position_buff[buff] = (self.position[0], self.position[1])
        return buffs

    def _get_id_buffs(self, resource):
        skill_buffs = []
        skills_map = SERVERS_FILE.get_value(resource)
        for buff in self.raw_buffs:
            skill_buff = skills_map.get(str(buff), None)
            if not skill_buff:
                continue
            skill_buffs.append(skill_buff)
        return skill_buffs

    def next_item_buff_to_use(self, list_items, prop_seq) -> bool:
        if MEMORY.hp_address == 0x0:
            return None
        job_id = APP_CONTROLLER.job.id
        for item in list_items:
            if item.id not in self.item_buffs and not self.is_quagmire_block(job_id, item, prop_seq) and self.is_moviment_cell_done(job_id, item, prop_seq):
                return item
        return None

    def next_item_debuff_to_use(self, list_items) -> bool:
        if MEMORY.hp_address == 0x0:
            return None
        items_to_use = []
        for item in list_items:
            for status in item.recover_status:
                if status in self.status_debuff:
                    items_to_use.append(item)
        if len(items_to_use) == 0:
            return None
        return sorted(items_to_use, key=lambda item: item.priority, reverse=True)[0]

    def next_skill_buff_to_use(self, list_buff, prop_seq) -> bool:
        if MEMORY.hp_address == 0x0:
            return (None, None, None)
        buffs_to_use = []
        for job_id, buffs in list_buff.items():
            for buff in buffs:
                if buff.id not in self.skill_buffs and not self.is_quagmire_block(job_id, buff, prop_seq) and self.is_moviment_cell_done(job_id, buff, prop_seq):
                    buffs_to_use.append((job_id, buff.id, buff.priority))
        if len(buffs_to_use) == 0:
            return (None, None, None)
        return sorted(buffs_to_use, key=lambda x: x[2], reverse=True)[0]

    def is_quagmire_block(self, job_id, buff: Buff, prop_seq):
        key_base = [job_id, *prop_seq, buff.id, BLOCK_QUAGMIRE]
        if not CONFIG_FILE.get_value(key_base):
            return False
        return QUAGMIRE in self.status_debuff

    def is_moviment_cell_done(self, job_id, buff, prop_seq):
        active = CONFIG_FILE.get_value([job_id, *prop_seq, buff.id, USE_MOVIMENT])
        if not active:
            return True
        cells = CONFIG_FILE.get_value([job_id, *prop_seq, buff.id, MOVIMENT_CELLS])
        return self.is_cells_movimented(cells, buff.id)

    def is_cells_movimented(self, cells, buff_id):
        last_position_buff = self.index_last_position_buff.get(buff_id, None)
        if not last_position_buff:
            self.index_last_position_buff[buff_id] = (self.position[0], self.position[1])
            last_position_buff = self.index_last_position_buff[buff_id]
        x_distance = abs(last_position_buff[0] - self.position[0])
        y_distance = abs(last_position_buff[1] - self.position[1])
        return x_distance >= cells or y_distance >= cells

    def next_macro_element_to_use(self, list_auto_element) -> bool:
        macros_to_use = []
        if MEMORY.entity_list_address == 0x0:
            return (None, None, None)
        for job, macros in list_auto_element.items():
            for macro in macros:
                mob_ids = CONFIG_FILE.get_mob_ids([AUTO_ELEMENT, macro.id])
                for entity in self.entity_list:
                    if entity[0] in mob_ids:
                        macros_to_use.append((job, macro.id, entity[2]))
        if len(macros_to_use) == 0:
            return (None, None, None)
        return sorted(macros_to_use, key=lambda x: x[2])[0]

    def monitoring_job_change_gui(self):
        if MEMORY.job_address == 0x0:
            return
        if APP_CONTROLLER.job.id != JOB_MAP[self.job_id].id and isinstance(self.job, Job):
            APP_CONTROLLER.updated_job.emit(self.job)

    def _get_buffs(self):
        buffs = []
        if MEMORY.hp_address == 0x0:
            return buffs
        buff_index = 0
        buff_offset = Offsets.BUFF_LIST_LATAM if SERVERS_FILE.get_value(NAME) == "LATAM" else Offsets.BUFF_LIST
        while True:
            buff = MEMORY.process.read_int(MEMORY.hp_address + buff_offset + (0x4 * buff_index))
            if buff == -1:
                break
            buffs.append(buff)
            buff_index += 1
        return buffs

    def __str__(self):
        return f"""
            HP: {self.hp}/{self.hp_max}
            SP: {self.sp}/{self.sp_max}
            POSITION: {self.position}
            JOB: {self.job}
            MAP: {self.current_map}
            BUFFS: {self.buffs}
            CHAT_BAR_ENABLED: {self.chat_bar_enabled}
            ABRACADABRA_SKILL: {self.abracadabra_skill}
            ENTITY_LIST: \n{"\n".join([f"\t\t{id} - {name} ({distance:.2f})" for id, name, distance in self.entity_list])}
        """
