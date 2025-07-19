from functools import lru_cache
import os
from PySide6.QtWidgets import QLabel, QSpinBox, QBoxLayout, QWidget, QVBoxLayout, QSizePolicy, QHBoxLayout, QWidgetItem, QScrollArea, QFrame, QPushButton, QRadioButton
from PySide6.QtCore import QSize, Qt, QUrl
from PySide6.QtGui import QPixmap, QDesktopServices, QStandardItem, QFont, QColor, QIcon, QCursor

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
    painel.setSpacing(20)
    painel.addWidget(QLabel(title))
    layout.addWidget(widget)
    return painel


def build_label_subtitle(text: str) -> QLabel:
    label = QLabel(text)
    label.setContentsMargins(0, 5, 0, 0)
    label.setStyleSheet("color: #d33e20;")
    return label


def get_color_by_id(_id) -> QColor:
    color = QColor()
    for _type in ["attack", "defense", "song", "element"]:
        if _id in [f"{_type}_1", f"{type}_1"]:
            color.setRgb(72, 133, 237)
            return color
        if _id in [f"{_type}_2", f"{type}_2"]:
            color.setRgb(123, 104, 238)
            return color
        if _id in [f"{_type}_3", f"{type}_3"]:
            color.setRgb(199, 80, 255)
            return color
        if _id in [f"{_type}_4", f"{type}_4"]:
            color.setRgb(255, 99, 171)
            return color
        if _id in [f"{_type}_fire", f"{_type}_fire"]:
            color.setRgb(255, 107, 74)
            return color

        if _id in [f"{_type}_water", f"{_type}_water"]:
            color.setRgb(77, 166, 255)
            return color

        if _id in [f"{_type}_ground", f"{_type}_ground"]:
            color.setRgb(167, 140, 107)
            return color

        if _id in [f"{_type}_wind", f"{_type}_wind"]:
            color.setRgb(181, 227, 227)
            return color

        if _id in [f"{_type}_holy", f"{_type}_holy"]:
            color.setRgb(255, 217, 106)
            return color

        if _id in [f"{_type}_dark", f"{_type}_dark"]:
            color.setRgb(138, 108, 207)
            return color

        if _id in [f"{_type}_ghost", f"{_type}_ghost"]:
            color.setRgb(204, 204, 255)
            return color
    return None


def build_scroll_vbox(heigth=300):
    content_widget = QWidget()
    scroll = QScrollArea()
    scroll.setMinimumHeight(heigth)
    scroll.setWidgetResizable(True)
    scroll.setWidget(content_widget)
    vbox = QVBoxLayout(content_widget)
    vbox.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
    return (vbox, scroll)


def build_radio_btn(text):
    radio = QRadioButton(text)
    radio.setStyleSheet("font-size: 12px;")
    return radio


def build_action_badge():
    widget = QWidget()
    widget.setFixedSize(30, 40)
    widget.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
    layout = QHBoxLayout(widget)
    layout.setAlignment(Qt.AlignmentFlag.AlignBottom)
    layout.setContentsMargins(0, 0, 0, 0)
    return (widget, layout)


def build_badge_btn(parent, icon):
    btn = QPushButton(parent)
    btn.setFixedSize(20, 20)
    btn.move(0, 0)
    btn.setIcon(QIcon(icon))
    btn.setIconSize(QSize(10, 10))
    btn.setContentsMargins(0, 0, 0, 0)
    btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
    return btn


def build_label_info(text: str) -> QLabel:
    label = QLabel(text)
    label.setWordWrap(True)
    label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
    label.setStyleSheet("font-size: 12px; color: gray;")
    return label


def build_label(text: str, font=12, word_wrap=True) -> QLabel:
    label = QLabel(text)
    label.setWordWrap(word_wrap)
    label.setStyleSheet(f"font-size: {font}px;")
    return label


def build_icon(icon: str, tooltip: str = None, size=25, parent: QWidget = None) -> QLabel:
    label = QLabel(parent)
    if tooltip:
        label.setToolTip(tooltip)
    label.setPixmap(QPixmap(icon).scaled(size, size))
    return label


def build_hr() -> QFrame:
    line = QFrame()
    line.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
    line.setFrameShape(QFrame.Shape.HLine)
    line.setFrameShadow(QFrame.Shadow.Sunken)
    return line


@lru_cache(maxsize=None)
def clear_layout(layout):
    new_layout = None
    if isinstance(layout, QWidgetItem):
        new_layout = layout.layout()
    if not new_layout and layout:
        return clean_widget(layout.widget())
    execute_clean_layout(new_layout)


def execute_clean_layout(layout):
    while layout and layout.count():
        item = layout.takeAt(0)
        if item is None:
            continue
        child_layout = item.layout()
        if child_layout:
            clear_layout(child_layout)
            continue
        clean_widget(item.widget())


def clean_widget(widget):
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

def build_spinbox_cells(cell_prop: str, label: str = None) -> QWidget:
    widget = QWidget()
    hbox = QHBoxLayout(widget)
    hbox.setSpacing(0)
    hbox.setContentsMargins(0,0,0,0)
    spinbox = QSpinBox()
    spinbox.setFixedWidth(130)
    spinbox.setRange(1, 99)
    spinbox.setSuffix(" células")
    value = CONFIG_FILE.read(cell_prop)
    if value is not None:
        spinbox.setValue(clamp(value))
    spinbox.valueChanged.connect(lambda value: CONFIG_FILE.update(cell_prop, value))
    if label:
        hbox.addWidget(QLabel(label))
    hbox.addWidget(spinbox)
    return widget


def build_cbox_category(model, label):
    if label is None:
        return
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


def build_link(link, name = None):
    link_label = QLabel()
    link_label.setText(f'<a href="{link}">{name or link}</a>')
    link_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
    link_label.setOpenExternalLinks(False)
    link_label.linkActivated.connect(lambda link: QDesktopServices.openUrl(QUrl(link)))
    return link_label


def build_link_icon(icon_path: str, url: str, size=25) -> QLabel:
    return ClickableLabel(icon_path, url, size)


def is_interception_available():
    try:
        from interception import Interception

        return len(Interception.devices) > 0
    except Exception as e:
        return False


class ClickableLabel(QLabel):
    def __init__(self, icon_path, url, size):
        super().__init__()
        self.setPixmap(QPixmap(icon_path).scaled(size, size, Qt.AspectRatioMode.KeepAspectRatio))
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.url = url

    def mousePressEvent(self, event):
        QDesktopServices.openUrl(QUrl(self.url))
