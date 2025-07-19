from datetime import datetime, timedelta
import webbrowser

from PySide6.QtWidgets import QWidget, QToolButton, QSpinBox, QHBoxLayout, QSizePolicy, QLabel, QSystemTrayIcon
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt

from config.app import APP_MAX_DELAY, APP_MIN_DELAY
from config.icon import ICON_NOTIFICATION
from gui.app_controller import APP_CONTROLLER, TIMER_PER_10_SEC
from service.config_file import CONFIG_FILE, DELAY, DELAY_ACTIVE, TIME
from service.servers_file import NAME, SERVERS_FILE
from util.number import clamp
from util.widgets import ICON_BTN


class InputNotification(QWidget):
    def __init__(self, parent: QWidget, key_seq: str, link) -> None:
        super().__init__(parent)
        self.key_seq = key_seq
        self.link = link
        self.layout = QHBoxLayout(self)
        self.toggle = self._build_toggle()
        self.spinbox = self._build_spinbox()
        self._config_layout()
        self._config_events()
        TIMER_PER_10_SEC.timeout.connect(self.send_notification)

    def send_notification(self):
        active = CONFIG_FILE.read(self.key_seq + DELAY_ACTIVE)
        if not active:
            return
        time = CONFIG_FILE.read(self.key_seq + TIME)
        if not time:
            return
        time_notification = datetime.fromisoformat(time)
        if datetime.now() < time_notification:
            return
        server_name = SERVERS_FILE.get_value(NAME)
        APP_CONTROLLER.tray_menu.showMessage(server_name, f"Já é possível votar novamente\nClique aqui e vote agora!", QSystemTrayIcon.Information, 7000)
        APP_CONTROLLER.tray_menu.messageClicked.connect(lambda: webbrowser.open(self.link))
        self.on_change_spinbox_value(self._get_delay())

    def _config_layout(self) -> None:
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.layout.setSpacing(5)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.toggle)
        self.layout.addWidget(self.spinbox)
        self.label_time = QLabel("")
        self.layout.addWidget(self.label_time)
        self.sync_time()

    def sync_time(self):
        time = CONFIG_FILE.read(self.key_seq + TIME)
        if self.toggle.isChecked() and not time:
            self.on_change_spinbox_value()
            time = CONFIG_FILE.read(self.key_seq + TIME)
        if self.toggle.isChecked() and time:
            self.label_time.setText(f"Próximo Lembrete: {self.get_date_format(time)}")
            self.label_time.setStyleSheet("color: gray;")

    def get_date_format(self, time):
        time = datetime.fromisoformat(time)
        return time.strftime("%d/%m/%Y %H:%M")

    def _config_events(self) -> None:
        self.toggle.toggled.connect(self._on_active_delay)
        self.spinbox.valueChanged.connect(self.on_change_spinbox_value)
        self._on_active_delay(self.toggle.isChecked())

    def on_change_spinbox_value(self, value=12):
        next_time = datetime.now() + timedelta(hours=value)
        CONFIG_FILE.update(self.key_seq + TIME, next_time.isoformat())
        CONFIG_FILE.update(self.key_seq + DELAY, value)
        self.sync_time()

    def _build_toggle(self) -> QToolButton:
        toggle = QToolButton()
        toggle.setCheckable(True)
        active = CONFIG_FILE.read(self.key_seq + DELAY_ACTIVE)
        toggle.setChecked(active if active else False)
        toggle.setIcon(QIcon(ICON_NOTIFICATION))
        toggle.setIconSize(ICON_BTN)
        return toggle

    def _build_spinbox(self) -> QSpinBox:
        spinbox = QSpinBox()
        spinbox.setRange(APP_MIN_DELAY, APP_MAX_DELAY)
        delay_s = self._get_delay()
        spinbox.setValue(delay_s)
        spinbox.setFixedWidth(95)
        spinbox.setSuffix("h")
        return spinbox

    def _get_delay(self) -> float:
        delay = CONFIG_FILE.read(self.key_seq + DELAY)
        if not delay:
            return 12
        if delay is not None:
            return clamp(delay, APP_MIN_DELAY, APP_MAX_DELAY)
        return delay

    def _on_active_delay(self, value: bool) -> None:
        self.spinbox.setVisible(value)
        self.label_time.setVisible(value)
        self.toggle.setToolTip(f"Notificação de evento - {"LIGADO" if value else "DESLIGADO"}")
        CONFIG_FILE.update(self.key_seq + DELAY_ACTIVE, value)
        self.sync_time()
