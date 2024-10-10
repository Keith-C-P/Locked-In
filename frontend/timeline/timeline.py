import flet as ft
from frontend.timeline.task_layer import Task_Layer
from frontend.timeline.time_layer import Time_Layer

class TimeLine(ft.Container):
    def __init__(self, min_height: int = 50, time_division: int = 15, header_height: int = 50,  height: int = 900, width: int = None):
        # Initialization
        super().__init__()
        self.time_division = time_division
        self.min_height = min_height
        self.task_layer = Task_Layer()
        self.header_height = header_height

        # Styling
        if width is None:
            self.expand = True
        else:
            self.width = width
        self.bgcolor = "#1E1E1E"
        self.border_radius = ft.border_radius.all(10)
        self.height = height
        # self.border = ft.border.all(1, "grey") # Debugging
        self.scroll = ft.ScrollMode.HIDDEN

        # Content
        self.content = ft.Column(
            controls=[
                ft.Stack(
                    controls=[
                        Time_Layer(min_height=self.min_height, time_division=self.time_division),
                        Task_Layer(min_height=self.min_height, time_division=self.time_division, header_height=self.header_height, padding=10),
                    ],
                    clip_behavior=None,
                ),
            ],
            scroll=ft.ScrollMode.HIDDEN,
        )

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