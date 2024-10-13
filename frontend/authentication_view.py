import flet as ft

class LoginPage(ft.Container):
    def __init__(self, page, switch_to_signup):
        super().__init__()
        self.page = page
        self.switch_to_signup = switch_to_signup

        # Set up page properties
        self.page.title = "Login"
        self.page.window_width = 800
        self.page.window_height = 1000

        # Left strip with solid color
        left_strip = ft.Container(
            width=279,
            height=self.page.window_height,
            bgcolor="#b3ff00",
            alignment=ft.alignment.center,
            content=ft.Column(
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
            ),
        )

        # "Login to your Account" text
        login_text = ft.Text(
            value="Login to your Account",
            size=40,
            color="#ffffff",
            weight=ft.FontWeight.BOLD
        )

        # Username and password fields
        self.username_field = ft.TextField(
            label="Username",
            label_style=ft.TextStyle(size=12, color="#000000"),
            width=400,
            bgcolor="#ffffff",
            color="#000000",
        )

        self.password_field = ft.TextField(
            label="Password",
            label_style=ft.TextStyle(size=12, color="#000000"),
            width=400,
            bgcolor="#ffffff",
            color="#000000",
            password=True,
            suffix=ft.IconButton(
                icon=ft.icons.REMOVE_RED_EYE,
                tooltip="Show password",
                on_click=lambda _: self.toggle_show_password()
            )
        )

        # Sign-in button
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

        # New here? Sign-up link text
        sign_up_text = ft.Text(
            spans=[
                ft.TextSpan(
                    "New here? Why not ",
                ),
                ft.TextSpan(
                    "sign up",
                    ft.TextStyle(
                        color=ft.colors.BLUE,
                        decoration=ft.TextDecoration.UNDERLINE,
                    ),
                    on_click=lambda _: self.switch_to_signup()
                ),
            ],
            color="#ffffff"
        )

        # Message label
        self.message_label = ft.Text(value="", color="#ff0000")

        # Right content layout
        right_content = ft.Column(
            [
                login_text,
                self.username_field,
                self.password_field,
                sign_in_button,
                sign_up_text,
                self.message_label
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )

        # Row for left and right layout
        self.content = ft.Row(
            [
                left_strip,
                ft.Container(
                    content=right_content,
                    expand=True,
                    alignment=ft.alignment.center,
                    height=self.page.window_height,
                )
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
        )

    def toggle_show_password(self):
        self.password_field.password = not self.password_field.password
        self.password_field.update()

    def validate_login(self, username, password):
        if username == "admin" and password == "password":
            self.message_label.value = "Login successful!"
            self.message_label.color = "#00ff00"
        else:
            self.message_label.value = "Invalid username or password."
            self.message_label.color = "#ff0000"
        self.page.update()


class SignupPage(ft.Container):
    def __init__(self, page, switch_to_login):
        super().__init__()
        self.page = page
        self.switch_to_login = switch_to_login

        # Set up page properties
        self.page.title = "Signup"
        self.page.window_width = 800
        self.page.window_height = 1000

        # Left strip with solid color
        left_strip = ft.Container(
            width=279,
            height=self.page.window_height,
            bgcolor="#b3ff00",
            alignment=ft.alignment.center,
            content=ft.Column(
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
            ),
        )

        # "Signup to Lock In!" text
        signup_text = ft.Text(
            value="Signup to Lock In!",
            size=40,
            color="#ffffff",
            weight=ft.FontWeight.BOLD
        )

        # Message label for password mismatch
        self.confirm_message_label = ft.Text(value="", color="#ff0000", size=16)

        # Username, password, and confirm password fields
        self.username_field = ft.TextField(
            label="Username",
            label_style=ft.TextStyle(size=12, color="#000000"),
            width=400,
            bgcolor="#ffffff",
            color="#000000",
        )

        self.password_field = ft.TextField(
            label="Password",
            label_style=ft.TextStyle(size=12, color="#000000"),
            width=400,
            bgcolor="#ffffff",
            color="#000000",
            password=True,
            suffix=ft.IconButton(
                icon=ft.icons.REMOVE_RED_EYE,
                tooltip="Show password",
                on_click=lambda _: self.toggle_show_password()
            )
        )

        self.confirm_password_field = ft.TextField(
            label="Confirm Password",
            label_style=ft.TextStyle(size=12, color="#000000"),
            width=400,
            bgcolor="#ffffff",
            color="#000000",
            password=True,
            suffix=ft.IconButton(
                icon=ft.icons.REMOVE_RED_EYE,
                tooltip="Show confirm password",
                on_click=lambda _: self.toggle_show_confirm_password()
            )
        )

        # Sign-up button
        signup_button = ft.ElevatedButton(
            text="Sign Up",
            style=ft.ButtonStyle(
                bgcolor="#323234",
                color="#ffffff",
            ),
            width=150,
            height=50,
            on_click=lambda _: self.validate_signup(self.username_field.value, self.password_field.value, self.confirm_password_field.value)
        )

        # Already locked in? Login link text
        login_text = ft.Text(
            spans=[
                ft.TextSpan(
                    "Already locked in? ",
                ),
                ft.TextSpan(
                    "Login to your account",
                    ft.TextStyle(
                        color=ft.colors.BLUE,
                        decoration=ft.TextDecoration.UNDERLINE,
                    ),
                    on_click=lambda _: self.switch_to_login()
                ),
            ],
            color="#ffffff"
        )

        # Message label
        self.message_label = ft.Text(value="", color="#ff0000")

        # Right content layout
        right_content = ft.Column(
            [
                self.confirm_message_label,
                signup_text,
                self.username_field,
                self.password_field,
                self.confirm_password_field,
                signup_button,
                login_text,
                self.message_label
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )

        # Row for left and right layout
        self.content = ft.Row(
            [
                left_strip,
                ft.Container(
                    content=right_content,
                    expand=True,
                    alignment=ft.alignment.center,
                    height=self.page.window_height,
                )
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
        )

    def toggle_show_password(self):
        self.password_field.password = not self.password_field.password
        self.password_field.update()

    def toggle_show_confirm_password(self):
        self.confirm_password_field.password = not self.confirm_password_field.password
        self.confirm_password_field.update()

    def validate_signup(self, username, password, confirm_password):
        if password != confirm_password:
            self.confirm_message_label.value = "Not the same"
            self.page.update()
        else:
            self.confirm_message_label.value = ""
            self.message_label.value = "Signup successful!"
            self.message_label.color = "#00ff00"
            self.page.update()


def main(page: ft.Page):
    def switch_to_signup():
        page.clean()
        page.add(SignupPage(page, switch_to_login).content)

    def switch_to_login():
        page.clean()
        page.add(LoginPage(page, switch_to_signup).content)

    # Start with login page
    switch_to_login()


if __name__ == "__main__":
    ft.app(target=main)
import flet as ft

class LoginPage(ft.Container):
    def __init__(self, page, switch_to_signup):
        super().__init__()
        self.page = page
        self.switch_to_signup = switch_to_signup

        # Set up page properties
        self.page.title = "Login"
        self.page.window_width = 800
        self.page.window_height = 1000

        # Left strip with solid color
        left_strip = ft.Container(
            width=279,
            height=self.page.window_height,
            bgcolor="#b3ff00",
            alignment=ft.alignment.center,
            content=ft.Column(
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
            ),
        )

        # "Login to your Account" text
        login_text = ft.Text(
            value="Login to your Account",
            size=40,
            color="#ffffff",
            weight=ft.FontWeight.BOLD
        )

        # Username and password fields
        self.username_field = ft.TextField(
            label="Username",
            label_style=ft.TextStyle(size=12, color="#000000"),
            width=400,
            bgcolor="#ffffff",
            color="#000000",
        )

        self.password_field = ft.TextField(
            label="Password",
            label_style=ft.TextStyle(size=12, color="#000000"),
            width=400,
            bgcolor="#ffffff",
            color="#000000",
            password=True,
            suffix=ft.IconButton(
                icon=ft.icons.REMOVE_RED_EYE,
                tooltip="Show password",
                on_click=lambda _: self.toggle_show_password()
            )
        )

        # Sign-in button
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

        # New here? Sign-up link text
        sign_up_text = ft.Text(
            spans=[
                ft.TextSpan(
                    "New here? Why not ",
                ),
                ft.TextSpan(
                    "sign up",
                    ft.TextStyle(
                        color=ft.colors.BLUE,
                        decoration=ft.TextDecoration.UNDERLINE,
                    ),
                    on_click=lambda _: self.switch_to_signup()
                ),
            ],
            color="#ffffff"
        )

        # Message label
        self.message_label = ft.Text(value="", color="#ff0000")

        # Right content layout
        right_content = ft.Column(
            [
                login_text,
                self.username_field,
                self.password_field,
                sign_in_button,
                sign_up_text,
                self.message_label
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )

        # Row for left and right layout
        self.content = ft.Row(
            [
                left_strip,
                ft.Container(
                    content=right_content,
                    expand=True,
                    alignment=ft.alignment.center,
                    height=self.page.window_height,
                )
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
        )

    def toggle_show_password(self):
        self.password_field.password = not self.password_field.password
        self.password_field.update()

    def validate_login(self, username, password):
        if username == "admin" and password == "password":
            self.message_label.value = "Login successful!"
            self.message_label.color = "#00ff00"
        else:
            self.message_label.value = "Invalid username or password."
            self.message_label.color = "#ff0000"
        self.page.update()


class SignupPage(ft.Container):
    def __init__(self, page, switch_to_login):
        super().__init__()
        self.page = page
        self.switch_to_login = switch_to_login

        # Set up page properties
        self.page.title = "Signup"
        self.page.window_width = 800
        self.page.window_height = 1000

        # Left strip with solid color
        left_strip = ft.Container(
            width=279,
            height=self.page.window_height,
            bgcolor="#b3ff00",
            alignment=ft.alignment.center,
            content=ft.Column(
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
            ),
        )

        # "Signup to Lock In!" text
        signup_text = ft.Text(
            value="Signup to Lock In!",
            size=40,
            color="#ffffff",
            weight=ft.FontWeight.BOLD
        )

        # Message label for password mismatch
        self.confirm_message_label = ft.Text(value="", color="#ff0000", size=16)

        # Username, password, and confirm password fields
        self.username_field = ft.TextField(
            label="Username",
            label_style=ft.TextStyle(size=12, color="#000000"),
            width=400,
            bgcolor="#ffffff",
            color="#000000",
        )

        self.password_field = ft.TextField(
            label="Password",
            label_style=ft.TextStyle(size=12, color="#000000"),
            width=400,
            bgcolor="#ffffff",
            color="#000000",
            password=True,
            suffix=ft.IconButton(
                icon=ft.icons.REMOVE_RED_EYE,
                tooltip="Show password",
                on_click=lambda _: self.toggle_show_password()
            )
        )

        self.confirm_password_field = ft.TextField(
            label="Confirm Password",
            label_style=ft.TextStyle(size=12, color="#000000"),
            width=400,
            bgcolor="#ffffff",
            color="#000000",
            password=True,
            suffix=ft.IconButton(
                icon=ft.icons.REMOVE_RED_EYE,
                tooltip="Show confirm password",
                on_click=lambda _: self.toggle_show_confirm_password()
            )
        )

        # Sign-up button
        signup_button = ft.ElevatedButton(
            text="Sign Up",
            style=ft.ButtonStyle(
                bgcolor="#323234",
                color="#ffffff",
            ),
            width=150,
            height=50,
            on_click=lambda _: self.validate_signup(self.username_field.value, self.password_field.value, self.confirm_password_field.value)
        )

        # Already locked in? Login link text
        login_text = ft.Text(
            spans=[
                ft.TextSpan(
                    "Already locked in? ",
                ),
                ft.TextSpan(
                    "Login to your account",
                    ft.TextStyle(
                        color=ft.colors.BLUE,
                        decoration=ft.TextDecoration.UNDERLINE,
                    ),
                    on_click=lambda _: self.switch_to_login()
                ),
            ],
            color="#ffffff"
        )

        # Message label
        self.message_label = ft.Text(value="", color="#ff0000")

        # Right content layout
        right_content = ft.Column(
            [
                self.confirm_message_label,
                signup_text,
                self.username_field,
                self.password_field,
                self.confirm_password_field,
                signup_button,
                login_text,
                self.message_label
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )

        # Row for left and right layout
        self.content = ft.Row(
            [
                left_strip,
                ft.Container(
                    content=right_content,
                    expand=True,
                    alignment=ft.alignment.center,
                    height=self.page.window_height,
                )
            ],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER,
        )

    def toggle_show_password(self):
        self.password_field.password = not self.password_field.password
        self.password_field.update()

    def toggle_show_confirm_password(self):
        self.confirm_password_field.password = not self.confirm_password_field.password
        self.confirm_password_field.update()

    def validate_signup(self, username, password, confirm_password):
        if password != confirm_password:
            self.confirm_message_label.value = "Not the same"
            self.confirm_message_label.color = "#ff0000"
            self.message_label.value = ""
        else:
            self.confirm_message_label.value = ""
            self.message_label.value = "Signup successful!"
            self.message_label.color = "#00ff00"
        self.page.update()


def main(page: ft.Page):
    def switch_to_signup():
        page.clean()
        page.add(SignupPage(page, switch_to_login).content)

    def switch_to_login():
        page.clean()
        page.add(LoginPage(page, switch_to_signup).content)

    # Start with login page
    switch_to_login()


if __name__ == "__main__":
    ft.app(target=main)
