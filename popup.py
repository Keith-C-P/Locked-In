import flet as ft

class Popup(ft.Container):
    def __init__(self, title: str):
        super().__init__()
        self.title = title

    def show(self, page: ft.Page):
        popup = ft.AlertDialog(
            modal=True,
            content=ft.Container(
                content=ft.Text(
                    self.title,
                    text_align=ft.TextAlign.CENTER,
                    color="#E7F5C6",
                    font_family="Helvetica",
                    size=20,
                    weight=ft.FontWeight.BOLD
                ),
                alignment=ft.alignment.center,
                padding=20,  
                width=200, 
                height=100,  
                border_radius=15,  
                bgcolor="#555555"
            ),
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

    button = ft.IconButton(icon=ft.icons.ADD, on_click=on_button_click)
    page.add(button)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
