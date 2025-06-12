from PyQt6.QtWidgets import QWidget, QToolButton, QComboBox, QSizePolicy, QHBoxLayout
from PyQt6.QtGui import QIcon

from config.icon import ICON_MAP
from service.config_file import CONFIG_FILE, MAP, MAP_ACTIVE
from service.servers_file import TYPE_MAPS
from util.widgets import ICON_BTN


class InputMapCriteria(QWidget):
    def __init__(self, parent: QWidget, key_seq: str) -> None:
        super().__init__(parent)
        self.key_seq = key_seq
        self.layout = QHBoxLayout(self)
        self.toggle = self._build_toggle()
        self.cbox_map = self._build_cbox_map()
        self._config_layout()
        self._config_events()

    def _config_layout(self) -> None:
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.toggle)
        self.layout.addWidget(self.cbox_map)

    def _config_events(self) -> None:
        self.toggle.toggled.connect(self._on_active_map)
        self.cbox_map.currentIndexChanged.connect(self._on_change_map)
        self._on_active_map(self.toggle.isChecked())

    def _build_toggle(self) -> QToolButton:
        toggle = QToolButton()
        toggle.setCheckable(True)
        active = CONFIG_FILE.read(self.key_seq + MAP_ACTIVE)
        toggle.setChecked(active if active else False)
        toggle.setIcon(QIcon(ICON_MAP))
        toggle.setIconSize(ICON_BTN)
        toggle.setToolTip("Ativo somente nesse tipo de mapa")
        return toggle

    def _build_cbox_map(self) -> QComboBox:
        cbox = QComboBox()
        cbox.addItems(TYPE_MAPS)
        cbox.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        map_selected = CONFIG_FILE.read(self.key_seq + MAP)
        if map_selected:
            cbox.setCurrentIndex([m.lower() for m in TYPE_MAPS].index(map_selected))
        return cbox

    def _on_active_map(self, value: bool) -> None:
        self.cbox_map.setVisible(value)
        CONFIG_FILE.update(self.key_seq + MAP_ACTIVE, value)

    def _on_change_map(self, index: int) -> None:
        CONFIG_FILE.update(self.key_seq + MAP, TYPE_MAPS[index].lower())
