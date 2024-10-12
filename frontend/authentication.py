import flet as ft

def create_login_page(page: ft.Page):
    page.title = "Login"
    page.window_width = 800  # Set the width of the window
    page.window_height = 1000  # Set the height of the window

    # Left strip with solid color, adjusted width to match your dashboard's left strip
    left_strip = ft.Container(
        width=279,  # Width matching your dashboard
        height=page.window_height,  # Set height to cover the entire window
        bgcolor="#b3ff00",  # Use the specified color for the left strip
        content=ft.Column(  # Centering the text vertically in the strip
            [
                # Centered text for "Locked-In" with a border effect
                ft.Stack(
                    [
                        ft.Text(
                            spans=[
                                ft.TextSpan(
                                    "Locked-In",
                                    ft.TextStyle(
                                        size=35,  # Font size
                                        weight=ft.FontWeight.BOLD,
                                        foreground=ft.Paint(
                                            color=ft.colors.WHITE,
                                            stroke_width=5,  # Stroke width for the white border
                                            stroke_join=ft.StrokeJoin.ROUND,
                                            style=ft.PaintingStyle.STROKE,
                                        ),
                                    ),
                                ),
                            ],
                        ),
                        ft.Text(
                            spans=[
                                ft.TextSpan(
                                    "Locked-In",
                                    ft.TextStyle(
                                        size=35,  # Font size
                                        weight=ft.FontWeight.BOLD,
                                        color="#000000",  # Actual text color
                                    ),
                                ),
                            ],
                        ),
                    ],
                    alignment=ft.alignment.center,  # Center alignment for the Stack
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Center content vertically
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Center content horizontally
            spacing=20  # Space if there are other elements (currently none)
        )
    )

    # "Login to your Account" text
    login_text = ft.Text(
        value="Login to your Account",
        size=30,
        color="#ffffff",  # White text color
        weight=ft.FontWeight.BOLD
    )

    # Username and password text fields with labels on top
    username_field = ft.TextField(
        label="Username",  # Label above the box
        label_style=ft.TextStyle(size=12, color="#000000"),  # Smaller label size
        width=400,
        bgcolor="#ffffff",  # White background for text fields
        color="#000000",  # Black text color
    )

    password_field = ft.TextField(
        label="Password",  # Label above the box
        label_style=ft.TextStyle(size=12, color="#000000"),  # Smaller label size
        width=400,
        bgcolor="#ffffff",  # White background for text fields
        color="#000000",  # Black text color
        password=True,  # Hide password input
    )

    # Sign-in button
    sign_in_button = ft.ElevatedButton(
        text="Sign-In",
        style=ft.ButtonStyle(
            bgcolor="#323234",  # Button background color
            color="#ffffff",  # Button text color
        ),
        width=150,
        height=50,
        on_click=lambda _: validate_login(username_field.value, password_field.value)
    )

    # Message label for login feedback
    message_label = ft.Text(
        value="",
        color="#ff0000"  # Default color for error message (red)
    )

    def validate_login(username, password):
        # Basic validation for demonstration
        if username == "admin" and password == "password":
            message_label.value = "Login successful!"
            message_label.color = "#00ff00"  # Success message color (green)
        else:
            message_label.value = "Invalid username or password."
            message_label.color = "#ff0000"  # Error message color (red)
        page.update()

    # Right content layout (login form)
    right_content = ft.Column(
        [
            login_text,
            username_field,
            password_field,
            sign_in_button,
            message_label
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,  # Align vertically in the middle
        horizontal_alignment=ft.CrossAxisAlignment.CENTER  # Align horizontally
    )

    # Main layout with left strip and right content
    main_layout = ft.Row(
        [
            left_strip,
            ft.Container(  # Right-side content container
                content=right_content,
                expand=True,  # Right-side content takes the remaining space
                alignment=ft.alignment.center,  # Center content
            )
        ],
        expand=True  # Row takes full width of the screen
    )

    # Add main layout to the page
    page.add(main_layout)

# Run the Flet app
if __name__ == "__main__":
    ft.app(target=create_login_page)
