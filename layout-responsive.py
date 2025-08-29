import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QPushButton, QLabel, QStackedWidget, QListWidget, QListWidgetItem,
    QFrame, QSizePolicy
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("แอปพลิเคชัน PyQt6 Responsive")
        self.setGeometry(100, 100, 1200, 800)
        
        # สร้างวิดเจ็ตกลาง
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # เลย์เอาต์หลัก
        main_layout = QHBoxLayout(central_widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # สร้างแถบด้านข้าง
        self.sidebar = self.create_sidebar()
        main_layout.addWidget(self.sidebar)
        
        # สร้างพื้นที่เนื้อหาด้านขวา
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setSpacing(0)
        right_layout.setContentsMargins(0, 0, 0, 0)
        
        # สร้างแถบหัวเรื่อง
        self.header = self.create_header()
        right_layout.addWidget(self.header)
        
        # สร้างสแต็กเนื้อหา
        self.content_stack = QStackedWidget()
        right_layout.addWidget(self.content_stack)
        
        # เพิ่มหน้าไปยังสแต็กเนื้อหา
        self.pages = {}
        self.add_page("หน้าหลัก", "🏠", HomePage())
        self.add_page("แดชบอร์ด", "📊", DashboardPage())
        self.add_page("การตั้งค่า", "⚙️", SettingsPage())
        self.add_page("โปรไฟล์", "👤", ProfilePage())
        
        main_layout.addWidget(right_widget, 1)  # พื้นที่ด้านขวาใช้พื้นที่ที่เหลือ
        
        # ตั้งค่าหน้าเริ่มต้น
        self.sidebar_list.setCurrentRow(0)
        
    def create_sidebar(self):
        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setMinimumWidth(200)
        sidebar.setMaximumWidth(300)
        sidebar.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        
        sidebar_layout = QVBoxLayout(sidebar)
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
        self.sidebar_list.currentRowChanged.connect(self.change_page)
        sidebar_layout.addWidget(self.sidebar_list)
        
        # เพิ่มพื้นที่ยืดหยุ่นที่ด้านล่าง
        sidebar_layout.addStretch()
        
        return sidebar
        
    def create_header(self):
        header = QFrame()
        header.setObjectName("header")
        header.setMinimumHeight(60)
        header.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(20, 0, 20, 0)
        
        # ชื่อเรื่อง
        self.header_title = QLabel("หน้าหลัก")
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
        
        return header
        
    def add_page(self, name, icon, widget):
        # เพิ่มไปยังรายการแถบด้านข้าง
        item = QListWidgetItem(f"{icon} {name}")
        item.setSizeHint(QSize(100, 40))
        self.sidebar_list.addItem(item)
        
        # เพิ่มไปยังสแต็ก
        self.content_stack.addWidget(widget)
        self.pages[name] = self.content_stack.count() - 1
        
    def change_page(self, index):
        if index >= 0:
            self.content_stack.setCurrentIndex(index)
            # อัปเดตชื่อเรื่อง
            item_text = self.sidebar_list.item(index).text()
            page_name = item_text.split(" ", 1)[1]  # ลบไอคอน
            self.header_title.setText(page_name)


# คลาสสำหรับหน้าเนื้อหาต่างๆ
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


class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        title = QLabel("การตั้งค่า")
        title.setFont(QFont("Tahoma", 16))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        # เพิ่มเนื้อหาตัวอย่าง
        for i in range(1, 6):
            layout.addWidget(QLabel(f"ตัวเลือกการตั้งค่า {i}"))
        
        layout.addStretch()


class ProfilePage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        title = QLabel("โปรไฟล์")
        title.setFont(QFont("Tahoma", 16))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        # เพิ่มเนื้อหาตัวอย่าง
        for i in range(1, 6):
            layout.addWidget(QLabel(f"ข้อมูลโปรไฟล์ {i}"))
        
        layout.addStretch()


# สไตล์ชีต
STYLESHEET = """
#sidebar {
    background-color: #2c3e50;
    border: none;
}

#sidebar_title {
    background-color: #34495e;
    color: white;
    font-size: 18px;
    font-weight: bold;
}

#sidebar_list {
    background-color: #2c3e50;
    color: white;
    border: none;
    outline: none;
}

#sidebar_list::item {
    padding: 10px;
    border-bottom: 1px solid #34495e;
}

#sidebar_list::item:selected {
    background-color: #3498db;
    color: white;
}

#sidebar_list::item:hover {
    background-color: #34495e;
}

#header {
    background-color: #ecf0f1;
    border-bottom: 1px solid #bdc3c7;
}

#header_title {
    font-size: 20px;
    font-weight: bold;
}

QPushButton {
    padding: 5px 10px;
    border-radius: 4px;
}

QPushButton:hover {
    background-color: #d6dbdf;
}
"""


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet(STYLESHEET)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())