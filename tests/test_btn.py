from PyQt6.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton,
    QVBoxLayout
)
from PyQt6.QtCore import Qt

class InputWithFloatingBadge(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Badge Flutuante")
        self.resize(300, 100)

        # Layout principal
        layout = QVBoxLayout(self)

        # Campo de entrada
        self.input = QLineEdit(self)
        self.input.setPlaceholderText("Digite algo...")
        self.input.setFixedHeight(40)
        layout.addWidget(self.input)

        # Botão como badge flutuante
        self.badge_button = QPushButton("✖", self)
        self.badge_button.setFixedSize(20, 20)
        self.badge_button.setStyleSheet("""
            QPushButton {
                background-color: red;
                color: white;
                border: none;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: darkred;
            }
        """)
        self.badge_button.clicked.connect(self.input.clear)

        # Coloca o botão manualmente posicionado depois do resize
        self.update_badge_position()

        # Atualiza posição sempre que o widget for redimensionado
        self.input.resizeEvent = lambda e: self.update_badge_position()

    def update_badge_position(self):
        # Posiciona o botão no canto direito interno do QLineEdit
        margin = 4
        x = self.input.x() + self.input.width() - self.badge_button.width() - margin
        y = self.input.y() + (self.input.height() - self.badge_button.height()) // 2
        self.badge_button.move(x, y)

app = QApplication([])
window = InputWithFloatingBadge()
window.show()
app.exec()
