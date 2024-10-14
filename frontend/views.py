import flet as ft
from frontend.dashboard_view import Dashboard
from frontend.authentication_view import LoginPage, SignupPage

def view_handler(page: ft.Page) -> dict[str, ft.View]:
    return {
        '/': ft.View(
            route='/',
            controls=[
                Dashboard(),
            ],
        ),
        '/login': ft.View(
            route='/login',
            controls=[
                LoginPage(page, switch_to_signup=lambda: page.go('/signup')),
            ],
        ),
        '/signup': ft.View(
            route='/signup',
            controls=[
                SignupPage(page, switch_to_login=lambda: page.go('/login')),
            ],
        ),
    }
