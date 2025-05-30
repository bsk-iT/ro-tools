from PyQt6.QtWidgets import QWidget, QToolButton, QComboBox, QSizePolicy, QHBoxLayout
from PyQt6.QtGui import QIcon

from config.app import APP_MAP_CRITERIA
from config.icon import ICON_MAP
from service.file import CONFIG_FILE
from util.widgets import ICON_BTN


class InputMapCriteria(QWidget):
    def __init__(self, parent: QWidget, active: str, map_criteria: str) -> None:
        super().__init__(parent)
        self.active = active
        self.map_criteria = map_criteria
        self.layout = QHBoxLayout(self)
        self.toggle = self._build_toggle(active)
        self.cbox_map = self._build_cbox_map(map_criteria)
        self._config_layout()
        self._config_events()

    def _config_layout(self) -> None:
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.toggle)
        self.layout.addWidget(self.cbox_map)

    def _config_events(self) -> None:
        self.toggle.toggled.connect(self._on_active_delay)
        self.cbox_map.currentIndexChanged.connect(self._on_change_map)
        self._on_active_delay(self.toggle.isChecked())

    def _build_toggle(self, active: str) -> QToolButton:
        toggle = QToolButton()
        toggle.setCheckable(True)
        active: bool = CONFIG_FILE.read(active)
        toggle.setChecked(active if active else False)
        toggle.setIcon(QIcon(ICON_MAP))
        toggle.setIconSize(ICON_BTN)
        toggle.setToolTip("Ativo somente nesse tipo de mapa")
        return toggle

    def _build_cbox_map(self, map_criteria: str) -> QComboBox:
        cbox = QComboBox()
        cbox.addItems(APP_MAP_CRITERIA)
        cbox.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        map_selected = CONFIG_FILE.read(map_criteria)
        if map_selected:
            cbox.setCurrentIndex([m.lower() for m in APP_MAP_CRITERIA].index(map_selected))
        return cbox

    def _on_active_delay(self, value: bool) -> None:
        self.cbox_map.setVisible(value)
        CONFIG_FILE.update(self.active, value)

    def _on_change_map(self, index: int) -> None:
        CONFIG_FILE.update(self.map_criteria, APP_MAP_CRITERIA[index].lower())
