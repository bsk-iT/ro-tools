from PyQt5.QtWidgets import QWidget, QToolButton, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from config.icon import ICON_MVP
from service.config_file import CONFIG_FILE, MVP_ACTIVE
from util.widgets import ICON_BTN, build_label


class InputMvp(QWidget):
    def __init__(self, parent, key_base):
        super().__init__(parent)
        self.key_base = key_base
        self.layout = QHBoxLayout(self)
        self.toggle = self._build_toggle()
        self.config = self._build_config()
        self._config_layout()
        self._config_events()

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.toggle)
        self.layout.addWidget(self.config)

    def _build_config(self):
        widget = QWidget()
        vbox = QVBoxLayout(widget)
        vbox.setSpacing(0)
        label_1 = QLabel("Autocast ATIVO")
        label_1.setStyleSheet("color: green; font-size: 10px;")
        label_1.setWordWrap(True)
        vbox.addWidget(label_1)
        vbox.addWidget(build_label('Ao clicar na tecla da skill "Abracadabra" inicia automatização, clicar novamente ou encontrar a skill que invoca MvP, irá parar automatização.', 10, True))
        label_2 = QLabel('Para melhor eficiência configurar skill "Cancelar Magia"')
        label_2.setStyleSheet("color: red; font-size: 10px;")
        label_2.setWordWrap(True)
        vbox.addWidget(label_2)
        return widget

    def _config_events(self) -> None:
        self.toggle.toggled.connect(self._on_active_mvp)
        self._on_active_mvp(self.toggle.isChecked())

    def _build_toggle(self) -> QToolButton:
        toggle = QToolButton()
        toggle.setCheckable(True)
        active = CONFIG_FILE.read(self.key_base + MVP_ACTIVE)
        toggle.setChecked(active if active else False)
        toggle.setIcon(QIcon(ICON_MVP))
        toggle.setIconSize(ICON_BTN)
        toggle.setToolTip(f"Auto summonar MvP")
        return toggle

    def _on_active_mvp(self, value: bool) -> None:
        self.config.setVisible(value)
        CONFIG_FILE.update(self.key_base + MVP_ACTIVE, value)
