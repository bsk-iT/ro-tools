from PySide6.QtWidgets import QWidget, QToolButton, QHBoxLayout
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

from config.icon import PATH_ITEM, get_image
from service.config_file import CONFIG_FILE, PET_ACTIVE
from util.widgets import ICON_BTN


class InputPet(QWidget):
    def __init__(self, parent, key_base):
        super().__init__(parent)
        self.key_base = key_base
        self.layout = QHBoxLayout(self)
        self.toggle = self._build_toggle()
        self._config_layout()
        self._config_events()

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.toggle)

    def _config_events(self) -> None:
        self.toggle.toggled.connect(self._on_active_pet)
        self._on_active_pet(self.toggle.isChecked())

    def _build_toggle(self) -> QToolButton:
        toggle = QToolButton()
        toggle.setCheckable(True)
        active = CONFIG_FILE.read(self.key_base + PET_ACTIVE)
        toggle.setChecked(active if active else False)
        toggle.setIcon(QIcon(get_image(PATH_ITEM, "incubator")))
        toggle.setIconSize(ICON_BTN)
        return toggle

    def _on_active_pet(self, value: bool) -> None:
        self.toggle.setToolTip(f"Auto capturar PET - {"LIGADO" if value else "DESLIGADO"}")
        CONFIG_FILE.update(self.key_base + PET_ACTIVE, value)
