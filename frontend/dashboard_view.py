import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) #find another way
import flet as ft
from frontend.timeline_component.timeline import TimeLine
from frontend.sidebar_component import Sidebar
from frontend.navbar_component import Navbar
from frontend.popup_component import TaskDialogue
from backend.database_connector import Database, Task, User

class Dashboard(ft.View):
    def __init__(self, page: ft.Page , database: Database):
        super().__init__()
        self.route = "/"
        self.page = page
        self.database = database
        self.Times = TimeLine(database=database)
        self.Side = Sidebar(page=page)
        self.Nav = Navbar(heading="Dashboard", subheading="Todays Progress", username = database.logged_in_user.username if database.logged_in_user else None)

        # Styling
        # self.border=ft.border.all(1, "#FF0000") # Debugging
        self.expand = True

        self.controls=[
            ft.Row(
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
                    ),
                ],
                expand=True
            ),
            ft.FloatingActionButton(
                icon=ft.icons.ADD,
                bgcolor="#49a078",
                foreground_color="#dce1de",
                on_click=lambda e: page.open(TaskDialogue(page=page, database=database, task_layer=self.Times.task_layer, rehydrate_task_layer=self.Times.rehydrate_task_layer)),
            ),
            # ft.TextButton(
            #     text="Rehydrate",
            #     on_click=lambda e: self.Times.rehydrate_task_layer(),
            #     # bgcolor="#49a078",
            #     # foreground_color="#dce1de",
            # ),
        ]

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