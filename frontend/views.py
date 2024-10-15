import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) #find another way
import flet as ft
from frontend.dashboard_view import Dashboard
from frontend.authentication_view import Login_View, Signup_View
from backend.database_connector import Database, User

def view_handler(page: ft.Page, database: Database, user: User = User(username="John Doe", password="12345678", uuid=0, privilege="USER", )) -> dict[str, ft.View]:
    return {
        '/': ft.View(
            route='/',
            controls=[
                Dashboard(page=page, database=database),
            ],
        ),
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
