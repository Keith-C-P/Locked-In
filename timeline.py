import flet as ft
from task import Task, TaskColumn
from time_column import TimeColumn
import datetime as dt

class TimeLine(ft.Container):
    def __init__(self):
        super().__init__()
        self.Time_Column: ft.Container = TimeColumn()
        self.availableTasks: list[str] = []
        self.width = 1500
        # self.border = ft.border.all(1) #Debugging
        self.border_radius = ft.BorderRadius(10, 0, 10, 0)
        # self.margin=ft.margin.all(100)
        # self.padding=ft.padding.all(100)
        # self.bgcolor = "#E7F5C6"
        # self.width = 1000
        # self.height = 900
        self.task_input: ft.TextField = ft.TextField(
            hint_text="Add a Task",
            width=300,
        )

        self.Task_Column = TaskColumn()
        self.Task_Column.add_task(Task(name="Task 1", start_time = "01:15", end_time="2:00"))
        self.Task_Column.add_task(Task(name="Task 2", start_time = "02:15", end_time="5:00"))


        self.content = ft.Column(
            [
                ft.Text(
                    dt.datetime.now().strftime("%A"),
                    size=20,
                ),
                ft.Divider(),
                ft.Container(
                    content = ft.Row(
                        controls=[
                            self.Time_Column,
                            ft.VerticalDivider(
                                width=1,
                                color="red",
                                opacity=1,
                                thickness=100,
                                ),
                            self.Task_Column,
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    # height=800,
                ),
            ],
            scroll=ft.ScrollMode.HIDDEN,
            on_scroll_interval=0,
            width = 1000,
            height = 900,
            # expand=True,
        )
