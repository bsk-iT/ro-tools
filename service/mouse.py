import win32api
import win32con
import time

from config.app import APP_DELAY
from service.config_file import CONFIG_FILE, DRIVE, KEYBOARD_TYPE
from util.widgets import is_interception_available


class Mouse:

    def __init__(self):
        self.toggle_pos = 1
        if is_interception_available():
            from interception import Interception

            self._interception = Interception()
            self._keyboard_id = self._interception.mouse

    def click(self, mouse_flick=False, button="left", x=None, y=None) -> None:
        self.move(x, y)
        keyboard_type = CONFIG_FILE.get_value([KEYBOARD_TYPE])
        if mouse_flick:
            self.toggle_pos *= -1
            self.move(0, 5 * self.toggle_pos)
        if keyboard_type != DRIVE:
            self.default_click(button)
        else:
            self.game_block_click(button)

    def game_block_click(self, button):
        from interception import MouseStroke, MouseFlag, MouseButtonFlag

        flag = MouseFlag.MOUSE_MOVE_RELATIVE
        if button == "left":
            self._interception.send(self._mouse_id, MouseStroke(flag, MouseButtonFlag.MOUSE_LEFT_BUTTON_DOWN, 0, 0, 0))
            time.sleep(APP_DELAY)
            self._interception.send(self._mouse_id, MouseStroke(flag, MouseButtonFlag.MOUSE_LEFT_BUTTON_UP, 0, 0, 0))
        elif button == "right":
            self._interception.send(self._mouse_id, MouseStroke(flag, MouseButtonFlag.MOUSE_RIGHT_BUTTON_DOWN, 0, 0, 0))
            time.sleep(APP_DELAY)
            self._interception.send(self._mouse_id, MouseStroke(flag, MouseButtonFlag.MOUSE_RIGHT_BUTTON_UP, 0, 0, 0))

    def default_click(self, button):
        action_down = win32con.MOUSEEVENTF_LEFTDOWN if button == "left" else win32con.MOUSEEVENTF_RIGHTDOWN
        action_up = win32con.MOUSEEVENTF_LEFTUP if button == "left" else win32con.MOUSEEVENTF_RIGHTUP
        win32api.mouse_event(action_down, 0, 0, 0, 0)
        time.sleep(APP_DELAY)
        win32api.mouse_event(action_up, 0, 0, 0, 0)

    def move(self, x_offset=None, y_offset=None) -> None:
        if x_offset is None or y_offset is None:
            return
        (x, y) = win32api.GetCursorPos()
        win32api.SetCursorPos((x + x_offset, y + y_offset))


MOUSE = Mouse()
