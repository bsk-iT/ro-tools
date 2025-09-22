import sys
import os
import ctypes

from gui.main_window import MainWindow
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtGui import QFontDatabase, QFont
from config.app import APP_FONT, APP_FONT_SIZE, APP_STYLE


def is_admin():
    """Verifica se o programa está rodando como administrador"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def run_as_admin():
    """Reinicia o programa como administrador"""
    try:
        if sys.argv[0].endswith('.py'):
            # Se for executado via Python
            ctypes.windll.shell32.ShellExecuteW(
                None, 
                "runas", 
                sys.executable, 
                f'"{os.path.abspath(sys.argv[0])}"',
                None, 
                1
            )
        else:
            # Se for executável compilado
            ctypes.windll.shell32.ShellExecuteW(
                None, 
                "runas", 
                sys.executable, 
                " ".join(sys.argv[1:]),
                None, 
                1
            )
    except Exception as e:
        print(f"Erro ao executar como administrador: {e}")
        return False
    return True


def main():
    # Verificar se está rodando como administrador
    if not is_admin():
        print("RO Tools precisa de privilegios de administrador para acessar a memoria do jogo.")
        print("Reiniciando como administrador...")

        # Tentar reiniciar como administrador
        if run_as_admin():
            sys.exit(0)  # Encerrar a instância atual
        else:
            # Se falhar, mostrar mensagem de erro
            app = QApplication(sys.argv)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setWindowTitle("RO Tools - Erro de Permissão")
            msg.setText("O RO Tools precisa ser executado como administrador!")
            msg.setInformativeText(
                "Para acessar a memória do jogo, é necessário executar como administrador.\n\n"
                "Clique com o botão direito no arquivo e selecione 'Executar como administrador'."
            )
            msg.exec()
            sys.exit(1)
    
    print("✅ Executando como administrador!")
    
    app = QApplication(sys.argv)
    app.setStyleSheet(APP_STYLE)
    app.setFont(_build_font())
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


def _build_font():
    try:
        font = QFontDatabase.addApplicationFont(APP_FONT)
        font_families = QFontDatabase.applicationFontFamilies(font)
        if font_families and len(font_families) > 0:
            font_family = font_families[0]
            return QFont(font_family, APP_FONT_SIZE)
        else:
            print("⚠️ Fonte customizada não encontrada, usando fonte padrão")
            return QFont("Arial", APP_FONT_SIZE)
    except Exception as e:
        print(f"⚠️ Erro ao carregar fonte: {e}")
        return QFont("Arial", APP_FONT_SIZE)


if __name__ == "__main__":
    main()
