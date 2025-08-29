from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        title = QLabel("หน้าหลัก")
        title.setFont(QFont("Tahoma", 16))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        # เพิ่มเนื้อหาตัวอย่าง
        for i in range(1, 6):
            layout.addWidget(QLabel(f"นี่คือรายการเนื้อหาหน้าหลัก {i}"))
        
        layout.addStretch()