import flet as ft
from frontend.views import view_handler

def main(page: ft.Page) -> None:
    page.title = "Locked-In"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = 'dark'

    def route_change(route: ft.RouteChangeEvent) -> None:
        print(f"Current Route: {page.route}")
        page.views.clear()

        # Get the view based on the current route
        view = view_handler(page).get(page.route, ft.View(controls=[ft.Text("404 Not Found")]))

        # Append the view to the page's views
        page.views.append(view)
        page.update()

    page.on_route_change = route_change
    page.go('/')  # Navigate to the home page

if __name__ == "__main__":
    ft.app(target=main)
