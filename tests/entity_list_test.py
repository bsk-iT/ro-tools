import time
from service.keyboard import KEYBOARD
from service.memory import MEMORY


def _get_entity_list():
    is_found = False
    while True:
        MEMORY.update_process("LegionBR.exe", 3916)
        game_mode = MEMORY.process.read_uint(MEMORY.base_address + 0x00A43F44)
        world = MEMORY.process.read_uint(game_mode + 0xCC)
        entity_list = MEMORY.process.read_uint(world + 0x10)
        prev_entity = MEMORY.process.read_uint(entity_list + 0x0)
        entity = MEMORY.process.read_uint(prev_entity + 0x8)
        list_entity = []
        while entity != 0:
            mob_id = MEMORY.process.read_uint(entity + 0x10C)
            x_pos = MEMORY.process.read_uint(entity + 0x15C)
            y_pos = MEMORY.process.read_uint(entity + 0x160)
            list_entity.append(mob_id)
            prev_entity = MEMORY.process.read_uint(prev_entity + 0x0)
            entity = MEMORY.process.read_uint(prev_entity + 0x8)
        if not 1080 in list_entity:
            is_found = False
            KEYBOARD.press_key("Space")
            time.sleep(0.2)
            KEYBOARD.press_key("Space")
            time.sleep(0.2)
            continue
        if not is_found:
            KEYBOARD.press_key("Enter+E+s+t+a+Space+a+q+u+i+Enter")
            is_found = True


def main():
    _get_entity_list()


if __name__ == "__main__":
    main()
