from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTabWidget
from PyQt5.QtCore import Qt

from config.icon import ICON_GITHUB
from gui.widget.input_app_status import InputAppStatus
from gui.widget.cbox_process import CboxProcess
from gui.widget.painel_config import PainelConfig
from gui.widget.painel_debug import PainelDebug
from gui.widget.painel_home import PainelHome
from gui.widget.painel_links import PainelLinks
from util.widgets import build_link_icon


class CentralWidget(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.cbox_process = CboxProcess(self)
        self._config_layout()

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        header_hbox = QHBoxLayout()
        hbox = QHBoxLayout()
        hbox.setAlignment(Qt.AlignmentFlag.AlignLeft)
        hbox.addWidget(build_link_icon(ICON_GITHUB, "https://github.com/uniaodk/ro-tools", 50))
        hbox.addWidget(self.cbox_process)
        header_hbox.addLayout(hbox)
        header_hbox.addWidget(InputAppStatus(self))
        self.layout.addLayout(header_hbox)
        tab_panel = QTabWidget()
        tab_panel.addTab(PainelHome(self), "Home")
        tab_panel.addTab(PainelLinks(self), "Links")
        tab_panel.addTab(PainelDebug(self), "Debug")
        tab_panel.addTab(PainelConfig(self), "Settings")
        self.layout.addWidget(tab_panel)
