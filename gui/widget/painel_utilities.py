from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QPlainTextEdit, QLabel
from PySide6.QtCore import Qt

from gui.widget.input_keybind import InputKeybind
from service.config_file import AUTO_COMMANDS, COMMANDS, CONFIG_FILE, DRAFT_COMMANDS, KEY
from util.widgets import build_label_info, build_label_subtitle, build_scroll_vbox

DEFAULT_DRAFT = """--- Autoloot Types ---
@aloottype + 0 -> Items de Cura
@aloottype + 2 -> Utilizáveis
@aloottype + 3 -> Etc
@aloottype + 4 -> Armadura
@aloottype + 5 -> Arma
@aloottype + 6 -> Carta
@aloottype + 7 -> Pet Egg
@aloottype + 8 -> Pet Armor
@aloottype + 10 -> Munição

--- Consumíveis ---
@alootid + 518 -> Mastela
@alootid + 522 -> Mastela
@alootid + 526 -> Geléia Real

--- Caixas ---
@alootid + 603 -> Velha Caixa Azul
@alootid + 617 -> Velha Caixa Roxa
@alootid + 644 -> Caixa de Presente
@alootid + 12030 -> Caixa do Ressentimento

--- Equipes ---
@alootid + 1705 -> Arco Composto [4]

--- Etc ---
@alootid + 748 -> Rosa Eterna
@alootid + 747 -> Espelho de Cristal

"""


class PainelUtilities(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.key_base = f"{AUTO_COMMANDS}:"
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self.auto_commands = QPlainTextEdit()
        self.draft_auto_commands = QPlainTextEdit()
        self._config_layout()

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.setSpacing(15)
        (vbox, scroll) = build_scroll_vbox()
        vbox.addLayout(self.build_auto_commands())
        self.layout.addWidget(scroll)

    def build_auto_commands(self):
        vbox_commands = QVBoxLayout()
        vbox_commands.setContentsMargins(0, 0, 0, 0)
        vbox_commands.addWidget(build_label_subtitle("Auto Commands"))

        hbox = QHBoxLayout()
        hbox.setSpacing(0)
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setAlignment(Qt.AlignmentFlag.AlignLeft)
        hbox.addWidget(QLabel("Tecla para Ativar"))
        hbox.addWidget(InputKeybind(self, self.key_base + KEY, True))
        vbox_commands.addLayout(hbox)

        hbox_commands = QHBoxLayout()
        hbox_commands.setContentsMargins(0, 0, 0, 0)

        vbox_text = QVBoxLayout()
        vbox_text.setSpacing(0)
        vbox_text.setContentsMargins(0, 0, 0, 0)
        vbox_text.addWidget(build_label_info("Commandos"))
        commands = CONFIG_FILE.read(self.key_base + COMMANDS)
        self.auto_commands.setPlainText(commands or "")
        self.auto_commands.textChanged.connect(lambda: CONFIG_FILE.update(self.key_base + COMMANDS, self.auto_commands.toPlainText()))
        vbox_text.addWidget(self.auto_commands)
        hbox_commands.addLayout(vbox_text)

        vbox_draft = QVBoxLayout()
        vbox_draft.setSpacing(0)
        vbox_draft.setContentsMargins(0, 0, 0, 0)
        vbox_draft.addWidget(build_label_info("Rascunho"))
        draft = CONFIG_FILE.read(self.key_base + DRAFT_COMMANDS)
        self.draft_auto_commands.setPlainText(draft or DEFAULT_DRAFT)
        self.draft_auto_commands.textChanged.connect(lambda: CONFIG_FILE.update(self.key_base + DRAFT_COMMANDS, self.draft_auto_commands.toPlainText()))
        vbox_draft.addWidget(self.draft_auto_commands)
        hbox_commands.addLayout(vbox_draft)

        vbox_commands.addLayout(hbox_commands)
        return vbox_commands
