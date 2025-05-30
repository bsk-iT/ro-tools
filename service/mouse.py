import win32api
import win32con
import time


class Mouse:
    def click(self, button="left", x=None, y=None) -> None:
        self.move(x, y)
        action_down = win32con.MOUSEEVENTF_LEFTDOWN if button == "left" else win32con.MOUSEEVENTF_RIGHTDOWN
        action_up = win32con.MOUSEEVENTF_LEFTUP if button == "left" else win32con.MOUSEEVENTF_RIGHTUP
        win32api.mouse_event(action_down, 0, 0, 0, 0)
        time.sleep(self.delay)
        win32api.mouse_event(action_up, 0, 0, 0, 0)

    def move(self, x=None, y=None) -> None:
        if x is None or y is None:
            return
        win32api.SetCursorPos((x, y))


MOUSE = Mouse()
