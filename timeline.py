import flet as ft

class Task(ft.Card):
    def __init__(self, taskName: str):
        self.taskName = taskName
        super().__init__()
        self.content = ft.Row(
            controls=[
                ft.Container(width=1),
                ft.Text(
                    value=self.taskName,
                    size=20,
                ),
                ft.IconButton(
                    icon="delete",
                ),
            ],
            # expand=True,
        )

class TimeLine(ft.Card):
    def addTask(self, taskName: str) -> None:
        self.availableTasks.append(taskName)
        self.tasks.controls.append(Task(taskName))
        self.update()

    def makeTimes(self) -> None:
        times = []
        for i in range(12 * 4):
            times.append(ft.Row(
                        controls=[
                                ft.Container(width=1),
                                ft.Text(
                                value=f"{i//4:02}:{(i%4)*15:02}",
                                size=20
                                ),
                                Task("Task"),
                            ]
                        )
            )
            times.append(ft.Divider(thickness=1, color="grey", opacity=0))
        self.tasks = ft.Column(times)

    def __init__(self):
        super().__init__()
        self.tasks: ft.Column = None
        self.availableTasks: list[str] = []
        self.task_input: ft.TextField = ft.TextField(
            hint_text="Add a Task",
            width=300,
        )

        self.makeTimes()

        self.content = ft.Column(
            [
                ft.Row(
                    [
                        ft.Text("Timeline",
                            size=20
                            ),
                        ft.Container(width=230),
                        self.task_input,
                        ft.IconButton(icon="add",
                            alignment=ft.alignment.Alignment(1, 0),
                            on_click=lambda _: self.addTask("Task"),
                            )
                    ]
                ),
                self.tasks
            ],
            scroll=ft.ScrollMode.AUTO,
            on_scroll_interval=0,
            width = 700,
            # expand=True,
        )
