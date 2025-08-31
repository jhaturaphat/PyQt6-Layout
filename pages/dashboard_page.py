from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QApplication
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class DashboardPage(QWidget):
    def __init__(self):
        super().__init__()        
        layout = QVBoxLayout(self)
        title = QLabel("แดชบอร์ด")
        title.setFont(QFont("Tahoma", 16))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        # เพิ่มเนื้อหาตัวอย่าง
        for i in range(1, 6):
            layout.addWidget(QPushButton(f"ปุ่มแดชบอร์ด {i}"))
        
        layout.addStretch()


# Run Test
if __name__ == "__main__":
    app = QApplication([])
    window = DashboardPage()
    window.show()
    app.exec()