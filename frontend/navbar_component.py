import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))  # find another way
from backend.database_connector import Database, User
import flet as ft

class ProfileDropdown(ft.Container):
    def __init__(self, username: str | None = None) -> None:
        # Initialization
        super().__init__()

        # Styling
        self.width = 250
        # self.bgcolor = "#dce1de"
        self.border_radius = ft.BorderRadius(23, 23, 23, 23)
        self.padding = 20
        self.alignment = ft.alignment.center
        # self.border = ft.border.all(1, "#FF0000") # Debugging

        # Content
        self.content = ft.Row(
            controls=[
                ft.IconButton(ft.icons.PERSON, bgcolor="#dce1de", icon_color="#49a078"),
                ft.Text(f"{username if username  else 'Samba'}", size=20, color="#dce1de"),
                ft.IconButton(ft.icons.ARROW_DROP_DOWN, icon_color="#49a078"),
            ]
        )

class SearchBar(ft.TextField):
    def __init__(self) -> None:
        # Initialization
        super().__init__()

        # Styling
        self.hint_text = "Search"
        self.hint_text_color = "#9cc5a1"  # Set the hint text color here
        self.width = 300
        self.height = 40
        self.border_radius = 23
        self.bgcolor = "#dce1de"
        self.color = "#49a078"
        self.cursor_color = "#49a078"
        self.focused_border_color = ft.colors.TRANSPARENT
        self.border_color = ft.colors.TRANSPARENT
        self.border = ft.Border(0)
        self.suffix = ft.IconButton(
            ft.icons.SEARCH,
            # bgcolor=ft.colors.RED, # Debugging
            icon_color="#288173",
            icon_size=25,
            # width=20,
            on_click=lambda _: print("Search button pressed"),
        )

class Navbar(ft.Container):
    def __init__(self, heading: str = "", subheading: str = "", username: str | None = None) -> None:
        # Initialization
        super().__init__(height=100)

        # Styling
        self.height = 100
        # self.border = ft.border.all(1, "#FF0000") # Debugging

        # Content
        self.content = ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text(f"{heading}", size=35, color="#dce1de"),
                            ft.Text(f"{subheading}", size=15, color="#dce1de"),
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
