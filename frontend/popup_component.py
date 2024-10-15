import flet as ft
import datetime

class Popup(ft.Container):
    def __init__(self, on_submit):
        super().__init__()
        self.on_submit = on_submit

        #Fields for task data
        self.task_name = ft.TextField(label="Task Name", width=300)
        self.start_time = ft.TextField(label="Start Time (HH:MM)", width=150)
        self.end_time = ft.TextField(label="End Time (HH:MM)", width=150)
        self.description = ft.TextField(label="Description", multiline=True, width=300, height=100)

        # Selected date display
        self.selected_date = ft.Text(value=str(datetime.date.today()), width=200)

        self.date_picker = ft.DatePicker(
            value=datetime.date.today(),
            on_change=self.update_selected_date
        )

    def open_date_picker(self, e):
        """Open the DatePicker dialog."""
        self.page.overlay.append(self.date_picker)  
        self.date_picker.open = True  
        self.page.update()

    def update_selected_date(self, e):

        #returns the date u select on the calendar
        selected_date = e.data.split("T")[0]  
        self.selected_date.value = selected_date 
        self.date_picker.open = False 
        self.page.update()

    
    def show(self, page: ft.Page):
        self.page = page 
        date_selection_row = ft.Row(
            [
                self.selected_date,
                ft.IconButton(
                    icon=ft.icons.CALENDAR_TODAY,
                    on_click=self.open_date_picker,  
                ),
            ],
            spacing=10,
        )

        #Checkbox is used because radio buttons do not allow for multiple choices
        repetition_options = [
            ft.Checkbox(label="Mon", width=50),
            ft.Checkbox(label="Tue", width=50),
            ft.Checkbox(label="Wed", width=50),
            ft.Checkbox(label="Thu", width=50),
            ft.Checkbox(label="Fri", width=50),
            ft.Checkbox(label="Sat", width=50),
            ft.Checkbox(label="Sun", width=50),
            ft.Checkbox(label="Daily", width=50),
        ]
        self.repetition_options = repetition_options

        repetition_grid = ft.Row(
            [
                ft.Column(repetition_options[:4], tight=True),
                ft.Column(repetition_options[4:], tight=True),
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
        )

        popup = ft.AlertDialog(
            modal=True,
            content=ft.Column(
                [
                    self.task_name,
                    ft.Row([self.start_time, self.end_time], spacing=10),
                    self.description,
                    ft.Text("Select Date:"),
                    date_selection_row,  
                    ft.Text("Repetition:"),
                    repetition_grid,
                    ft.ElevatedButton("Create Task", on_click=self.submit_task),
                ],
                tight=True,
            ),
            on_dismiss=lambda e: page.overlay.remove(popup),
        )

        page.overlay.append(popup)
        popup.open = True
        page.update()

    def submit_task(self, e):
        selected_days = [chk.label for chk in self.repetition_options if chk.value]

        task_data = {
            "name": self.task_name.value,
            "start_time": self.start_time.value,
            "end_time": self.end_time.value,
            "description": self.description.value,
            "date": self.selected_date.value,
            "repetition": selected_days,
        }

        self.on_submit(task_data)

def main(page: ft.Page):
    page.title = "Popup Task Creation"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def on_task_submit(task_data):
        print("Task Submitted:", task_data)

        snack_bar = ft.SnackBar(ft.Text("Task Created!"))
        page.overlay.append(snack_bar)
        snack_bar.open = True
        page.update()

    def on_button_click(e):
        popup = Popup(on_task_submit)
        popup.show(page)

    button = ft.FloatingActionButton(
        icon=ft.icons.ADD,
        #color="#E7F5C6",
        #dis not work, dis gae
        on_click=on_button_click,
        bgcolor="#555555",
    )

    page.add(button)

if __name__ == "__main__":
    ft.app(target=main)
