import flet as ft

class SidebarButton(ft.TextButton):
    def __init__(self, text: str, icon: ft.icons) -> None:
        super().__init__()
        self.icon= icon
        self.text= text
        self.style=ft.ButtonStyle(
            color="#E7F5C6",  # Default text color for button
            bgcolor=ft.colors.TRANSPARENT,  # Make background transparent
        )
        self.on_hover=self.hover

    def hover(self, event: ft.ControlEvent) -> None:
        self.bgcolor = "#E7F5C6" if event.data else ft.colors.TRANSPARENT
        self.color = "#b3ff00" if event.data else "#E7F5C6"

class Sidebar(ft.Container):
    def __init__(self, page: ft.Page) -> None:
        # Initialization
        super().__init__()

        # Styling
        self.width = 279
        # self.height = page.window.height
        self.bgcolor = "#32323E"
        self.padding = 20
        self.border_radius = ft.BorderRadius(40, 0, 40, 0)

        # Content
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
                SidebarButton("Dashboard", ft.icons.DASHBOARD),
                ft.Container(height=10),
                SidebarButton("Attendance", ft.icons.CHECK_CIRCLE_OUTLINED),
                ft.Container(height=10),
                SidebarButton("Mess Menu", ft.icons.FASTFOOD),
                ft.Container(height=10),
                # self.__create_button("Progress"),
                # ft.Container(height=10),
                SidebarButton("Settings", ft.icons.SETTINGS),
            ],
            alignment="start",
        )

# Testing the sidebar component
if __name__ == "__main__":
    def main(page: ft.Page):
        page.title = "Dashboard"
        page.add(Sidebar())

    ft.app(target=main)