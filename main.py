import sys

from gui.main_window import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFontDatabase, QFont
from config.app import APP_FONT, APP_FONT_SIZE, APP_STYLE


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(APP_STYLE)
    app.setFont(_build_font())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


def _build_font():
    font = QFontDatabase.addApplicationFont(APP_FONT)
    font_family = QFontDatabase.applicationFontFamilies(font)[0]
    return QFont(font_family, APP_FONT_SIZE)


if __name__ == "__main__":
    main()
