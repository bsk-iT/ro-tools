from typing import Any, List
import psutil

from PyQt6.QtWidgets import QVBoxLayout, QComboBox, QPushButton, QSizePolicy, QWidget, QLabel, QHBoxLayout
from PyQt6.QtCore import Qt
from config.app import APP_ICON_SIZE
from service.memory import MEMORY
from service.servers_file import SERVERS_FILE


class CboxProcess(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.layout: QVBoxLayout = QVBoxLayout(self)
        self.cbox = self._build_cbox_process()
        self.btn = self._build_btn_refresh()
        self.allowed_process = self._list_allowed_process()
        self.process_options = []
        self._config_layout()
        self._update_cbox_process()

    def _config_layout(self) -> None:
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.setSpacing(5)
        self.layout.addWidget(QLabel("Selecione o processo:"))
        hbox = QHBoxLayout()
        hbox.addWidget(self.cbox)
        hbox.addWidget(self.btn)
        self.layout.addLayout(hbox)

    def _build_cbox_process(self) -> QComboBox:
        cbox = QComboBox()
        cbox.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        cbox.setMinimumWidth(200)
        cbox.currentIndexChanged.connect(self._on_change_process)
        return cbox

    def _build_btn_refresh(self) -> QPushButton:
        btn_refresh = QPushButton("⟳")
        btn_refresh.setFixedWidth(APP_ICON_SIZE)
        btn_refresh.clicked.connect(self._update_cbox_process)
        btn_refresh.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        return btn_refresh

    def _on_change_process(self, index) -> None:
        if not self.process_options:
            MEMORY.process.close_process()
            return
        process = self.process_options[index]
        MEMORY.update_process(process["name"], process["pid"])
        self.focusNextChild()

    def _list_allowed_process(self) -> List[str]:
        server_file = SERVERS_FILE.read(None)
        return [server.lower() for server in server_file]

    def _update_cbox_process(self) -> None:
        self.process_options = self._list_process_options()
        self.cbox.clear()
        self.cbox.addItems(self._label_options())
        self.focusNextChild()

    def _list_process_options(self) -> List[Any]:
        options = []
        for proc in psutil.process_iter(["pid", "name"]):
            if proc.info["name"].lower() in self.allowed_process:
                options.append(proc.info)
        return options

    def _label_options(self) -> List[str]:
        return [f"{proc['name']} - {proc['pid']}" for proc in self.process_options]
