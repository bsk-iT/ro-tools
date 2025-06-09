from functools import lru_cache
import os
from PyQt6.QtWidgets import QLabel, QSpinBox, QBoxLayout, QWidget, QVBoxLayout, QSizePolicy, QHBoxLayout, QWidgetItem
from PyQt6.QtCore import QSize, Qt, QUrl
from PyQt6.QtGui import QPixmap, QDesktopServices, QStandardItem, QFont

from config.app import APP_ICON_SIZE
from service.config_file import CONFIG_FILE
from service.file import File
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


def build_label(text: str, font=12, word_wrap=True) -> QLabel:
    label = QLabel(text)
    label.setWordWrap(word_wrap)
    label.setStyleSheet(f"font-size: {font}px;")
    return label


def build_icon(icon: str, tooltip: str = None, size=APP_ICON_SIZE, parent: QWidget = None) -> QLabel:
    label = QLabel(parent)
    if tooltip:
        label.setToolTip(tooltip)
    pixmap = QPixmap(icon)
    pixmap.scaledToWidth(size)
    label.setPixmap(pixmap)
    return label


@lru_cache(maxsize=None)
def clear_layout(layout):
    if isinstance(layout, QWidgetItem):
        layout = layout.layout()
    while layout and layout.count():
        item = layout.takeAt(0)
        if item is None:
            continue
        child_layout = item.layout()
        if child_layout:
            clear_layout(child_layout)
            continue
        widget = item.widget()
        if widget:
            widget.setParent(None)
            widget.deleteLater()


def build_spinbox_percentage(percentage_prop: str, label: str = None) -> QWidget:
    widget = QWidget()
    hbox = QHBoxLayout(widget)
    spinbox = QSpinBox()
    spinbox.setFixedWidth(80)
    spinbox.setRange(0, 100)
    spinbox.setSuffix("%")
    value = CONFIG_FILE.read(percentage_prop)
    if value is not None:
        spinbox.setValue(clamp(value))
    spinbox.valueChanged.connect(lambda value: CONFIG_FILE.update(percentage_prop, value))
    if label:
        hbox.addWidget(QLabel(label))
    hbox.addWidget(spinbox)
    return widget


def build_cbox_category(model, label):
    item = QStandardItem(label)
    item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEnabled)
    item.setFont(QFont(None, weight=QFont.Weight.Bold))
    model.appendRow(item)


def build_link_file(file: File):
    absolute_path = os.path.abspath(file.file_path)
    file_url = QUrl.fromLocalFile(absolute_path)
    link_label = QLabel()
    link_label.setText(f'<a href="{file_url.toString()}">{file.file_path}</a>')
    link_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
    link_label.setOpenExternalLinks(False)
    link_label.linkActivated.connect(lambda link: QDesktopServices.openUrl(QUrl(link)))
    return link_label
