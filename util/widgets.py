import os
from PyQt6.QtWidgets import QLabel, QSpinBox, QBoxLayout, QWidget, QVBoxLayout, QSizePolicy, QHBoxLayout
from PyQt6.QtCore import QSize, Qt, QUrl
from PyQt6.QtGui import QPixmap, QDesktopServices

from config.app import APP_ICON_SIZE
from service.file import CONFIG_FILE, File
from util.number import clamp

ICON_BTN = QSize(24, 24)
ICON_STATUS = QSize(40, 40)


def build_painel(layout: QBoxLayout, title: str) -> QVBoxLayout:
    widget = QWidget()
    widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    widget.setObjectName("painel")
    painel = QVBoxLayout(widget)
    painel.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
    painel.setSpacing(8)
    painel.addWidget(QLabel(title))
    layout.addWidget(widget)
    return painel


def build_label_subtitle(text: str) -> QLabel:
    label = QLabel(text)
    label.setContentsMargins(0, 20, 0, 0)
    label.setStyleSheet("color: #d33e20;")
    return label


def build_label_info(text: str) -> QLabel:
    label = QLabel(text)
    label.setWordWrap(True)
    label.setStyleSheet("font-size: 12px; color: gray;")
    return label


def build_icon(icon: str, tooltip: str = None) -> QLabel:
    label = QLabel()
    if tooltip:
        label.setToolTip(tooltip)
    pixmap = QPixmap(icon)
    pixmap.scaledToWidth(APP_ICON_SIZE)
    label.setPixmap(pixmap)
    return label


def build_spinbox_percentage(percentage: str, label: str = None) -> QWidget:
    widget = QWidget()
    hbox = QHBoxLayout(widget)
    spinbox = QSpinBox()
    spinbox.setFixedWidth(80)
    spinbox.setRange(0, 100)
    spinbox.setSuffix("%")
    value = CONFIG_FILE.read(percentage)
    if value is not None:
        spinbox.setValue(clamp(value))
    spinbox.valueChanged.connect(lambda value: CONFIG_FILE.update(percentage, value))
    if label:
        hbox.addWidget(QLabel(label))
    hbox.addWidget(spinbox)
    return widget


def build_link_file(file: File):
    absolute_path = os.path.abspath(file.file_path)
    file_url = QUrl.fromLocalFile(absolute_path)
    link_label = QLabel()
    link_label.setText(f'<a href="{file_url.toString()}">{file.file_path}</a>')
    link_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
    link_label.setOpenExternalLinks(False)
    link_label.linkActivated.connect(lambda link: QDesktopServices.openUrl(QUrl(link)))
    return link_label
