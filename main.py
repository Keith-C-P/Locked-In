import flet as ft
from timeline import TimeLine

def main(page: ft.Page) -> None:
    page.title = "APP Project"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = 'dark'
    Times = TimeLine()

    page.add(
        Times
    )


if __name__ == "__main__":
    ft.app(target=main)