import flet as ft

class TimeColumn(ft.Container):
    def makeTimes(self) -> None:
        for i in range(12 * 4):
            self.times.append(
                ft.Row(
                    controls=[
                            ft.Container(
                                content=ft.Text(
                                    value=f"----{i//4:02}:{(i%4)*15:02}----",
                                    size=10,
                                    style=ft.TextStyle(
                                        weight=ft.FontWeight.BOLD,
                                        italic=True,
                                        ),
                                    opacity=0.2,
                                ),
                                width=100,
                                height=50,
                                alignment=ft.alignment.Alignment(0, 1),
                                # border=ft.border.all(1, "grey"),
                            ),
                        ]
                    )
            )

    def __init__(self, height: int = 500):
        super().__init__()
        self.times = []
        self.makeTimes()
        self.content = ft.Column(
            controls=self.times,
            alignment=ft.CrossAxisAlignment.START,
            scroll=ft.ScrollMode.ALWAYS,
            expand=True,
        )
        # self.border=ft.border.all(1, "grey")
        self.height=500
