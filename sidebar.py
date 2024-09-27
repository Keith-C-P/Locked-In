import flet as ft

def create_sidebar():
    # Sidebar container with specified dimensions and colors
    sidebar = ft.Container(
        content=ft.Column(
            controls=[
                # "Locked-In" label at the top
                ft.Text(
                    value="Locked-In",
                    size=35,  # Updated size
                    color="#E7F5C6",  # Color code for the text
                    font_family="Helvetica",  # Updated font to Helvetica
                    weight=ft.FontWeight.BOLD,  # Set to bold
                ),
                # Thin line below the label
                ft.Divider(
                    height=1,
                    color="#BFD1E5",  # Color code for the thin line
                ),
                # Create a gap between title and buttons
                ft.Container(height=20),  # Gap between title and buttons
                # Create buttons with hover effects
                create_button("Dashboard"),
                ft.Container(height=10),  # Gap between buttons
                create_button("Objectives"),
                ft.Container(height=10),  # Gap between buttons
                create_button("Profile"),
                ft.Container(height=10),  # Gap between buttons
                create_button("Progress"),
                ft.Container(height=10),  # Gap between buttons
                create_button("Settings"),
            ],
            alignment="start",
        ),
        width=279,
        height=953,
        bgcolor="#32323E",  # Background color of the sidebar
        padding=20,
        border_radius=ft.BorderRadius(40, 0, 40, 0),  # Rounded corners: top left and bottom left
    )

    return sidebar

def create_button(text):
    # Button creation with hover effects
    return ft.TextButton(
        text=text,
        style=ft.ButtonStyle(
            color="#E7F5C6",  # Default text color for button
            bgcolor=ft.colors.TRANSPARENT,  # Make background transparent
        ),
        on_hover=lambda e: e.control.update(
            bgcolor="#E7F5C6" if e.data else ft.colors.TRANSPARENT,  # Highlight color on hover
            color="#288173" if e.data else "#E7F5C6"  # Text color on hover
        ),
    )

# Testing the sidebar component
if __name__ == "__main__":
    def main(page: ft.Page):
        page.title = "Dashboard"
        page.add(create_sidebar())

    ft.app(target=main)