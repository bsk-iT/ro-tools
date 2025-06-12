from PyQt6.QtWidgets import QWidget, QToolButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

from config.icon import ICON_SWAP, PATH_ITEM, get_image
from gui.widget.input_keybind import InputKeybind
from service.config_file import CONFIG_FILE, KEY, SWAP_ACTIVE
from util.widgets import ICON_BTN, build_icon

MAX_SWAP = 6
ITEM_SWAP = ["NOVICE_EGG_CAP", "NOVICE_PLATE", "NOVICE_KNIFE", "NOVICE_GUARD", "NOVICE_HOOD", "NOVICE_BOOTS"]
ITEM_TOOLTIP = ["Hat", "Armadura", "Arma", "Escudo", "Capa", "Sapato"]


class InputSwap(QWidget):
    def __init__(self, parent, key_base):
        super().__init__(parent)
        self.key_base = key_base
        self.layout = QHBoxLayout(self)
        self.toggle = self._build_toggle()
        self.inputs_swap = self._build_inputs_swap()
        self._config_layout()
        self._config_events()

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.toggle)
        self.layout.addWidget(self.inputs_swap)

    def _config_events(self) -> None:
        self.toggle.toggled.connect(self._on_active_delay)
        self._on_active_delay(self.toggle.isChecked())

    def _build_toggle(self) -> QToolButton:
        toggle = QToolButton()
        toggle.setCheckable(True)
        active = CONFIG_FILE.read(self.key_base + SWAP_ACTIVE)
        toggle.setChecked(active if active else False)
        toggle.setIcon(QIcon(ICON_SWAP))
        toggle.setIconSize(ICON_BTN)
        toggle.setToolTip("Swap entres equipes de ATK/DEF")
        return toggle

    def _build_inputs_swap(self):
        widget = QWidget()
        vbox = QVBoxLayout(widget)
        vbox.addWidget(self._build_input_keybinds("atk"))
        vbox.addLayout(self._build_swap_img())
        vbox.addWidget(self._build_input_keybinds("def"))
        return widget

    def _build_input_keybinds(self, type_swap):
        widget = QWidget()
        hbox = QHBoxLayout(widget)
        hbox.setContentsMargins(5, 0, 5, 0)
        hbox.setSpacing(0)
        hbox.addWidget(QLabel(type_swap.upper()))
        for index in range(MAX_SWAP):
            hbox.addWidget(InputKeybind(self, self.key_base + f"{type_swap}_{index}_{KEY}"))
        widget.setStyleSheet(f"background-color: {"#AF6060" if type_swap == "atk" else "#207D8A"}; border-radius: 5px;")
        return widget

    def _build_swap_img(self):
        hbox = QHBoxLayout()
        hbox.addWidget(QLabel())
        hbox.setContentsMargins(5, 0, 5, 0)
        hbox.setSpacing(0)
        for index in range(MAX_SWAP):
            image_path = get_image(PATH_ITEM, ITEM_SWAP[index])
            hbox.addWidget(build_icon(image_path, ITEM_TOOLTIP[index]))
        return hbox

    def _on_active_delay(self, value: bool) -> None:
        self.inputs_swap.setVisible(value)
        CONFIG_FILE.update(self.key_base + SWAP_ACTIVE, value)
