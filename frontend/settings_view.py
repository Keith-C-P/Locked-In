import flet as ft
from frontend.sidebar_component import Sidebar
from frontend.navbar_component import Navbar
from typing import List

class SettingsOption(ft.Container):
    def __init__(self, text: str, description: str):
        super().__init__()
        self.text_control = ft.Text(
            value=text,
            size=18,
            color=ft.colors.WHITE,
            weight=ft.FontWeight.BOLD,
        )
        
        self.description_control = ft.Text(
            value=description,
            size=12,
            color=ft.colors.WHITE54,
        )

        super().__init__(
            content=ft.Column(
                controls=[self.text_control, self.description_control],
            ),
            on_hover=self.handle_hover,  # Attach hover here, not inside text
            border=ft.border.only(bottom=ft.BorderSide(1, "transparent")),
            padding=ft.padding.symmetric(vertical=10)
        )

    def handle_hover(self, e: ft.ControlEvent):
        is_hover = e.data == "true"
        self.text_control.color = "#49a078" if is_hover else ft.colors.WHITE
        self.border = ft.border.only(bottom=ft.BorderSide(1, "#49a078" if is_hover else "transparent"))
        self.update()

    def navigate_to_settings(self, option):
        print(f"Redirecting to {option} page...")

class SettingsContent(ft.Container):
    def __init__(self):
        super().__init__()
        self.alignment = ft.MainAxisAlignment.START
        self.spacing = 20

        super().__init__(
            content=ft.Column(
                controls=self.create_settings_options(),
                expand=True
            )
        )

    def create_settings_options(self) -> List[ft.Container]:
        settings_controls = []

        settings_data = [
            ("Account Settings", "Change username, password, profile info, and other stuff"),
            ("Theme & Appearance", "Change how you want it to look"),
            ("Notifications", "Email, push, sound alerts, you decide"),
            ("Privacy", "Get 2-factor or control visibility because you never know"),
            ("Language", "Nothing to say about it, go ahead"),
            ("General Settings", "A bunch of other stuff like auto-update, time zone, data backup"),
            ("Help & Support", "Relax, just tell us if it doesn't work the way it's supposed to"),
            ("About & Legal", "Terms of service, app version, licenses, documentation")
        ]

        for setting, description in settings_data:
            settings_controls.append(
                SettingsOption(text=setting, description=description)
            )
        return settings_controls

class SettingsPage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.sidebar = Sidebar(page=page)
        self.navbar = Navbar(heading="Settings", subheading="Manage your account settings")

        super().__init__(
            content=ft.Row(
                controls=[
                    ft.Container(  # Sidebar Container with rounded corners
                        content=self.sidebar,
                        width=280,
                        height=page.height,  # Ensure full height for sidebar
                        bgcolor="#32323E",
                        border_radius=ft.border_radius.only(
                            top_left=40, bottom_left=40  # Rounded corners on the left
                        ),
                        alignment=ft.alignment.top_left,
                    ),
                    ft.Container(  # Main content area
                        content=ft.Column(
                            controls=[self.navbar, SettingsContent()],
                            alignment=ft.MainAxisAlignment.START,
                            spacing=30
                        ),
                        expand=True,
                        padding=20,
                        bgcolor="#010b13"
                    ),
                ],
                expand=True,
            )
        )
        self.bgcolor = "#010b13"

def main(page: ft.Page):
    page.title = "Settings Page"
    page.bgcolor = "#010b13"
    page.update()

    # Set page size or ensure the sidebar fills the page
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    page.vertical_alignment = ft.MainAxisAlignment.STRETCH

    page.add(SettingsPage(page))
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
