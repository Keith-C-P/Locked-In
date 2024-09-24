import flet as ft

class Task(ft.Container):
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
            expand=True,
        )
        # self.width=150
        # self.height=50