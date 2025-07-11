from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel
from PyQt5.QtCore import Qt

from gui.app_controller import APP_CONTROLLER
from service.servers_file import NAME, URL
from util.widgets import build_link, build_scroll_vbox, clear_layout


class PainelLinks(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self._config_layout()
        APP_CONTROLLER.updated_process.connect(self.update_links)

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.setSpacing(15)
        self.update_links()

    def update_links(self):
        clear_layout(self.layout.takeAt(0))
        (vbox, scroll) = build_scroll_vbox(100)
        vbox.setSpacing(15)
        for link in APP_CONTROLLER.links:
            self._add_link(link[NAME], link[URL], vbox)
        self._add_link("MvP Timer", "https://www.ragnarokmvptimer.com/", vbox)
        self.layout.addWidget(scroll)

    def _add_link(self, name, link, layout):
        widget = QWidget()
        vbox = QVBoxLayout(widget)
        vbox.setSpacing(5)
        vbox.addWidget(QLabel(name))
        vbox.addWidget(build_link(link))
        layout.addWidget(widget)
