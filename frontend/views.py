import os
import sys
import flet as ft
from frontend.dashboard_view import Dashboard
from frontend.authentication_view import Login_View, Signup_View
from frontend.mess_menu_view import MessMenuPage # Ensure you have this view implemented
from frontend.settings_view import SettingsPage
from backend.database_connector import Database

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))  # Ensure this is set properly

def view_handler(page: ft.Page, database: Database) -> dict[str, ft.View]:
    return {
        '/': Dashboard(page=page, database=database),
        '/login': ft.View(
            route='/login',
            controls=[Login_View(page=page, database=database)],
        ),
        '/signup': ft.View(
            route='/signup',
            controls=[Signup_View(page=page, database=database)],
        ),
        '/dashboard': ft.View(
            route='/dashboard',
            controls=[Dashboard(page=page, database=database)],  # Replace with your actual dashboard view
        ),
        '/mess-menu': ft.View(
            route='/mess-menu',
            controls=[MessMenuPage(page=page)],
        ),
        '/settings': ft.View(
            route='/settings',
            controls=[SettingsPage(page=page)],
        ),
    }


#TODO:
# [] Convert to ft.View class