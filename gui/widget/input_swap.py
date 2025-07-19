from PySide6.QtWidgets import QWidget, QToolButton, QHBoxLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

from gui.widget.cbox_macro_select import CboxMacroSelect
from service.config_file import ACTIVE, CONFIG_FILE, MACRO
from util.widgets import ICON_BTN


class InputSwap(QWidget):
    def __init__(self, parent, resource, key_base, icon):
        super().__init__(parent)
        self.resource = resource
        self.key_base = key_base + f"swap_{self.resource}:"
        self.icon = icon
        self.layout = QHBoxLayout(self)
        self.toggle = self._build_toggle()
        self.cbox_macro = CboxMacroSelect(self, self.key_base + MACRO)
        self._config_layout()
        self._config_events()

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.toggle)
        self.layout.addWidget(self.cbox_macro)

    def _config_events(self) -> None:
        self.toggle.toggled.connect(self._on_active_swap)
        self._on_active_swap(self.toggle.isChecked())

    def _build_toggle(self) -> QToolButton:
        toggle = QToolButton()
        toggle.setCheckable(True)
        active = CONFIG_FILE.read(self.key_base + ACTIVE)
        toggle.setChecked(active if active else False)
        toggle.setIcon(QIcon(self.icon))
        toggle.setIconSize(ICON_BTN)
        return toggle

    def _on_active_swap(self, value: bool) -> None:
        self.cbox_macro.setVisible(value)
        self.toggle.setToolTip(f"Macro Swap para equipe de {self.resource.upper()} - {"LIGADO" if value else "DESLIGADO"}")
        CONFIG_FILE.update(self.key_base + ACTIVE, value)
