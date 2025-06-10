from PyQt6.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout, QCheckBox, QTabWidget
from PyQt6.QtCore import Qt

from gui.widget.painel_auto_item_buff import PainelAutoItemBuff
from gui.widget.painel_auto_item_debuff import PainelAutoItemDebuff
from gui.widget.painel_auto_item_hp_sp import PainelAutoItemHpSp
from service.config_file import AUTO_ITEM, CITY_ACTIVE, CONFIG_FILE
from service.servers_file import SERVERS_FILE
from util.widgets import build_link_file, build_painel


class PainelAutoItem(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self._config_layout()

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        painel = build_painel(self.layout, "Auto Item")
        painel.addLayout(self._build_layout_config())
        tab_panel = QTabWidget()
        tab_panel.addTab(PainelAutoItemHpSp(self), "HP/SP")
        tab_panel.addTab(PainelAutoItemBuff(self), "Buff")
        tab_panel.addTab(PainelAutoItemDebuff(self), "Debuff")
        painel.addWidget(tab_panel)

    def _build_layout_config(self):
        vbox = QVBoxLayout()
        vbox.setContentsMargins(0, 0, 0, 0)
        hbox_city = QHBoxLayout()
        check_city = QCheckBox("Ativo em cidades")
        active_city = CONFIG_FILE.get_value([AUTO_ITEM, CITY_ACTIVE])
        check_city.setChecked(True if active_city else False)
        check_city.checkStateChanged.connect(self._update_active_city)
        hbox_city.addWidget(check_city)
        hbox_city.addWidget(build_link_file(SERVERS_FILE))
        vbox.addLayout(hbox_city)
        return vbox

    def _update_active_city(self, state):
        CONFIG_FILE.update_config(state.value == 2, [AUTO_ITEM, CITY_ACTIVE])
