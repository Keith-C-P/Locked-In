import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) #find another way
import flet as ft
from frontend.dashboard_view import Dashboard
from frontend.authentication_view import Login_View, Signup_View
from backend.database_connector import Database

def view_handler(page: ft.Page, database: Database) -> dict[str, ft.View]:
    return {
        '/': Dashboard(page=page, database=database),
        '/login': ft.View(
            route='/login',
            controls=[
                Login_View(page=page, database=database),
            ],
        ),
        '/signup': ft.View(
            route='/signup',
            controls=[
                Signup_View(page=page, database=database),
            ],
        ),
    }

#TODO:
# [] Convert to ft.View class