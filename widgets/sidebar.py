from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel, QListWidget, QListWidgetItem
from PyQt6.QtCore import QSize, Qt

class Sidebar(QFrame):
    def __init__(self):
        super().__init__()
        self.setObjectName("sidebar")
        self.setMinimumWidth(200)
        self.setMaximumWidth(300)
        
        sidebar_layout = QVBoxLayout(self)
        sidebar_layout.setSpacing(0)
        sidebar_layout.setContentsMargins(0, 0, 0, 0)
        
        # ชื่อแอปพลิเคชัน
        title_label = QLabel("แอปของฉัน")
        title_label.setObjectName("sidebar_title")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setMinimumHeight(60)
        sidebar_layout.addWidget(title_label)
        
        # รายการนำทาง
        self.sidebar_list = QListWidget()
        self.sidebar_list.setObjectName("sidebar_list")
        self.sidebar_list.setSpacing(2)
        sidebar_layout.addWidget(self.sidebar_list)
        
        # เพิ่มพื้นที่ยืดหยุ่นที่ด้านล่าง
        sidebar_layout.addStretch()
    
    def add_item(self, name, icon):
        """เพิ่มไอเท็มไปยังรายการแถบด้านข้าง"""
        item = QListWidgetItem(f"{icon} {name}")
        item.setSizeHint(QSize(100, 40))
        self.sidebar_list.addItem(item)