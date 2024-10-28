import flet as ft
import datetime
from frontend.sidebar_component import Sidebar
from frontend.navbar_component import Navbar
from backend.database_connector import Database

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
    def __init__(self, page: ft.Page, database: Database):
        super().__init__()
        self.conn = database
        self.menu_data = {
            "Monday": {
                "breakfast": "Bread, Butter, Jam, Millet Dosa, Idly Podi, Oil, Chutney, Sambar, Chapathi, White Khuruma, Tea/Coffee/Milk, Boiled Egg",
                "lunch": "Chappathi, Rajma Masala, Jeera Pulao, Steamed Rice, Arachivitta Sambar, Panchratna Dal, Drumstick Brinjal Mochai, Dum Aloo, Pineapple Rasam, Pickle, Buttermilk, Fryums",
                "snacks": "Pav Bhaji, Tea/Coffee",
                "dinner": "Madras Paratha, Mattar Paneer Masala, Vegetable Idly, Idly Podi, Oil, Special Chutney, Steamed Rice, Hara Moong Dal, Sambar, Rasam, Pickle, Fryums, Veg Salad, Milk, Banana, Fish Gravy"
            },
            "Tuesday": {
                "breakfast": "Bread, Butter, Jam, Poori, Dal Aloo Masala, Semia Veg Kichadi, Chutney, Tea/Coffee/Milk",
                "lunch": "Sweet, Millet Chappathi, Meal Maker Curry, Bahara Pulao, Variety Rice, Curd Rice, Steamed Rice, Dal Fry, Tomato Rasam, Urulai Peas Roasted, Pickle",
                "snacks": "Mysore Bonda, Chutney, Tea/Coffee",
                "dinner": "Punjabi Paratha, Black Channa, Steamed Rice, Dal Fry, Veg/Chilli Gobi Dry, Millet Dosa, Idly Podi, Oil, Sambar, Pepper Rasam, Pickle, Fryums, Veg Salad, Milk, Special Fruits, Mutton Gravy"
            },
            "Wednesday": {
                "breakfast": "Bread, Butter, Jam, Millet, Idly Podi, Oil, Sambar, Chutney, Poha, Mint Chutney, Tea/Coffee/Milk, Masala Omellete",
                "lunch": "Chapati, Muttar Masala, Bhindi Aloo, Bujjia, Veg Pulao, Steamed Rice, Masala Sambar, Tomato Dal, Garlic Rasam, Pickle, Poriyal, Buttermilk, Fryums",
                "snacks": "Veg Puff/Sweet Puff, Tea/Coffee",
                "dinner": "Chapati, Steamed Rice, Dal Tadka, Butter Chicken Masala (Non-Veg)/ Paneer Butter Masala/ Butter Paneer, Rasam, Pickle, Fryums, Veg Salad, Milk, Banana, Chicken Gravy"
            },
            "Thursday": {
                "breakfast": "Bread, Butter, Jam, Idiyappam (Masala or Lemon) or Millet Idiyappam, Chapathi, Chana Masala/White Khurma Chutney, Tea/Coffee/Milk,",
                "lunch": "Chapathi, Aloo Gobi Athiraki, Onion Pulao, Steamed Rice, Punjabi Dal Fry, Kadi Pakoda, Rasam, Pickle, Yam, Varuval, Butter Milk, Fryums",
                "snacks": "Pani Puri (or) Chana Sundal, Tea/Coffee",
                "dinner": "Millet Sweet (or) Kasari, Chole Pattora, Chole Masala, Steamed Rice, Tomato Dal, Idly, Sambar, Coconut Chutney, Idly Podi, Oil, Rasam, Pickle, Fryums, Veg Salad, MIlk, Banana. Mutton Gravy"
            },
            "Friday": {
                "breakfast": "Bread, Butter, Jam, Chapathi, Rajma Masala, Dosa, Idly Podi, Oil, Sambar, Coconut Chutney / Tomato Chutney, Tea/Coffee/Milk",
                "lunch": "Dry Jamun/Bread Halwa, Capsicum Gobi Curry, Dal Tadka, Veg Biryani, Mix Raita, Bisibelabath Rice, Curd Rice, Steamed Rice, Tomato Rasam, Pickle, Fryums",
                "snacks": "Sambar Vada (or) Millet Vada, Tea/Coffee",
                "dinner": "Millet Chapathi, Veg Manchurian/Gobi Manchurian, Veg Fried Rice/Veg Noodles, Steamed Rice, Dal Maharani, Sambar, Rasam, Pickle, Fryums, Veg Salad, Milk, Special Fruits, Chicken Gravy",
            },
            "Saturday": {
                "breakfast": "Bread, Butter, Jam, Chapathi, Veg Khurma, Sambar, Pongal (or) Millet Pongal Vada, Chutney, Tea/Coffee/Milk",
                "lunch": "Poori, White Peas Curry, Aloo Thindeli, Kashmiri Pulao, Steamed Rice, Dal Fry, Karakozhambu, Kootu(Cabbage), Rasam, Pickle, Buttermilk, Fryums",
                "snacks": "Cake (or) Brownie, Tea/Coffee",
                "dinner": "Punjabi Paratha, Potato Fry, Steamed Rice, Veg Jhal Pyaza, Bagara Dal, Idly, Idly Podi, Oil, Chutney, Kathamba, Sambar, Rasam, Pickle, Fryums, Veg Salad, Milk, Banana, Chicken Gravy"
            },
            "Sunday": {
                "breakfast": "Bread, Butter, Jam, Chole Bhature, Chana Masala, Sambar, Rava Upma, Coconut Chutney, Tea/Coffee/Milk",
                "lunch": "Chapathi, Chicken(Pepper/Kadai), Paneer Butter Masala, Dal Tadka, Mint Pulao / Steamed Rice, Rasam Pickle, Mixed Veg Poriyal, Butter Milk, Fryums",
                "snacks": "Corn/Bajji with Chutney, Tea/Coffee",
                "dinner": "Aloo Paratha, Masala Curd, Steamed Rice, Hara Moong Dal Tadka, Kathamba Sambar, Poriyal, Rasam, Pickle, Fryums, Veg Salad, Milk, Banana, Ice Cream Cone, Chicken Gravy"
            },
        }
        self.page = page
        self.sidebar = Sidebar(page=page)
        self.navbar = Navbar(heading="Mess Menu", subheading="Check out today's meals", username=self.conn.logged_in_user.username if self.conn.logged_in_user else None)
        today = datetime.datetime.now().strftime('%A')
        self.current_day = today if today in self.menu_data else "Monday"
        self.menu_display = self.get_day_menu(self.current_day)
        self.day_buttons = self.create_day_buttons()

        # Styling
        self.expand=True

        # Content
        self.content = ft.Row(
            controls=[
                self.sidebar,  # Sidebar on the left
                ft.Container(
                    content=ft.Column(
                        controls=[
                            self.navbar,
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
        """Create buttons for each day (Monday to Sunday), displayed in an oval box."""
        buttons = []
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:  # Added Saturday and Sunday
            buttons.append(
                ft.Container(
                    content=ft.TextButton(
                        text=day,
                        style=ft.ButtonStyle(
                            color="#b3ff00" if day == self.current_day else "#E7F5C6",  # Highlight the selected day
                            bgcolor=ft.colors.TRANSPARENT,
                        ),
                        on_click=lambda e, d=day: self.switch_day(d)
                    ),
                    padding=ft.padding.symmetric(horizontal=10, vertical=8),  # Reduced padding for smaller buttons
                    border_radius=ft.border_radius.all(15),  # Smaller oval shape
                    border=ft.border.all(2, "#b3ff00" if day == self.current_day else "#E7F5C6"),
                )
            )
        return buttons

    def switch_day(self, day):
        """Switch to the selected day's menu."""
        self.current_day = day
        self.menu_display.content = self.get_day_menu(day).content  # Update the displayed menu
        for button in self.day_buttons:
            button.content.style = ft.ButtonStyle(
                color="#b3ff00" if button.content.text == day else "#E7F5C6"
            )
            button.border = ft.border.all(2, "#b3ff00" if button.content.text == day else "#E7F5C6")
        self.page.update()

    def get_day_menu(self, day):
        """Get the menu for the specified day."""
        menu = self.menu_data.get(day, {"breakfast": "", "lunch": "", "dinner": ""})
        return MessMenuDay(day, menu["breakfast"], menu["lunch"], menu["dinner"])

def main(page: ft.Page):
    page.title = "Mess Menu for Hostellers"
    page.bgcolor = "#010b13"  # Black background
    mess_menu_view = MessMenuPage(page)
    page.add(mess_menu_view)


if __name__ == "__main__":
    ft.app(target=main)
