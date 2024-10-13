import flet as ft
from frontend.dashboard_view import Dashboard
from frontend.authentication_view import create_login_page

def view_handler(page: ft.Page) -> dict[str : ft.View]:
    return {
        '/': ft.View(
            route='/',
            controls= [
                Dashboard(),
            ],
        ),
    }