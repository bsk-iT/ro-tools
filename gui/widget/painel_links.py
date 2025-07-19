from PySide6.QtWidgets import QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import Qt

from gui.app_controller import APP_CONTROLLER
from gui.widget.input_notification import InputNotification
from service.servers_file import LINKS, NAME, TYPE, URL, VOTE
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
            self._add_link(link[NAME], link[URL], vbox, link.get(TYPE, None))
        self._add_link("MvP Timer", "https://www.ragnarokmvptimer.com/", vbox)
        self.layout.addWidget(scroll)

    def _add_link(self, name, link, layout, _type = None):
        widget = QWidget()
        vbox = QVBoxLayout(widget)
        vbox.setSpacing(5)
        if _type == VOTE:
            vbox.addWidget(InputNotification(self, f"{LINKS}:{VOTE}:", link))
        vbox.addWidget(QLabel(name))
        vbox.addWidget(build_link(link))
        layout.addWidget(widget)
