import flet as ft
from frontend.timeline_component.task_layer import Task_Layer
from frontend.timeline_component.time_layer import Time_Layer
from backend.database_connector import User, Database

class TimeLine(ft.Container):
    def __init__(self,
        database: Database = None,
        page: ft.Page = None,
        min_height: int = 50,
        time_division: int = 15,
        header_height: int = 50,
        height: int = 900,
        width: int = None,
        user: User = User(
            uuid=1,
            username="JohnDoe",
            privilege="ADMIN",
            password="password"
        )
    ):
        # Initialization
        super().__init__()
        self.time_division = time_division
        self.min_height = min_height
        self.task_layer = Task_Layer(min_height=self.min_height, time_division=self.time_division, database=database)
        self.header_height = header_height

        # Styling
        self.expand = True
        # self.bgcolor = "#1E1E1E"
        self.bgcolor = "#00000000"
        self.height = height
        # self.border_radius = ft.border_radius.all(10)
        # self.border = ft.border.all(1, "grey") # Debugging
        self.scroll = ft.ScrollMode.HIDDEN

        # Content
        self.content = ft.Column(
            controls=[
                ft.Stack(
                    controls=[
                        Time_Layer(min_height=self.min_height, time_division=self.time_division),
                        self.task_layer,
                    ],
                    clip_behavior=None,
                ),
            ],
            scroll=ft.ScrollMode.HIDDEN,
        )

    def rehydrate_task_layer(self) -> None:
        self.task_layer.rehydrate_task_list()
        self.update()
        # print("Rehydrated Task Layer from TimeLine")

def main(page : ft.Page) -> None:
    page.title = "Timeline Test"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = 'dark'
    timelineStacked = TimeLine(
        time_division=15,
        min_height=50,
        header_height=70,
        height=900,
        width=1000,
    )

    page.add(
        timelineStacked,
    )

if __name__ == "__main__":
    ft.app(target=main)


#TODO:
# [x] Rebuild the task list after a task is added
# [x] Sort the tasks by start time
# [x] Give task delete functionality
# [x] Fix positioning of tasks