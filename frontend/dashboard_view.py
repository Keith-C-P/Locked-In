import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) #find another way
import flet as ft
from frontend.timeline.timeline import TimeLine
from frontend.sidebar_component import Sidebar
from frontend.navbar_component import Navbar

class Dashboard(ft.Container):
    def __init__(self):
        super().__init__()
        self.Times = TimeLine()
        self.Side = Sidebar()
        self.Search = Navbar()

        self.content=ft.Column(
            controls=[ft.Container(
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
                        self.Search,
                        ft.Container(width=500),
                        ft.IconButton(ft.icons.PERSON, bgcolor="#E7F5C6", icon_color="#288173"),
                        ft.Text("John Doe", size=20, color="#E7F5C6"),
                        ft.IconButton(ft.icons.ARROW_DROP_DOWN, icon_color="#288173"),
                    ]
                ),
                alignment=ft.alignment.center_left
            ),
            ft.Container(
                content=ft.Row(
                    controls= [
                        self.Side,
                        self.Times,
                    ]
                ),
            ),
            ft.FloatingActionButton(icon="add", ),
            ],
        )


def main(page: ft.Page) -> None:
    page.title = "Locked-In"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = 'dark'
    dashboard_view = Dashboard()

    page.add(
        dashboard_view
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=main)