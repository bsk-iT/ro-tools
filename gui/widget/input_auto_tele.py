from PySide6.QtWidgets import QToolButton, QVBoxLayout, QHBoxLayout, QLabel, QWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt
from config.icon import ICON_TELEPORT
from gui.app_controller import APP_CONTROLLER
from gui.widget.input_keybind import InputKeybind
from service.config_file import AUTO_ITEM, AUTO_TELEPORT, CONFIG_FILE, FLY_WING, SHORTCUT_KEY
from util.widgets import ICON_STATUS


class InputAutoTele(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QHBoxLayout(self)
        self.shortcut_key = CONFIG_FILE.read(f"{AUTO_ITEM}:{FLY_WING}:{SHORTCUT_KEY}")
        self._config_layout()
        self.auto_tele_toggle.toggled.connect(self._on_toggle_auto_tele)
        APP_CONTROLLER.toogled_auto_tele.connect(self.auto_tele_toggle.setChecked)

    def _on_toggle_auto_tele(self, value):
        APP_CONTROLLER.toogled_auto_tele.emit(value)

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        toggle = QToolButton()
        toggle.setCheckable(True)
        active = CONFIG_FILE.read(f"{AUTO_ITEM}:{FLY_WING}:" + AUTO_TELEPORT)
        toggle.setChecked(True if active else False)
        toggle.setIcon(QIcon(ICON_TELEPORT))
        toggle.setIconSize(ICON_STATUS)
        toggle.setToolTip(f"LIGAR/DESLIGAR o Auto Teletranporte")
        self.auto_tele_toggle = toggle
        self.input_keybind = InputKeybind(None, f"{AUTO_ITEM}:{FLY_WING}:{SHORTCUT_KEY}", True)
        vbox = QVBoxLayout()
        vbox.setSpacing(0)
        vbox.addWidget(QLabel("Atalho"))
        vbox.addWidget(self.input_keybind, alignment=Qt.AlignmentFlag.AlignRight)
        self.layout.addLayout(vbox)
        self.layout.addWidget(self.auto_tele_toggle)
