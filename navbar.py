import flet as ft

def create_navbar():
    # Create an input field for the search
    search_input = ft.TextField(
        hint_text="Search",
        width=300,  # Adjust width if necessary
        height=40,
        border_radius=23,
        bgcolor="#F5F3FF",  # Background color of the input field
        color="#288173",  # Input text color
        cursor_color="#288173",  # Color of the text cursor
        focused_border_color=ft.colors.TRANSPARENT,  # No border color when focused
        border_color=ft.colors.TRANSPARENT,  # No border color by default
        border=ft.Border(0),  # Remove any border
    )

    # Define the search bar container with the input field and icon
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
        bgcolor="#F5F3FF",  # Background color of the search bar
        padding=10,
    )

    # Return the search bar centered within a Column
    return ft.Column(
        controls=[
            ft.Row(
                controls=[search_bar],  # Add the search bar to the Row
                alignment=ft.MainAxisAlignment.CENTER,  # Center the Row
            )
        ],
        alignment=ft.MainAxisAlignment.START,
    )

# This allows you to run this file to see the search bar, but also import it in another file
if __name__ == "__main__":
    def main(page: ft.Page):
        navbar = create_navbar()
        page.add(navbar)

    ft.app(target=main)
