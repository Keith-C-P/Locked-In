import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..')) #find another way
import flet as ft
import datetime
import re
from frontend.timeline_component.task_layer import Task_Layer
from backend.database_connector import Database

class Repeat(ft.Container):
    def __init__(self) -> None:
        # Initialization
        super().__init__()
        self.repetition_options = [ft.Segment(label = ft.Text(value=day), value = day) for day in ("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")]
        self.selected_days : str = ""
        self.repeat = ft.SegmentedButton(
            segments = self.repetition_options,
            allow_multiple_selection=True,
            allow_empty_selection=True,
            selected={},
            selected_icon=ft.Container(margin=ft.margin.all(0), padding=ft.padding.all(0)),
            width=500,
            on_change=self.handle_change
        )
        self.message_label = ft.Text(value="", color="#ff0000")

        # Styling
        self.width = 400
        self.border_radius = 2
        self.alignment = ft.alignment.center
        # self.border = ft.border.all(1, "#ff0000") # Debugging
        # self.margin = 5

        # Content
        self.content = ft.Column(
            controls=[
                ft.Text("Repeat"),
                self.repeat,
            ]
        )

    def get_selected_days(self) -> str:
        selected = "".join(self.selected_days)
        selected = re.sub(r"[\[\]\"\'\s]", "", selected)
        selected = re.sub(r"\,", " ", selected)
        print("Selected Days:", selected)
        return selected

    def handle_change(self, e: ft.ControlEvent) -> None:
        self.selected_days = e.data

class TaskDialogue(ft.AlertDialog):
    def __init__(self, page: ft.Page, database: Database, task_layer: Task_Layer, rehydrate_task_layer: callable = None) -> None:
        # Initialization
        super().__init__()
        self.page: ft.Page = page
        self.conn: Database = database
        self.start_time: str | None = None
        self.end_time: str | None = None
        self.task_layer = task_layer
        self.rehydrate_task_layer = rehydrate_task_layer
        self.task_name = ft.TextField(
            label="Task Name",
            hint_text="Enter Task Name",
        )
        self.start_time_picker = ft.TimePicker(on_change=self.update_start_time)
        self.end_time_picker = ft.TimePicker(on_change=self.update_end_time)

        #Elevated buttons for start and end time (im not sure which other buttons to use but these are fine too ig)
        self.start_time_button = ft.ElevatedButton(
            text="Start Time",
            width=125,
            on_click=lambda _: page.open(self.start_time_picker)
        )

        self.end_time_button = ft.ElevatedButton(
            text="End Time",
            width=125,
            on_click=lambda _: page.open(self.end_time_picker)
        )

        self.description = ft.TextField(
            label="Description",
            multiline=True,
            # width=300,
            height=100,
            min_lines=3,
            hint_text="Enter Task Description",
        )

        self.error_label = ft.Text(value="", color="#ff0000")

        self.date_picker = ft.DatePicker(
            value=datetime.date.today(),
            on_change=self.update_selected_date
        )

        self.date = ft.TextField(
            label="Date",
            hint_text="Select Date",
            text_vertical_align=ft.VerticalAlignment.START,
            value="",
            # width=200,
            # height=40,
            suffix=ft.IconButton(
                    icon=ft.icons.CALENDAR_TODAY, #you can also use an image here like samba.png :0
                    icon_color="#dce1de",
                    icon_size=25,
                    on_click=lambda _: page.open(self.date_picker),
                ),
        )
        self.repeat = Repeat()

        # Styling

        # Content
        self.content = ft.Column(
            [
                self.task_name,
                self.description,
                ft.Container(
                    ft.Row(
                        controls=[
                            self.start_time_button,
                            self.end_time_button
                        ],
                        spacing=10
                    ),
                    # self.border = ft.border.all(1, "#ff0000") # Debugging
                    # expand=True
                ),
                self.date,
                self.repeat,
                ft.Container(
                    content=ft.ElevatedButton("Create Task", on_click=self.submit_task),
                    alignment=ft.alignment.center_right,
                    # border = ft.border.all(1, "#ff0000") # Debugging
                ),
                self.error_label,
            ],
            tight=True,
        )

    def update_start_time(self, e: ft.ControlEvent):
        hour, minute = map(int, e.data.split(":"))
        formatted_time = f"{hour:02}:{minute:02}"  # Ensure two digits (cuz this was being gay earlier)
        self.start_time_button.text = f"Start: {formatted_time}"
        self.start_time = formatted_time
        print("Start Time:", self.start_time)
        self.update()

    def update_end_time(self, e: ft.ControlEvent):
        hour, minute = map(int, e.data.split(":"))
        formatted_time = f"{hour:02}:{minute:02}"  # Ensure two digits
        self.end_time_button.text = f"End: {formatted_time}"
        self.end_time = formatted_time
        print("End Time:", self.end_time)
        self.update()

    def update_selected_date(self, e: ft.ControlEvent):
        selected_date = e.data.split("T")[0]
        self.date.value = selected_date
        # self.date_picker.open = False
        self.update()

    def submit_task(self, e):
        if not self.task_name.value:
            self.error("Task name is required.")
            return

        if not self.start_time or not self.end_time:
            self.error("Start and end time are required.")
            return

        if self.task_length() <= 0:
            # print(self.task_length())
            self.error("Task length must be greater than 0.")
            return

        task_data = {
            "name": self.task_name.value,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "description": self.description.value,
            "date": self.date.value,
            "repetition": self.repeat.get_selected_days(),
        }

        added_task = self.conn.add_task(
            name=self.task_name.value,
            start_time=self.start_time,
            end_time=self.end_time,
            date=self.date.value,
            description=self.description.value,
            repetition=self.repeat.get_selected_days(),
            source="user",
        )

        if added_task:
            self.error(added_task)
            return

        print("Task Submitted:", task_data)

        snack_bar = ft.SnackBar(
            content=ft.Text("Task Created!")
        )
        self.page.overlay.append(snack_bar)
        snack_bar.open = True
        self.update()
        self.rehydrate_task_layer()
        self.page.close(self)

    def task_length(self) -> int:
        if not self.start_time or not self.end_time:
            return 0
        start_time = tuple(map(int , self.start_time.split(":")))
        end_time = tuple(map(int , self.end_time.split(":")))
        start_minutes = int(start_time[0]) * 60 + int(start_time[1])
        end_minutes = int(end_time[0]) * 60 + int(end_time[1])
        print("Task Length:", end_minutes - start_minutes)
        return end_minutes - start_minutes

    def error(self, message: str):
        self.error_label.value = message if message else ""
        self.update()

def main(page: ft.Page):
    page.title = "Popup Task Creation"
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    button = ft.FloatingActionButton(
        icon=ft.icons.ADD,
        foreground_color="#dce1de",
        on_click=lambda e: page.open(TaskDialogue(page=page, database=Database())),
        bgcolor="#010b13",
    )

    page.add(button)
if __name__ == "__main__":
    ft.app(target=main)

