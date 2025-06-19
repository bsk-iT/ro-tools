from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel
from PyQt6.QtCore import Qt

from util.widgets import build_link, build_scroll_vbox


class PainelLinks(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self._config_layout()

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.setSpacing(15)
        (vbox, scroll) = build_scroll_vbox(100)
        vbox.setSpacing(15)
        self._add_link("LegionBR", "https://www.legionbr.net/", vbox)
        self._add_link("Vote 4 Point", "https://www.legionbr.net/master-account/vote4points", vbox)
        self._add_link("Wiki", "https://wiki.legionbr.net/", vbox)
        self._add_link("Daily Quests", "https://uniaodk.github.io/ragnarok-tools/assets/view/daily_quest.html", vbox)
        self._add_link("Item Quest Simulator", "https://uniaodk.github.io/ragnarok-item-quest-simulator/", vbox)
        self._add_link("MvP Timer", "https://www.ragnarokmvptimer.com/", vbox)
        self.layout.addWidget(scroll)

    def _add_link(self, name, link, layout):
        widget = QWidget()
        vbox = QVBoxLayout(widget)
        vbox.setSpacing(5)
        vbox.addWidget(QLabel(name))
        vbox.addWidget(build_link(link))
        layout.addWidget(widget)
