import flet as ft
from task import Task, TaskColumn
from time_column import TimeColumn
import datetime as dt

class TimeLine(ft.Card):
    def __init__(self):
        super().__init__()
        self.Time_Column: ft.Container = TimeColumn()
        self.availableTasks: list[str] = []
        self.margin=ft.margin.all(20)
        self.padding=ft.padding.all(20)
        self.task_input: ft.TextField = ft.TextField(
            hint_text="Add a Task",
            width=300,
        )

        self.Task_Column = TaskColumn()
        self.Task_Column.add_task(Task(name="Task 1", start_time = "01:15", end_time="2:00"))
        self.Task_Column.add_task(Task(name="Task 2", start_time = "02:15", end_time="5:00"))


        self.content = ft.Column(
            [
                # ft.Row(
                #     [
                #         ft.Text(
                #                 dt.datetime.now().strftime("%A"),
                #                 size=20,
                #             ),
                #         ft.Container(width=570),
                #         self.task_input,
                #         ft.IconButton(icon="add",
                #             alignment=ft.alignment.Alignment(1, 0),
                #             # on_click=lambda _: self.addTask("Task"),
                #             )
                #     ],
                #     spacing=0,
                # ),
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
            height=900,
            # expand=True,
        )
