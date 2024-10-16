import flet as ft
from sidebar_component import Sidebar  # Correct the import to point directly to sidebar_component

class SettingsContent(ft.Column):
    def __init__(self):
        super().__init__()

        # List of settings options and their descriptions
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

        # Add settings options to the layout
        self.controls = self.create_settings_options()
        self.alignment = ft.MainAxisAlignment.START  # Left-align
        self.spacing = 20

    def create_settings_options(self):
        """Creates a list of left-aligned clickable texts with descriptions."""
        settings_controls = []

        for option, description in self.settings_data:
            # Main clickable option text inside a container for hover effect
            option_container = ft.Container(
                content=ft.Text(
                    value=option,
                    size=18,
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                ),
                padding=ft.padding.only(bottom=4),
                border_radius=0,
                on_click=lambda e, opt=option: self.navigate_to_settings(opt),
                on_hover=self.handle_hover,  # Ensure this is correctly set
            )

            # Description text below the option
            description_text = ft.Text(
                value=description,
                size=12,
                color=ft.colors.WHITE54,  # Slightly faded color for descriptions
            )
            
            # Add both the option container and its description to the controls list
            settings_controls.append(option_container)
            settings_controls.append(description_text)

        return settings_controls

    def handle_hover(self, e):
        """Handle hover state, applying green underline and text color."""
        container: ft.Container = e.control
        is_hover = e.data == "true"  # Hover in if true, hover out if false
        container.content.color = "#49a078" if is_hover else ft.colors.WHITE  # Change text color on hover
        container.border = ft.border.only(
            bottom=ft.BorderSide(1, "#49a078" if is_hover else "transparent")
        )  # Add or remove green underline

        # Update the page to reflect changes
        self.page.update()  # Ensure the page updates after hover effects

    def navigate_to_settings(self, option: str):
        """Placeholder function to navigate to different settings pages."""
        print(f"Redirecting to {option} page...")
        # Implement actual navigation logic later.


class SettingsPage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

        # Sidebar to take full height
        self.sidebar = Sidebar(page=page)  # Pass page to Sidebar

        # Settings page layout
        self.content = ft.Row(
            controls=[
                self.sidebar,
                SettingsContent(),  # Adjust this to ensure it's in the right layout
            ],
            expand=True
        )
        self.alignment = ft.alignment.center
        self.bgcolor = "#010b13"  # Background color



def main(page: ft.Page):
    page.title = "Settings Page"
    page.bgcolor = "#010b13"  # Background color

    # Add the settings page to the app
    page.add(SettingsPage(page))
    page.update()


# Run the Flet app
if __name__ == "__main__":
    ft.app(target=main)
