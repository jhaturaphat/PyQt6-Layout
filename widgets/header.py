from PyQt6.QtWidgets import QFrame, QHBoxLayout, QLabel, QPushButton

class Header(QFrame):
    def __init__(self, title="หน้าหลัก"):
        super().__init__()
        self.setObjectName("header")
        self.setMinimumHeight(62)
        
        header_layout = QHBoxLayout(self)
        header_layout.setContentsMargins(20, 0, 20, 0)
        
        # ชื่อเรื่อง
        self.header_title = QLabel(title)
        self.header_title.setObjectName("header_title")
        header_layout.addWidget(self.header_title)
        
        # วิดเจ็ตด้านขวา
        header_layout.addStretch()
        
        # ปุ่มค้นหา
        search_btn = QPushButton("🔍 ค้นหา")
        search_btn.setFlat(True)
        header_layout.addWidget(search_btn)
        
        # ปุ่มการแจ้งเตือน
        notification_btn = QPushButton("🔔")
        notification_btn.setFlat(True)
        header_layout.addWidget(notification_btn)
        
        # ข้อมูลผู้ใช้
        user_btn = QPushButton("👤 สมชาย ใจดี")
        user_btn.setFlat(True)
        header_layout.addWidget(user_btn)
    
    def set_title(self, title):
        """ตั้งค่าชื่อเรื่อง"""
        self.header_title.setText(title)