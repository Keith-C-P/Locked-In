import flet as ft
import datetime as dt

class Header(ft.Container):
    def __init__(self, header_height: int = 50):
        super().__init__()
        self.height = header_height
        self.padding = ft.padding.all(10)
        # self.border = ft.border.all(1, "red") # Debugging
        self.content = ft.Row(
            controls=[
                ft.Text(
                    dt.datetime.now().strftime("%A"),
                    size=20,
                ),
            ],
            alignment=ft.CrossAxisAlignment.START,
            expand=True,
        )

class TimeStamp(ft.Container):
    def __init__(self, time: str, min_height: int = 50):
        # Initialization
        super().__init__()

        # Styling
        self.height=min_height
        # self.border=ft.border.all(1, "red") # Debugging

        # Content
        self.content = ft.Row(
            controls=[
                ft.Text(
                    value=time,
                    size=10,
                    style=ft.TextStyle(
                        weight=ft.FontWeight.BOLD,
                        # italic=True,
                        ),
                    opacity=0.3,
                ),
                ft.Container(
                    ft.Divider(
                        color="grey",
                        thickness=.1,
                    ),
                    expand=True,
                ),
            ],
            alignment=ft.CrossAxisAlignment.START,
        )

class Time_Layer(ft.Container):
    def __init__(self, time_division: int = 15, min_height: int = 50, header_height: int = 50):
        assert time_division > 0, "Time division must be greater than 0"
        assert min_height > 0, "Minimum height must be greater than 0"
        # Initialization
        super().__init__()
        self.time_division = time_division
        self.min_height = min_height
        self.header_height = header_height
        self.times = []

        # Styling
        self.padding = ft.padding.only(10,0,10,0)

        # Content
        self.__make_times()
        self.content = ft.Column(
            controls=[
                Header(header_height=self.header_height),
                ft.Divider(
                    thickness=1,
                    color="grey",
                    opacity=1,
                ),
                *self.times,
            ],
            alignment=ft.CrossAxisAlignment.START,
            expand=True,
            spacing=0,
        )

    def __make_times(self) -> None:
        sum = 0
        for i in range(0, (24 * 60), self.time_division):
            # print(i)
            time = f"{i // 60:02}:{i % 60:02}" if i != 0 else f"{i // 60:02}:00" # Divide by 0 error
            self.times.append(
                TimeStamp(time=time, min_height=self.min_height)
            )
            sum += 1