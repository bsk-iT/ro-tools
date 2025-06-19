from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTabWidget
from PyQt6.QtCore import Qt

from config.icon import ICON_GITHUB
from gui.widget.input_app_status import InputAppStatus
from gui.widget.cbox_process import CboxProcess
from gui.widget.painel_auto_item import PainelAutoItem
from gui.widget.painel_config import PainelConfig
from gui.widget.painel_job import PainelJob
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
        tab_panel.addTab(self._build_main_painel(), "Início")
        tab_panel.addTab(PainelLinks(self), "Links")
        tab_panel.addTab(PainelConfig(self), "Configurações")
        self.layout.addWidget(tab_panel)

    def _build_main_painel(self):
        widget = QWidget()
        body_hbox = QHBoxLayout(widget)
        body_hbox.addWidget(PainelAutoItem(self), alignment=Qt.AlignmentFlag.AlignLeft)
        body_hbox.addWidget(PainelJob(self))
        return widget
