import flet as ft
import datetime
from frontend.sidebar_component import Sidebar
from frontend.navbar_component import Navbar  # Import the Navbar component

class MessMenuDay(ft.Container):
    def __init__(self, day, breakfast, lunch, dinner):
        super().__init__()
        self.content = ft.Column(
            controls=[
                ft.Text(f"{day} Menu", size=20, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                ft.Divider(height=1, color=ft.colors.WHITE),
                ft.Text("Breakfast:", size=16, color=ft.colors.WHITE),
                ft.Text(breakfast, color=ft.colors.WHITE54),
                ft.Divider(height=1, color=ft.colors.WHITE),
                ft.Text("Lunch:", size=16, color=ft.colors.WHITE),
                ft.Text(lunch, color=ft.colors.WHITE54),
                ft.Divider(height=1, color=ft.colors.WHITE),
                ft.Text("Dinner:", size=16, color=ft.colors.WHITE),
                ft.Text(dinner, color=ft.colors.WHITE54),
            ],
            spacing=15
        )

class MessMenuPage(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.menu_data = {
            "Monday": {
                "breakfast": "Bread, Butter, Jam, Millet Dosa, Tea/Coffee, Boiled Egg",
                "lunch": "Chappathi, Rajma Masala, Jeera Pulao, Steamed Rice, Arachivitta Sambar, Pineapple Rasam",
                "dinner": "Madras Paratha, Mattar Paneer Masala, Steamed Rice, Hara Moong Dal, Sambar"
            },
            "Tuesday": {
                "breakfast": "Bread, Butter, Jam, Poori, Dal Aloo Masala, Tea/Coffee",
                "lunch": "Chappathi, Meal Maker Curry, Bahara Pulao, Variety Rice, Curd Rice",
                "dinner": "Punjabi Paratha, Black Channa, Steamed Rice, Dal Fry, Veg Chilli"
            },
            "Wednesday": {
                "breakfast": "Upma, Sambar, Coconut Chutney, Tea/Coffee",
                "lunch": "Dosa, Chutney, Steamed Rice, Mixed Vegetable Curry",
                "dinner": "Pasta, Garlic Bread, Salad"
            },
            "Thursday": {
                "breakfast": "Idli, Sambar, Coconut Chutney, Tea/Coffee",
                "lunch": "Rice, Dal Tadka, Vegetable Curry",
                "dinner": "Paneer Tikka, Naan, Raita"
            },
            "Friday": {
                "breakfast": "Cornflakes, Milk, Banana",
                "lunch": "Biryani, Raita, Salad",
                "dinner": "Pizza, Garlic Bread, Soft Drink"
            },
            "Saturday": {
                "breakfast": "Aloo Paratha, Curd, Tea/Coffee",
                "lunch": "Khichdi, Papad, Pickle",
                "dinner": "Vegetable Fried Rice, Manchurian"
            },
            "Sunday": {
                "breakfast": "Pancakes, Maple Syrup, Tea/Coffee",
                "lunch": "Grilled Chicken, Veg Salad, Rice",
                "dinner": "Burgers, Fries"
            },
        }
        self.page = page
        self.sidebar = Sidebar(page=page)
        
        # Instantiate the Navbar here
        self.navbar = Navbar(heading="Mess Menu", subheading="For Hostel peeps only")  # Assuming the Navbar constructor doesn't require parameters
        
        today = datetime.datetime.now().strftime('%A')
        self.current_day = today if today in self.menu_data else "Monday"
        self.menu_display = self.get_day_menu(self.current_day)
        self.day_buttons = self.create_day_buttons()

        # Content
        self.content = ft.Row(
            controls=[
                self.sidebar,  # Sidebar on the left
                ft.Container(
                    content=ft.Column(
                        controls=[
                            self.navbar,  # Add navbar here
                            ft.Row(controls=self.day_buttons, alignment=ft.MainAxisAlignment.CENTER, spacing=8),
                            ft.Divider(height=2, color=ft.colors.WHITE),
                            self.menu_display  # Show today's menu initially
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=30
                    ),
                    expand=True,
                    padding=20,
                    bgcolor="#010b13"  # Black background
                ),
            ],
            expand=True,
        )

    def create_day_buttons(self):
        buttons = []
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            buttons.append(
                ft.Container(
                    content=ft.TextButton(
                        text=day,
                        style=ft.ButtonStyle(
                            color="#b3ff00" if day == self.current_day else "#E7F5C6",
                            bgcolor=ft.colors.TRANSPARENT,
                        ),
                        on_click=lambda e, d=day: self.switch_day(d)
                    ),
                    padding=ft.padding.symmetric(horizontal=10, vertical=8),
                    border_radius=ft.border_radius.all(15),
                    border=ft.border.all(2, "#b3ff00" if day == self.current_day else "#E7F5C6"),
                )
            )
        return buttons

    def switch_day(self, day):
        self.current_day = day
        self.menu_display.content = self.get_day_menu(day).content  # Update the displayed menu
        for button in self.day_buttons:
            button.content.style = ft.ButtonStyle(
                color="#b3ff00" if button.content.text == day else "#E7F5C6"
            )
            button.border = ft.border.all(2, "#b3ff00" if button.content.text == day else "#E7F5C6")
        self.page.update()

    def get_day_menu(self, day):
        menu = self.menu_data.get(day, {"breakfast": "", "lunch": "", "dinner": ""})
        return MessMenuDay(day, menu["breakfast"], menu["lunch"], menu["dinner"])

def main(page: ft.Page):
    page.title = "Mess Menu for Hostellers"
    page.bgcolor = "#010b13"  # Black background
    mess_menu_view = MessMenuPage(page)
    page.add(mess_menu_view)

if __name__ == "__main__":
    ft.app(target=main)
