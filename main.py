import flet as ft
from timeline import TimeLine, Task

def main(page: ft.Page) -> None:
    page.title = "APP Project"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = 'dark'

    Times = TimeLine()

    page.add(
        ft.Column(
            [
                Times,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


if __name__ == "__main__":
    ft.app(target=main)