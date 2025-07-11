from PyQt6.QtWidgets import QPushButton, QSizePolicy, QWidget
from PyQt6.QtGui import QKeySequence, QKeyEvent, QIcon
from PyQt6.QtCore import Qt, QSize, pyqtSignal

from config.app import APP_ICON_SIZE
from config.icon import ICON_KEYBOARD
from gui.app_controller import APP_CONTROLLER
from service.config_file import CONFIG_FILE


class InputKeybind(QPushButton):

    updated_key = pyqtSignal(str)

    def __init__(self, parent: QWidget, key_config=None, sync_hotkeys=False) -> None:
        super().__init__(parent)
        self.listenning = False
        self.sync_hotkeys = sync_hotkeys
        self.key_sequence = None
        self.key_config = key_config
        self.clicked.connect(self._start_listenning)
        self._config_layout()
        self._load_value()

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if not self.listenning:
            return super().keyPressEvent(event)
        self._on_change_key_sequence(event)

    def _config_layout(self) -> None:
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.setMinimumWidth(APP_ICON_SIZE)
        self.setStyleSheet("padding: 0;")
        self.setFixedHeight(APP_ICON_SIZE - 3)
        self.setIconSize(QSize(APP_ICON_SIZE - 6, APP_ICON_SIZE))

    def _load_value(self) -> None:
        value = CONFIG_FILE.read(self.key_config)
        if value is None:
            self._default_label()
            return
        self.key_sequence = QKeySequence(value)
        self.setText(self.key_sequence.toString())

    def _default_label(self) -> None:
        self.setIcon(QIcon(ICON_KEYBOARD))
        self.setText("")

    def _start_listenning(self) -> None:
        self.setText("_")
        self.setIcon(QIcon())
        self.listenning = True
        self.setFocus()

    def _on_change_key_sequence(self, event: QKeyEvent) -> None:
        key = event.key()
        if key in (Qt.Key.Key_Control, Qt.Key.Key_Shift, Qt.Key.Key_Alt, Qt.Key.Key_Meta):
            return
        self.listenning = False
        if key == Qt.Key.Key_Escape:
            self.setText(self.key_sequence.toString()) if self.key_sequence else self._remove_hotkey()
            return
        if key == Qt.Key.Key_Backspace:
            self._remove_hotkey()
        else:
            self._update_input_keybind(key, event)
        key_str = self.get_key_str(key, event)
        if self.sync_hotkeys and not "+" in key_str:
            APP_CONTROLLER.sync_hotkeys()

    def _remove_hotkey(self):
        self._default_label()
        CONFIG_FILE.update(self.key_config, None)

    def get_key_str(self, key, event):
        modifiers = event.modifiers().value
        self.key_sequence = QKeySequence(modifiers | key)
        return self.key_sequence.toString()

    def _update_input_keybind(self, key, event):
        key_str = self.get_key_str(key, event)
        if self.sync_hotkeys and (key_str in APP_CONTROLLER.get_all_hotkeys() or "+" in key_str):
            self._remove_hotkey()
            return
        self.setText(key_str)
        CONFIG_FILE.update(self.key_config, key_str)
        APP_CONTROLLER.sync_status_key()
