import flet as ft
from task_layer import Task_Layer, Task
from time_layer import Time_Layer
class TimeLine(ft.Container):
    def __init__(self, min_height: int = 50, time_division: int = 15, height: int = 900, width: int = 1000):
        # Initialization
        super().__init__()
        self.time_division = time_division
        self.min_height = min_height
        self.width = width
        self.height = height
        self.task_layer = Task_Layer()

        # Styling
        self.border_radius = ft.border_radius.all(10)
        self.border = ft.border.all(1, "grey")
        self.scroll = ft.ScrollMode.HIDDEN

        # Content
        self.content = ft.Column(
            controls=[
                ft.Stack(
                    controls=[
                        Time_Layer(min_height=self.min_height, time_division=self.time_division),
                        Task_Layer(min_height=self.min_height, time_division=self.time_division, header_height=50),
                    ],
                    clip_behavior=None,
                ),
            ],
            scroll=ft.ScrollMode.HIDDEN,
        )

        # Test Data
        self.task_layer.add_task(Task(name="Task 1", start_time = "01:15", end_time="2:00"))
        self.task_layer.add_task(Task(name="Task 2", start_time = "02:15", end_time="5:00"))
        self.task_layer.add_task(Task(name="Task 2", start_time = "05:00", end_time="5:15"))

def main(page : ft.Page) -> None:
    page.title = "Timeline Test"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = 'dark '
    timelineStacked = TimeLine(
        time_division=15,
        min_height=50,
        height=900,
        width=1000
    )
    page.add(
        timelineStacked,
    )

if __name__ == "__main__":
    ft.app(target=main)