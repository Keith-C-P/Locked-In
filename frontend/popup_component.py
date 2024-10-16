import flet as ft
import datetime

class TaskDialogue(ft.AlertDialog):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.task_name = ft.TextField(label="Task Name", width=300)
        self.start_time = ft.TextField(label="Start Time (HH:MM)", width=120)
        self.end_time = ft.TextField(label="End Time (HH:MM)", width=120)
        self.description = ft.TextField(label="Description", multiline=True, width=300, height=100, min_lines=3)
        self.selected_date = ft.Text(value=str(datetime.date.today()), width=200)

        self.date_picker = ft.DatePicker(
            value=datetime.date.today(),
            on_change=self.update_selected_date
        )

        #can be replaced with a src pointing to samba.png
        date_selection_row = ft.Row(
            [
                self.selected_date,
                ft.IconButton(
                    icon=ft.icons.CALENDAR_TODAY,
                    icon_color="#E7F5C6",
                    on_click=self.open_date_picker,
                ),
            ],
            spacing=10,
        )

        # Repetition checkboxes
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

        # Layout for repetition checkboxes
        repetition_grid = ft.Row(
            [
                ft.Column(repetition_options[:4], tight=True),
                ft.Column(repetition_options[4:], tight=True),
            ],
            spacing=10,
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
        )

        # Dialog styling and content
        self.modal = True  #modal = True conflicts with the AlertDialog dismiss, so I can't dismiss it :(

        self.content = ft.Column(
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
        )

    def open_date_picker(self, e):
        self.page.overlay.append(self.date_picker)
        self.date_picker.open = True
        self.page.update()

    def update_selected_date(self, e):
        selected_date = e.data.split("T")[0]
        self.selected_date.value = selected_date
        self.date_picker.open = False
        self.page.update()

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

        print("Task Submitted:", task_data)

        # Show confirmation snack bar
        snack_bar = ft.SnackBar(ft.Text("Task Created!"))
        self.page.overlay.append(snack_bar)
        snack_bar.open = True
        self.page.update()

        
        self.dismiss()

    def dismiss(self):
        self.page.overlay.remove(self)
        self.open = False
        self.page.update()

    def show(self):
        self.page.overlay.append(self)
        self.open = True
        self.page.update()

def main(page: ft.Page):
    page.title = "Popup Task Creation"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    task_dialogue = TaskDialogue(page)

    button = ft.FloatingActionButton(
        icon=ft.icons.ADD,
        foreground_color="#E7F5C6",
        on_click=lambda e: task_dialogue.show(),
        bgcolor="#555555",
    )

    page.add(button)

if __name__ == "__main__":
    ft.app(target=main)
