from PyQt5.QtWidgets import QVBoxLayout, QWidget, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt

from service.config_file import AUTO_CLOSE, BLOCK_CHAT_INPUT, CONFIG_FILE, DEFAULT, DRIVE, KEYBOARD_TYPE, PHYSICAL, VIRTUAL, WAITING
from service.servers_file import SERVERS_FILE
from util.widgets import build_link, build_link_file, build_radio_btn, build_scroll_vbox, is_interception_available


class PainelConfig(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self._config_layout()
        self.sync_radio_keyboard_type()
        self.sync_radio_block_chat_input()

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.setSpacing(15)
        (vbox, scroll) = build_scroll_vbox(100)
        vbox.setSpacing(15)
        self._build_file_server(vbox)
        self._build_radio_keyboard_type(vbox)
        self._build_radio_block_chat_input(vbox)
        self.layout.addWidget(scroll)

    def _build_file_server(self, layout):
        widget = QWidget()
        vbox = QVBoxLayout(widget)
        vbox.setSpacing(5)
        vbox.addWidget(QLabel("Arquivo configuração do server:"))
        vbox.addWidget(build_link_file(SERVERS_FILE))
        layout.addWidget(widget)

    def _build_radio_keyboard_type(self, layout):
        widget = QWidget()
        vbox = QVBoxLayout(widget)
        vbox.setSpacing(5)
        vbox.addWidget(QLabel("Tipo de simulação do teclado:"))
        self.rad_virtual = build_radio_btn("Virtual - Ações serão enviadas somente para o jogo | Não funciona combinações de tecla Ex: ALT+1")
        self.rad_physical = build_radio_btn("Físico - Afeta qualquer programa | Combinações de tecla são aceito Ex: ALT+1")
        self.rad_drive = build_radio_btn("Drive - Caso não funcione as opções acima. Requer instalação do Interception.\t")
        hbox_drive = QHBoxLayout()
        hbox_drive.addWidget(self.rad_drive)
        hbox_drive.addWidget(build_link("https://github.com/oblitum/Interception", "Download"))
        self.rad_virtual.clicked.connect(self.on_radio_keyboard_type)
        self.rad_physical.clicked.connect(self.on_radio_keyboard_type)
        self.rad_drive.clicked.connect(self.on_radio_keyboard_type)
        vbox.addWidget(self.rad_virtual)
        vbox.addWidget(self.rad_physical)
        vbox.addLayout(hbox_drive)
        layout.addWidget(widget)

    def on_radio_keyboard_type(self):
        if self.rad_virtual.isChecked():
            CONFIG_FILE.update(KEYBOARD_TYPE, VIRTUAL)
        if self.rad_physical.isChecked():
            CONFIG_FILE.update(KEYBOARD_TYPE, PHYSICAL)
        if self.rad_drive.isChecked():
            CONFIG_FILE.update(KEYBOARD_TYPE, DRIVE)

    def sync_radio_keyboard_type(self):
        keyboard_type = CONFIG_FILE.read(KEYBOARD_TYPE)
        if not is_interception_available():
            keyboard_type = None if keyboard_type == DRIVE else keyboard_type
            self.rad_drive.setDisabled(True)
            self.rad_drive.setStyleSheet("font-size: 12px;color: #ccc;")
        if keyboard_type is None:
            keyboard_type = VIRTUAL
            CONFIG_FILE.update(KEYBOARD_TYPE, keyboard_type)
        if keyboard_type == VIRTUAL:
            self.rad_virtual.setChecked(True)
        if keyboard_type == PHYSICAL:
            self.rad_physical.setChecked(True)
        if keyboard_type == DRIVE:
            self.rad_drive.setChecked(True)


    def _build_radio_block_chat_input(self, layout):
        widget = QWidget()
        vbox = QVBoxLayout(widget)
        vbox.setSpacing(5)
        vbox.addWidget(QLabel("Comportamento da ferramenta quando o chat do jogo estiver aberto:"))
        self.rad_chat_default = build_radio_btn("Continuar executando")
        self.rad_chat_auto_close = build_radio_btn("Bloquear automáticamente o chat do jogo")
        self.rad_chat_waiting = build_radio_btn("Aguardar o chat ser fechado para continuar executando")
        self.rad_chat_default.clicked.connect(self.on_radio_block_chat_input)
        self.rad_chat_auto_close.clicked.connect(self.on_radio_block_chat_input)
        self.rad_chat_waiting.clicked.connect(self.on_radio_block_chat_input)
        vbox.addWidget(self.rad_chat_default)
        vbox.addWidget(self.rad_chat_auto_close)
        vbox.addWidget(self.rad_chat_waiting)
        layout.addWidget(widget)

    def on_radio_block_chat_input(self):
        if self.rad_chat_default.isChecked():
            CONFIG_FILE.update(BLOCK_CHAT_INPUT, DEFAULT)
        if self.rad_chat_auto_close.isChecked():
            CONFIG_FILE.update(BLOCK_CHAT_INPUT, AUTO_CLOSE)
        if self.rad_chat_waiting.isChecked():
            CONFIG_FILE.update(BLOCK_CHAT_INPUT, WAITING)

    def sync_radio_block_chat_input(self):
        block_chat = CONFIG_FILE.read(BLOCK_CHAT_INPUT)
        if block_chat is None:
            block_chat = DEFAULT
            CONFIG_FILE.update(BLOCK_CHAT_INPUT, block_chat)
        if block_chat == DEFAULT:
            self.rad_chat_default.setChecked(True)
        if block_chat == AUTO_CLOSE:
            self.rad_chat_auto_close.setChecked(True)
        if block_chat == WAITING:
            self.rad_chat_waiting.setChecked(True)
