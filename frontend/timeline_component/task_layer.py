import flet as ft
import random
from backend.database_connector import Database, Task, User

class TaskCard(ft.Container):
    def __init__(self, task: Task, height: int, task_layer):
        super().__init__()
        self.task: Task = task
        self.task_layer = task_layer

        # Styling
        self.bgcolor = ft.colors.with_opacity(opacity=0.5, color=self.task.color)
        self.border = ft.border.all(width=2, color=ft.colors.with_opacity(opacity=1, color=self.task.color))
        self.border_radius = ft.border_radius.all(10)
        self.height = height
        self.padding = ft.padding.all(5)
        self.margin = ft.margin.all(0)
        self.alignment = ft.alignment.top_left

        # Content
        self.content = ft.Column(
            controls=[
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                value=self.task.name,
                                size=20,
                                height=50,
                                # bgcolor="red" #Debugging
                            ),
                            ft.IconButton(
                                icon="delete",
                                on_click=lambda e: self.on_delete(),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.START,
                    ),
                ),
                ft.Container(
                    content=ft.Text(
                        value=self.task.description,
                        size=15,
                        height=50,
                        # bgcolor="red" #Debugging
                    ),
                ),
            ]
            # border=ft.border.all(1, "red"), # Debugging
        )

    def on_delete(self):
        print("Deleting Task")
        self.task_layer.conn.remove_task(self.task)
        self.task_layer.rehydrate_task_list()
        pass

class Task_Layer(ft.Container):
    def __init__(
        self,
        database: Database,
        time_division: int = 15,
        header_height: int = 50,
        min_height: int = 900,
        width: int = None,
        padding: int = 10
    ):

        # Initialization
        super().__init__()
        self.conn = database
        self.task_list: list[Task] = []
        self.task_cards: list[TaskCard] = []
        self.border_radius=ft.border_radius.all(10)
        self.header_height = header_height + (40 - padding) # Width of divider in header is 20 and padding is 10
        self.total_height = (((24 * 60) // time_division) * min_height) + self.header_height
        # print(f"Total Height: {self.total_height}")
        self.time_division = time_division

        # Styling
        self.height = self.total_height
        if width is None:
            self.expand=True
        else:
            self.width = width
        self.expand=True
        # self.border=ft.border.all(1, "red") # Debugging
        self.padding = ft.padding.all(padding)

        if self.conn.logged_in_user is not None:
            self.task_list = self.conn.get_tasks(self.conn.logged_in_user.uuid)
            self.task_cards = self.__task_builder()

        # Content
        self.content = ft.Row(
            controls=[
                ft.Container(
                    height=self.height,
                    width=70,
                ),
                ft.Column(
                    controls=self.task_cards,
                    alignment=ft.CrossAxisAlignment.START,
                    spacing=0,
                    expand=True,
                    # scroll=ft.ScrollMode.HIDDEN,70
                ),
            ],
            alignment=ft.CrossAxisAlignment.START,
            spacing=0,
            # width=self.width,
            height=self.total_height,
        )

    def rehydrate_task_list(self) -> None:
        """
        Add a task to the task list
        """
        self.task_cards = self.__task_builder()
        self.content.controls[1].controls = self.task_cards
        self.update()
        # print("Rehydrated from Task Layer")

    def __task_builder(self) -> list[TaskCard] | None:
        """
        Build the task cards
        """
        task_list = self.conn.get_tasks(self.conn.logged_in_user.uuid)
        if len(task_list) == 0:
            return

        task_cards = []
        filler_container = lambda height: ft.Container(
            height=height,
            # border=ft.border.all(1, "green") # Debugging
        )

        height_of_minute = (self.total_height - self.header_height) / (24 * 60)
        # print(f"Height of Minute: {height_of_minute}")

        task_cards.append(filler_container(height=self.header_height)) # Header space

        first_task = task_list[0]
        start_hour, start_minute = map(int, first_task.start_time.split(":"))
        start_time = (start_hour * 60) + start_minute

        if start_time != 0:
            filler_height = start_time * height_of_minute
            task_cards.append(filler_container(height=filler_height))

        for i, current_task in enumerate(task_list):
            task_length = current_task.length

            # print(f"Rendering Task: {current_task.name}, Height: {task_length * height_of_minute}")

            task_cards.append(
                TaskCard(
                    task=current_task,
                    height=task_length * height_of_minute,
                    task_layer=self
                )
            )

            if i == len(task_list) - 1:
                break

            next_task = task_list[i + 1]
            next_start_hour, next_start_minute = map(int, next_task.start_time.split(":"))
            next_start_minute = (next_start_hour * 60) + next_start_minute

            current_end_time = start_time + task_length
            gap = next_start_minute - current_end_time
            if gap > 0:
                task_cards.append(filler_container(height=gap * height_of_minute))

            start_time = next_start_minute
        # print("Task Cards:", self.task_cards)
        return task_cards

def main(page: ft.Page):
    page.title = "Task Layer Test"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = 'dark'

    task_layer = Task_Layer(
        time_division=15,
        total_height=900,
        height=900,
        width=1000
    )
    page.add(task_layer)

if __name__ == "__main__":
    ft.app(target=main)

#TODO:
# [x] Add the delete functionality to the TaskCard
