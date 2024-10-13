import flet as ft

class Navbar(ft.Column):
    def __init__(self):
        super().__init__()
        self.width = 412.3
        self.height = 40
        # self.bgcolor = "#E7F5C6"
        self.padding = 20
        self.border_radius = ft.BorderRadius(23, 23, 23, 23)

        search_input = ft.TextField(
            hint_text="Search",
            width=300,  # Adjust width if necessary
            height=40,
            border_radius=23,
            # bgcolor="#E7F5C6",  # Background color of the input field
            color="#000000FF",  # Input text color
            cursor_color="#288173",  # Color of the text cursor
            focused_border_color=ft.colors.TRANSPARENT,  # No border color when focused
            border_color=ft.colors.TRANSPARENT,  # No border color by default
            border=ft.Border(0),  # Remove any border
        )

        search_bar = ft.Container(
            content=ft.Row(
                controls=[
                    search_input,  # Add the input field here
                    ft.Icon(ft.icons.SEARCH, color="#288173"),  # Magnifier icon
                ],
                alignment="spaceBetween",
                vertical_alignment=ft.MainAxisAlignment.CENTER,
            ),
            width=412.3,
            height=40,
            border_radius=23,
            bgcolor="#E7F5C6",  # Background color of the search bar
            padding=10,
        )

        self.controls = [
            ft.Row(
                controls=[search_bar],  # Add the search bar to the Row
                alignment=ft.MainAxisAlignment.CENTER,  # Center the Row
            )
        ]
        self.alignment = ft.MainAxisAlignment.START,

# This allows you to run this file to see the search bar, but also import it in another file
if __name__ == "__main__":
    def main(page: ft.Page):
        navbar = Navbar()
        page.add(navbar)
        page.theme_mode = "dark"

    ft.app(target=main)
