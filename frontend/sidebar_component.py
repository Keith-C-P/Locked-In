import flet as ft

class SidebarButton(ft.TextButton):
    def __init__(self, text: str, icon: ft.icons, on_click: callable = None) -> None:
        super().__init__()
        self.icon = icon
        self.text = text
        self.style = ft.ButtonStyle(
            color="#dce1de",  # Default text color for button
            bgcolor=ft.colors.TRANSPARENT,  # Make background transparent
        )
        self.on_hover = self.hover
        if on_click is None:
            self.on_click = on_click

    def hover(self, event: ft.ControlEvent) -> None:
        self.bgcolor = "#E7F5C6" if event.data else ft.colors.TRANSPARENT
        self.color = "#49a078" if event.data else "#E7F5C6"

class Sidebar(ft.Container):
    def __init__(self, page: ft.Page) -> None:
        # Initialization
        super().__init__()
        self.page = page

        # Styling
        self.width = 279
        self.bgcolor = "#32323E"
        self.padding = 20
        self.border_radius = ft.BorderRadius(40, 0, 40, 0)

        # Content
        self.content = ft.Column(
            controls=[
                ft.Text(
                    value="Locked-In",
                    size=35,
                    color="#dce1de",
                    font_family="Helvetica",
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Divider(
                    height=1,
                    color="#9cc5a1",
                ),
                ft.Container(height=20),
                SidebarButton("Dashboard", ft.icons.DASHBOARD, on_click=lambda e: self.page.go("/")),
                # ft.Container(height=10),
                # SidebarButton("Attendance", ft.icons.CHECK_CIRCLE_OUTLINED, ),
                ft.Container(height=10),
                SidebarButton("Mess Menu", ft.icons.FASTFOOD, on_click=lambda e: self.page.go("/mess-menu")),
                ft.Container(height=10),
                SidebarButton("Settings", ft.icons.SETTINGS, on_click=lambda e: self.page.go("/settings")),
            ],
            alignment="start",
        )

# Testing the sidebar component
if __name__ == "__main__":
    def main(page: ft.Page):
        page.title = "Dashboard"
        page.add(Sidebar(page=page))  # Pass page to Sidebar

    ft.app(target=main)
