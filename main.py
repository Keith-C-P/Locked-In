import flet as ft
from timeline import TimeLine
from sidebar import Sidebar
from navbar import Navbar

def main(page: ft.Page) -> None:
    page.title = "APP Project"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = 'dark'
    Times = TimeLine()
    Side = Sidebar()
    Search = Navbar()
    # page.bgcolor = "#E7F5C6"

    page.add(
        ft.Container(
            content = ft.Row(
                controls=[
                    ft.Column(
                    controls= [
                        ft.Text("Dashboard", size=35, color="#E7F5C6"),
                        ft.Text("Todays Progress", size=15, color="#E7F5C6"),
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    ),
                    ft.Container(width=500),
                    Search,
                    ft.Container(width=500),
                    ft.IconButton(ft.icons.PERSON, bgcolor="#E7F5C6", icon_color="#288173"),
                    ft.Text("John Doe", size=20, color="#E7F5C6"),
                    ft.IconButton(ft.icons.ARROW_DROP_DOWN, icon_color="#288173"),
                ]
            ),
            alignment=ft.alignment.center_left
        ),
        # Search,
        ft.Container(
            content=ft.Row(
                controls= [
                    Side,
                    Times,
                ]
            ),
        ),
        ft.FloatingActionButton(icon="add", ),
    )


if __name__ == "__main__":
    ft.app(target=main)