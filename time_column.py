import flet as ft

class TimeStamp(ft.Container):
    def __init__(self, time: str):
        super().__init__()
        self.content = ft.Text(
            value=time,
            size=10,
            style=ft.TextStyle(
                weight=ft.FontWeight.BOLD,
                # italic=True,
                ),
            opacity=0.3,
        )
        self.width=100
        self.height=50
        self.alignment=ft.alignment.Alignment(-1, 0)
        # self.border=ft.border.all(1, "grey") # Debugging

class TimeColumn(ft.Container):
    def makeTimes(self) -> None:
        # self.times.append(ft.Container(height=50)) # Empty space at the top
        for i in range((24 * 4)):
            self.times.append(
                TimeStamp(time=f"{i // 4:02}:{(i % 4) * 15:02} ——————")
            )

    def __init__(self):
        super().__init__()
        self.times = []
        self.makeTimes()
        self.content = ft.Column(
            controls=self.times,
            alignment=ft.CrossAxisAlignment.START,
            expand=True,
            spacing=0,
        )
        # self.border=ft.border.all(1, "grey")