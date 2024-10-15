import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) #find another way
import flet as ft
from backend.database_connector import Database, Task, User

class UsernameField(ft.TextField):
    def __init__(self):
        super().__init__()
        self.label="Username"
        self.label_style=ft.TextStyle(size=12, color="#000000")
        self.width=400
        self.bgcolor="#ffffff"
        self.color="#000000"

class PasswordField(ft.TextField):
    def __init__(self, label):
        super().__init__()
        self.label=label
        self.label_style=ft.TextStyle(size=12, color="#000000")
        self.width=400
        self.bgcolor="#ffffff"
        self.color="#000000"
        self.password=True
        self.text_align=ft.TextAlign.LEFT
        self.suffix=ft.IconButton(
            icon=ft.icons.REMOVE_RED_EYE,
            tooltip="Show password",
            on_click=lambda _: self.toggle_show_password(),
            icon_size=20,
            padding=0,
            splash_radius=0
        )

    def toggle_show_password(self):
        self.password = not self.password
        self.update()

class LeftStrip(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.width=279
        self.height=page.window.height
        self.bgcolor="#b3ff00"
        self.alignment=ft.alignment.center
        self.content=ft.Column(
            [
                ft.Stack(
                    [
                        ft.Text(
                            spans=[
                                ft.TextSpan(
                                    "Locked-In",
                                    ft.TextStyle(
                                        size=35,
                                        weight=ft.FontWeight.BOLD,
                                        foreground=ft.Paint(
                                            color=ft.colors.WHITE,
                                            stroke_width=5,
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
                                        size=35,
                                        weight=ft.FontWeight.BOLD,
                                        color="#000000",
                                    ),
                                ),
                            ],
                        ),
                    ],
                    alignment=ft.alignment.center,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )

class PageToggle(ft.Text):
    def __init__(self, normal, hyperlink, on_click):
        super().__init__()
        self.color="#ffffff"
        self.spans=[
            ft.TextSpan(
                f"{normal}",
            ),
            ft.TextSpan(
                f"{hyperlink}",
                ft.TextStyle(
                    color=ft.colors.BLUE,
                    decoration=ft.TextDecoration.UNDERLINE,
                ),
                on_click=on_click
            ),
        ]

class Login_View(ft.Container):
    def __init__(self, page: ft.Page, database: Database):
        super().__init__()
        self.page = page
        self.conn = database
        header = ft.Text(
            value="Login to your Account",
            size=40,
            color="#ffffff",
            weight=ft.FontWeight.BOLD
        )
        self.username_field = UsernameField()
        self.password_field = PasswordField("Password")
        sign_in_button = ft.ElevatedButton(
            text="Login",
            style=ft.ButtonStyle(
                bgcolor="#323234",
                color="#ffffff",
            ),
            width=150,
            height=50,
            on_click=lambda _: self.validate_login(self.username_field.value, self.password_field.value)
        )
        toggle_page = PageToggle(
            normal = "New here? Why not ",
            hyperlink = "Sign Up",
            on_click=lambda _: page.go('/signup')
        )
        self.message_label = ft.Text(value="", color="#ff0000")
        self.main_content = ft.Column(
            [
                header,
                self.username_field,
                self.password_field,
                sign_in_button,
                toggle_page,
                self.message_label
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
        self.content = ft.Row(
            [
                LeftStrip(page=page),
                ft.Container(
                    content=self.main_content,
                    expand=True,
                    alignment=ft.alignment.center,
                    height=page.window.height,
                )
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
        )

    def validate_login(self, username: str, password: str):
        assert isinstance(username, str) and isinstance(password, str) # Type checking
        print(self.conn.login(username, password))
        if self.conn.logged_in_user:
            self.message_label.color = "#00ff00"
            self.message_label.value = "Login successful!"
            self.page.go('/')
            self.page.update()
        else:
            self.message_label.color = "#ff0000"
            self.message_label.value = "Invalid Username or Password"
            self.page.update()

class Signup_View(ft.Container):
    def __init__(self, page: ft.Page, database: Database):
        super().__init__()
        self.conn = database
        self.header = ft.Text(
            value="Signup to Lock In!",
            size=40,
            color="#ffffff",
            weight=ft.FontWeight.BOLD
        )
        self.confirm_message_label = ft.Text(value="", color="#ff0000", size=16)
        self.username_field = UsernameField()
        self.password_field = PasswordField("Password")
        self.confirm_password_field = PasswordField("Confirm Password")
        signup_button = ft.ElevatedButton(
            text="Sign Up",
            style=ft.ButtonStyle(
                bgcolor="#323234",
                color="#ffffff",
            ),
            width=150,
            height=50,
            on_click=lambda _: self.validate_signup(self.password_field.value, self.confirm_password_field.value)
        )

        self.toggle_page = PageToggle(
            normal = "Already Locked-In? ",
            hyperlink = "Login",
            on_click=lambda _: page.go('/login')
        )

        self.message_label = ft.Text(value="", color="#ff0000")

        right_content = ft.Column(
            [
                self.confirm_message_label,
                self.header,
                self.username_field,
                self.password_field,
                self.confirm_password_field,
                signup_button,
                self.toggle_page,
                self.message_label
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )

        self.content = ft.Row(
            [
                LeftStrip(page=page),
                ft.Container(
                    content=right_content,
                    expand=True,
                    alignment=ft.alignment.center,
                    height=page.window.height,
                )
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
        )

    def validate_signup(self, password, confirm_password):
        assert isinstance(password, str) and isinstance(confirm_password, str), "Password and Confirm Password must be strings."
        if password == confirm_password:
            if (self.conn.add_user(User(username=self.username_field.value, password=password))):
                self.confirm_message_label.value = "Account Created Successfully!"
                self.confirm_message_label.color = "#00ff00"
                self.page.go('/login')
                self.page.update()
            else:
                self.confirm_message_label.value = "User already exists!"
                self.confirm_message_label.color = "#ff0000"

def main(page: ft.Page):
    page.title = "Locked-In"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = 'dark'

    def route_change(route: ft.RouteChangeEvent) -> None:
        print(f"Current Route: {page.route}")
        page.views.clear()
        view = view_handler(page).get(page.route, ft.View(controls=[ft.Text("404 Not Found")]))
        page.views.append(view)
        page.update()
    page.on_route_change = route_change
    page.go('/login')

if __name__ == "__main__":
        ft.app(target=main)
