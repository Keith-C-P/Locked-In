import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) #find another way
import flet as ft
from frontend.timeline.timeline import TimeLine
from frontend.sidebar_component import Sidebar
from frontend.navbar_component import Navbar
from backend.database_connector import Database, Task, User

class Dashboard(ft.Container):
    def __init__(self, page: ft.Page , database: Database):
        super().__init__()
        self.Times = TimeLine(database=database)
        self.Side = Sidebar(page=page)
        self.Nav = Navbar(heading="Dashboard", subheading="Todays Progress", username = database.logged_in_user.username if database.logged_in_user else None)

        # Styling
        # self.border=ft.border.all(1, "#FF0000") # Debugging
        self.expand = True

        self.content=ft.Row(
            controls=[
                self.Side,
                ft.Container(
                    content=ft.Column(
                        controls=[
                            self.Nav,
                            self.Times,
                        ],
                    ),
                    # border=ft.border.all(1, "#FF0000"), # Debugging
                    expand = True
                )
            ],
            expand=True
        )

def main(page: ft.Page) -> None:
    page.title = "Locked-In"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = 'dark'
    dashboard_view = Dashboard(page=page, database=Database())

    page.add(
        dashboard_view
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=main)