from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QStackedWidget
)
from widgets.sidebar import Sidebar
from widgets.header import Header
from pages.home_page import HomePage
from pages.dashboard_page import DashboardPage
from pages.settings_page import SettingsPage
from pages.profile_page import ProfilePage

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
        self.sidebar = Sidebar()
        main_layout.addWidget(self.sidebar)
        
        # สร้างพื้นที่เนื้อหาด้านขวา
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setSpacing(0)
        right_layout.setContentsMargins(0, 0, 0, 0)
        
        # สร้างแถบหัวเรื่อง
        self.header = Header("หน้าหลัก")
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
        
        # เชื่อมต่อสัญญาณ
        self.sidebar.sidebar_list.currentRowChanged.connect(self.change_page)
        
        # ตั้งค่าหน้าเริ่มต้น
        self.sidebar.sidebar_list.setCurrentRow(0)
        
    def add_page(self, name, icon, widget):
        # เพิ่มไปยังรายการแถบด้านข้าง
        self.sidebar.add_item(name, icon)
        
        # เพิ่มไปยังสแต็ก
        self.content_stack.addWidget(widget)
        self.pages[name] = self.content_stack.count() - 1
        
    def change_page(self, index):
        if index >= 0:
            self.content_stack.setCurrentIndex(index)
            # อัปเดตชื่อเรื่อง
            item_text = self.sidebar.sidebar_list.item(index).text()
            page_name = item_text.split(" ", 1)[1]  # ลบไอคอน
            self.header.set_title(page_name)