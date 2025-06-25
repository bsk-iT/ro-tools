from PyQt6.QtWidgets import QWidget, QToolButton, QHBoxLayout, QVBoxLayout, QLabel, QPlainTextEdit
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt

from config.icon import ICON_TELEPORT
from service.config_file import AUTO_TELEPORT, CONFIG_FILE, MOB_IDS
from util.widgets import ICON_BTN, build_label


class InputTeleport(QWidget):
    def __init__(self, parent, key_base):
        super().__init__(parent)
        self.key_base = key_base
        self.layout = QHBoxLayout(self)
        self.text_edit = QPlainTextEdit()
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
        hbox = QHBoxLayout(widget)
        vbox = QVBoxLayout()
        vbox.setSpacing(0)
        label_1 = QLabel("Auto Teleport ATIVO")
        label_1.setStyleSheet("color: green; font-size: 10px;")
        label_1.setWordWrap(True)
        vbox.addWidget(label_1)
        vbox.addWidget(build_label('Ao clicar na tecla da "Asa de Mosca" inicia automatização, clicar novamente ou encontrar o mob, irá parar automatização.', 10, True))
        label_2 = QLabel('Adicionar o ID do mob que gostaria de localizar, se for mais de um separar por ";". Ex: 1009;1008;1007')
        label_2.setStyleSheet("color: red; font-size: 10px;")
        label_2.setWordWrap(True)
        vbox.addWidget(label_2)
        text = CONFIG_FILE.read(self.key_base + MOB_IDS)
        self.text_edit.setPlainText(text)
        self.text_edit.textChanged.connect(self.change_mob_id)
        hbox.addWidget(self.text_edit)
        hbox.addLayout(vbox)
        return widget

    def change_mob_id(self):
        CONFIG_FILE.update(self.key_base + MOB_IDS, self.text_edit.toPlainText())

    def _config_events(self) -> None:
        self.toggle.toggled.connect(self._on_active_auto_teleport)
        self._on_active_auto_teleport(self.toggle.isChecked())

    def _build_toggle(self) -> QToolButton:
        toggle = QToolButton()
        toggle.setCheckable(True)
        active = CONFIG_FILE.read(self.key_base + AUTO_TELEPORT)
        toggle.setChecked(active if active else False)
        toggle.setIcon(QIcon(ICON_TELEPORT))
        toggle.setIconSize(ICON_BTN)
        toggle.setToolTip(f"Auto teleport MOB")
        return toggle

    def _on_active_auto_teleport(self, value: bool) -> None:
        self.config.setVisible(value)
        CONFIG_FILE.update(self.key_base + AUTO_TELEPORT, value)
