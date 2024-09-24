import flet as ft
from task import Task
from time_column import TimeColumn
import datetime as dt

class TimeLine(ft.Card):
    def addTask(self, taskName: str) -> None:
        self.availableTasks.append(taskName)
        self.task.controls.append(Task(taskName))
        self.update()

    def __init__(self):
        super().__init__()
        self.timesColumn: ft.Container = TimeColumn()
        self.availableTasks: list[str] = []
        self.task_input: ft.TextField = ft.TextField(
            hint_text="Add a Task",
            width=300,
        )

        self.content = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(
                                dt.datetime.now().strftime("%A"),
                                size=20,
                            ),
                        ft.Container(width=230),
                        self.task_input,
                        ft.IconButton(icon="add",
                            alignment=ft.alignment.Alignment(1, 0),
                            # on_click=lambda _: self.addTask("Task"),
                            )
                    ],
                ),
                ft.Container(
                    content = ft.Row(
                        controls=[
                            self.timesColumn,
                            ft.VerticalDivider(
                                width=1,
                                color="red",
                                opacity=1,
                                thickness=100,
                                ),
                            ft.Container(
                                ft.Column(
                                    [
                                        Task("Task 1"),
                                        Task("Task 2"),
                                    ],
                                    alignment=ft.MainAxisAlignment.START,
                                ),
                                border=ft.border.all(1, "grey"),
                                height=500,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                ),
            ],
            scroll=ft.ScrollMode.ALWAYS,
            on_scroll_interval=0,
            width = 700,
            # expand=True,
        )
