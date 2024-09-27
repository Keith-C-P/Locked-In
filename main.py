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
            content = ft.Column(
                controls= [
                    ft.Text("Dashboard", size=35),
                    ft.Text("Todays Progress", size=15),
                ],
                alignment=ft.MainAxisAlignment.START,
                # horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
            alignment=ft.alignment.center_left
        ),
        Search,
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