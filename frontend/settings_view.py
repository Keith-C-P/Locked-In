import flet as ft
from sidebar_component import Sidebar
from navbar_component import Navbar

class SettingsOption(ft.Container):
    def __init__(self, text: str, description: str):
        # Initialization
        super().__init__()
        self.text = ft.Container(
            ft.Text(
                value=f"{text}",
                size=18,
                color=ft.colors.WHITE,
                weight=ft.FontWeight.BOLD,
            ),
            padding=ft.padding.only(bottom=4),
            border_radius=0,
            on_click=lambda _: self.navigate_to_settings(text),
            on_hover=self.handle_hover,
        )
        self.description = ft.Text(
            value=f"{description}",
            size=12,
            color=ft.colors.WHITE54,
        )

        # Styling

        # Content
        self.content=ft.Column(
            controls=[
                self.text,
                self.description,
            ],
        )

    def handle_hover(self, e: ft.ControlEvent):
        container: ft.Container = e.control
        is_hover = e.data == "true"
        if is_hover:
            container.content.color = "#49a078"
            container.border = ft.border.only(
                bottom=ft.BorderSide(1, "#49a078")
            )
        else:
            container.content.color = ft.colors.WHITE
            container.border = ft.border.only(
                bottom=ft.BorderSide(1, "transparent")
            )
        self.update()

    def navigate_to_settings(self, option):
        print(f"Redirecting to {option} page...")
        # page.go(option)

class SettingsContent(ft.Container):
    def __init__(self):
        # Initialization
        super().__init__()
        self.settings_data = [
            ("Account Settings", "Change username, password, profile info, and other stuff"),
            ("Theme & Appearance", "Change how you want it to look"),
            ("Notifications", "Email, push, sound alerts, you decide"),
            ("Privacy", "Get 2-factor or control visibility because you never know"),
            ("Language", "Nothing to say about it, go ahead"),
            ("General Settings", "A bunch of other stuff like auto-update, time zone, data backup"),
            ("Help & Support", "Relax, just tell us if it doesn't work the way it's supposed to"),
            ("About & Legal", "Terms of service, app version, licenses, documentation")
        ]

        # Styling
        self.alignment = ft.MainAxisAlignment.START  # Left-align
        self.spacing = 20

        # Content
        self.content = ft.Column(
            controls=self.create_settings_options()
        )

    def create_settings_options(self)-> list[ft.Container]:
        """Creates a list of left-aligned clickable texts with descriptions."""
        settings_controls = []

        for setting, description in self.settings_data:
            settings_controls.append(
                SettingsOption(text=setting, description=description)
            )
        return settings_controls


class SettingsPage(ft.Container):
    def __init__(self, page: ft.Page):
        # Initialization
        super().__init__()
        self.page = page
        self.sidebar = Sidebar(page=page)
        self.navbar = Navbar(heading="Settings", subheading="Manage your account settings")
        # Styling
        self.expand = True

        # Content
        self.content=ft.Row(
            controls=[
                self.sidebar,
                ft.Container(
                    content=ft.Column(
                        controls=[
                            self.navbar,
                            SettingsContent(),
                        ],
                    ),
                    # border=ft.border.all(1, "#FF0000"), # Debugging
                    expand = True,
                ),
            ],
            expand=True
        )
        self.alignment = ft.alignment.center
        self.bgcolor = "#010b13"

def main(page: ft.Page):
    page.title = "Settings Page"
    page.bgcolor = "#010b13"

    page.add(SettingsPage(page))
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
