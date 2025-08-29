# ทำให้โฟลเดอร์ pages เป็น Python package
from .home_page import HomePage
from .dashboard_page import DashboardPage
from .settings_page import SettingsPage
from .profile_page import ProfilePage

__all__ = ['HomePage', 'DashboardPage', 'SettingsPage', 'ProfilePage']