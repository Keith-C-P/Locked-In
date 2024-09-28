import flet as ft

class Sidebar(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = ft.Column(
            controls=[
                ft.Text(
                    value="Locked-In",
                    size=35,
                    color="#E7F5C6",
                    font_family="Helvetica",
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Divider(
                    height=1,
                    color="#BFD1E5",
                ),
                ft.Container(height=20),
                self.__create_button("Dashboard", ft.icons.DASHBOARD),
                ft.Container(height=10),
                self.__create_button("Attendance", ft.icons.CHECK_CIRCLE_OUTLINED),
                ft.Container(height=10),
                self.__create_button("Mess Menu", ft.icons.FASTFOOD),
                ft.Container(height=10),
                # self.__create_button("Progress"),
                # ft.Container(height=10),
                self.__create_button("Settings", ft.icons.SETTINGS),
            ],
            alignment="start",
        )
        self.width = 279
        self.height = 900
        self.bgcolor = "#32323E"
        self.padding = 20
        self.border_radius = ft.BorderRadius(40, 0, 40, 0)

    def __create_button(self, text: str, icon: ft.icons) -> ft.TextButton:
        # Button creation with hover effects
        return ft.TextButton(
            icon= icon,
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
        page.add(Sidebar())

    ft.app(target=main)