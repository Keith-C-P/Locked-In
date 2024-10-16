import flet as ft

class SettingsPage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page

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

        # Settings page layout
        self.content = ft.Column(
            controls=self.create_settings_options(),
            alignment=ft.MainAxisAlignment.CENTER,  # Center vertically
            horizontal_alignment=ft.CrossAxisAlignment.START,  # Left-align
            spacing=20
        )
        self.alignment = ft.alignment.center
        self.bgcolor = "#323234"  # Background color

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
                on_hover=self.handle_hover,  # Hover effect handler
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
        container.content.color = "#b3ff00" if is_hover else ft.colors.WHITE  # Change text color on hover
        container.border = ft.border.only(
            bottom=ft.BorderSide(1, "#b3ff00" if is_hover else "transparent")
        )  # Add or remove green underline
        self.page.update()

    def navigate_to_settings(self, option: str):
        """Placeholder function to navigate to different settings pages."""
        print(f"Redirecting to {option} page...")
        # Implement actual navigation logic later.


def main(page: ft.Page):
    page.title = "Settings Page"
    page.bgcolor = "#323234"  # Background color

    # Add the settings page to the app
    page.add(SettingsPage(page))
    page.update()


# Run the Flet app
if __name__ == "__main__":
    ft.app(target=main)
