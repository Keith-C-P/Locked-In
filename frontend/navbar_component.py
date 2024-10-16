import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) #find another way
from backend.database_connector import Database, User
import flet as ft

class ProfileDropdown(ft.Container):
    def __init__(self, username: str = "John Doe") -> None:
        # Initialization
        super().__init__()

        # Styling
        self.width = 250
        # self.bgcolor = "#E7F5C6"
        self.border_radius = ft.BorderRadius(23, 23, 23, 23)
        self.padding = 20
        self.alignment = ft.alignment.center
        # self.border = ft.border.all(1, "#FF0000") # Debugging

        # Content
        self.content = ft.Row(
            controls=[
                ft.IconButton(ft.icons.PERSON, bgcolor="#E7F5C6", icon_color="#b3ff00"),
                ft.Text(f"{username}", size=20, color="#E7F5C6"),
                ft.IconButton(ft.icons.ARROW_DROP_DOWN, icon_color="#b3ff00"),
            ]
        )

class SearchBar(ft.TextField):
    def __init__(self) -> None:
        # Initialization
        super().__init__()

        # Styling
        self.hint_text="Search"
        self.width=300
        self.height=40
        self.border_radius=23
        self.bgcolor="#E7F5C6"
        self.color="#b3ff00"
        self.cursor_color="#b3ff00"
        self.focused_border_color=ft.colors.TRANSPARENT
        self.border_color=ft.colors.TRANSPARENT
        self.border = ft.Border(0)
        self.suffix = ft.IconButton(
            ft.icons.SEARCH,
            # bgcolor=ft.colors.RED, # Debugging
            icon_color="#b3ff00",
            icon_size=20,
            # width=20,
            on_click=lambda _: print("Search button pressed"),
        )

class Navbar(ft.Container):
    def __init__(self, heading: str = "", subheading: str = "", username: str | None = None) -> None:
        #Initialization
        super().__init__(height=100)

        # Styling
        self.height = 100
        # self.border=ft.border.all(1, "#FF0000") # Debugging

        # Content
        self.content=ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(f"{heading}", size=35, color="#E7F5C6"),
                            ft.Text(f"{subheading}", size=15, color="#E7F5C6"),
                        ],
                    ),
                    # border=ft.border.all(1, "#FF0000") # Debugging
                ),
                SearchBar(),
                ProfileDropdown(username=username),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            expand=True,
        )

def main(page: ft.Page):
    page.theme_mode = "dark"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    navbar = Navbar(page=page)
    page.add(
        navbar,
    )

if __name__ == "__main__":
    ft.app(target=main)
