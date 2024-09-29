import flet as ft

class Popup:
    def __init__(self, title: str):
        self.title = title

    def show(self, page: ft.Page):
        popup = ft.AlertDialog(
            title=ft.Text(self.title),
            on_dismiss=lambda e: page.overlay.remove(popup)
        )
        page.overlay.append(popup)
        popup.open = True
        page.update()

def main(page: ft.Page):
    page.title = "Popup Testing"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = 'dark'

    # Button for testing
    def on_button_click(e):
        Popup("Task Created!").show(page)
    button = ft.ElevatedButton("Create Task", on_click=on_button_click)
    page.add(button)
    page.update()  

if __name__ == "__main__":
    ft.app(target=main)
