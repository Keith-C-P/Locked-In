import flet as ft

class Popup:
    def __init__(self, title: str):
        self.title = title

    def show(self, page: ft.Page): #popup thingie
        popup = ft.AlertDialog(
            title=ft.Text(self.title),
            on_dismiss=lambda e: page.overlay.remove(popup)
        )
        page.overlay.append(popup)
        popup.open = True
        page.update()
#you can use this popup for multiple things, not just the task layer