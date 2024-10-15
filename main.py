import flet as ft
from frontend.views import view_handler
from backend.database_connector import Database

def main(page: ft.Page) -> None:
    page.title = "Locked-In"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = 'dark'
    database = Database()

    def route_change(route: ft.RouteChangeEvent) -> None:
        print(f"Current Route: {page.route}")
        page.views.clear()
        view = view_handler(page, database=database).get(page.route, ft.View(controls=[ft.Text("404 Not Found")]))
        page.views.append(view)
        page.update()

    def resize(event: ft.WindowEvent) -> None:
        page.update()

    page.on_route_change = route_change
    page.window.on_event = resize
    page.go('/login')

if __name__ == "__main__":
    ft.app(target=main)
