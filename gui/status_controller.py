import keyboard

from PyQt6.QtWidgets import QToolButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from config.icon import ICON_OFF, ICON_ON
from events.game import GAME
from gui.widget.input_keybind import InputKeybind
from service.event import EVENT, Prop
from service.memory import MEMORY
from util.widgets import ICON_STATUS


class StatusController:

    def __init__(self):
        self.layout = None
        self.status_toggle = None
        self.input_keybind = None
        self.status_key = EVENT.get_config(Prop.KEY_MONITORING)
        if self.status_key:
            self.on_change_keybind(self.status_key)

    def start(self):
        self._load_status_toggle()
        self.status_toggle.toggled.connect(self.on_togle_monitoring)
        self.input_keybind.updated_key.connect(self.on_change_keybind)

    def _load_status_toggle(self) -> QToolButton:
        hbox = QHBoxLayout()
        hbox.setAlignment(Qt.AlignmentFlag.AlignRight)
        toggle = QToolButton()
        toggle.setCheckable(True)
        toggle.setObjectName("status-btn")
        toggle.setChecked(False)
        toggle.setIcon(QIcon(ICON_OFF))
        toggle.setIconSize(ICON_STATUS)
        toggle.setToolTip("LIGAR/DESLIGAR o monitoramento e eventos do RO Tools")
        self.status_toggle = toggle
        self.input_keybind = InputKeybind(None, EVENT.get_config_key(Prop.KEY_MONITORING))
        vbox = QVBoxLayout()
        vbox.setSpacing(0)
        vbox.addWidget(QLabel("Status"))
        vbox.addWidget(self.input_keybind, alignment=Qt.AlignmentFlag.AlignRight)
        hbox.addLayout(vbox)
        hbox.addWidget(self.status_toggle)
        self.layout = hbox

    def on_change_keybind(self, key: str):
        if self.status_key != key and not self.status_key is None:
            keyboard.remove_hotkey(self.status_key)
        self.status_key = key
        keyboard.add_hotkey(key, self.on_togle_monitoring)

    def on_togle_monitoring(self, active=None):
        if not MEMORY.is_valid():
            return
        if active is None:
            self.status_toggle.toggle()
            return
        GAME.start() if self.status_toggle.isChecked() else GAME.stop()
        self.status_toggle.setIcon(QIcon(ICON_ON if active else ICON_OFF))


STATUS_CONTROLLER = StatusController()
