import sys
from PyQt6.QtWidgets import QApplication
from main_window import MainWindow
from styles import STYLESHEET

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet(STYLESHEET)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())