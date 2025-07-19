from PySide6.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy
from PySide6.QtGui import QPixmap, QPalette, QBrush
from PySide6.QtCore import Qt

from config.icon import PATH_ICON, get_image
from service.config_file import CONFIG_FILE, REGION_IDS


class InputMapRegion(QWidget):

    def __init__(self, parent, key_base):
        super().__init__(parent)
        self.key_base = key_base
        region_ids = CONFIG_FILE.read(self.key_base + REGION_IDS)
        self.active_ids = region_ids or []
        self.setFixedWidth(150)
        self.image = QPixmap(get_image(PATH_ICON, "prontera"))
        self.setAutoFillBackground(True)
        self.grid = QGridLayout(self)
        self.grid.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.grid.setSpacing(0)
        self.grid.setContentsMargins(0, 0, 0, 0)

        self.id_map = {(0, 0): 7, (0, 1): 8, (0, 2): 9, (1, 0): 4, (1, 1): 5, (1, 2): 6, (2, 0): 1, (2, 1): 2, (2, 2): 3}
        self.buttons = {}
        for pos, id in self.id_map.items():
            btn = QPushButton(str(id))
            btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            btn.setCheckable(True)
            btn.setStyleSheet(
                """
                QPushButton {
                    background-color: rgba(255, 255, 255, 80);
                    border: 1px solid gray;
                    color: red;
                    font-size: 30px;
                    font-weight: bold;
                }
                QPushButton:checked {
                    background-color: rgba(100, 200, 255, 150);
                }
            """
            )
            btn.setChecked(id in self.active_ids)
            btn.clicked.connect(self.toggle_button)
            self.grid.addWidget(btn, *pos)
            self.buttons[id] = btn

    def set_background(self, pixmap: QPixmap):
        scaled = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(scaled))
        self.setPalette(palette)

    def resizeEvent(self, event):
        if self.image:
            self.set_background(self.image)
        super().resizeEvent(event)

    def toggle_button(self):
        button = self.sender()
        id = int(button.text())
        if button.isChecked():
            self.active_ids.append(id)
        else:
            self.active_ids.remove(id)
        CONFIG_FILE.update(self.key_base + REGION_IDS, self.active_ids)
