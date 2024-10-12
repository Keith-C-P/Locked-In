import flet as ft
import random
from backend.database_connector import Database, Task, User

class TaskCard(ft.Container):
    def __init__(self, task: Task, height: int):
        super().__init__()
        self.name = task.name
        self.start_time = task.start_time
        self.end_time = task.end_time
        self.color = task.color

        # Styling
        self.bgcolor = ft.colors.with_opacity(opacity=0.5, color=self.color)
        self.border = ft.border.all(width=2, color=ft.colors.with_opacity(opacity=1, color=self.color))
        self.border_radius = ft.border_radius.all(10)
        self.height = height
        self.padding = ft.padding.all(0)
        self.margin = ft.margin.all(0)
        self.alignment = ft.alignment.top_left

        # Content
        self.content = ft.Container(
            ft.Row(
                controls=[
                    ft.Text(
                        value=self.name,
                        size=20,
                        height=50,
                        # bgcolor="red" #Debugging
                    ),
                    ft.IconButton(
                        icon="delete",
                    ),
                ],
                vertical_alignment=ft.CrossAxisAlignment.START,
                alignment=ft.CrossAxisAlignment.START,
            ),
            # border=ft.border.all(1, "red"), # Debugging
        )

class Task_Layer(ft.Container):
    def __init__(self, user: User, time_division: int = 15, header_height: int = 50, min_height: int = 900, width: int = None, padding: int = 10):
        # Initialization
        super().__init__()
        self.conn = Database()
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

        self.task_list = self.conn.get_tasks(user.uuid)
        self.__task_builder(self.task_list)

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
                ft.Container(
                    height=self.height,
                    width=20,
                ),
            ],
            alignment=ft.CrossAxisAlignment.START,
            spacing=0,
            # width=self.width,
            height=self.total_height,
        )

    def add_task(self, task: Task) -> None:
        """
        Add a task to the task list
        """
        # print(f"Adding task: {task.name}, Start: {task.start_time}, End: {task.end_time}")
        if task.color is None:
            task.color = random.choice(self.colors)
        self.task_list.append(task)
        self.__task_builder()
        # if self.page is None:
        #     self.update()

    def __task_length(self, task: Task) -> int:
        """
        Calculate the length of the task in minutes
        """
        start_time = task.start_time.split(":")
        end_time = task.end_time.split(":")
        start_index = int(start_time[0]) * 60 + int(start_time[1])
        end_index = int(end_time[0]) * 60 + int(end_time[1])
        return end_index - start_index

    def __task_builder(self, task_list: tuple[Task]) -> None:
        """
        Build the task cards
        """
        if len(task_list) == 0:
            return

        height_of_minute = (self.total_height - self.header_height) / (24 * 60)
        # print(f"Height of Minute: {height_of_minute}")
        self.task_cards = []

        filler_container = lambda height: ft.Container(
            height=height,
            # border=ft.border.all(1, "green") # Debugging
        )

        self.task_cards.append(filler_container(height=self.header_height)) # Header space

        first_task = self.task_list[0]
        start_hour, start_minute = map(int, first_task.start_time.split(":"))
        start_time = (start_hour * 60) + start_minute

        if start_time != 0:
            filler_height = start_time * height_of_minute
            self.task_cards.append(filler_container(height=filler_height))

        for i in range(len(task_list)):
            current_task = task_list[i]
            task_length = current_task.length

            # print(f"Rendering Task: {current_task.name}, Height: {task_length * height_of_minute}")

            self.task_cards.append(
                TaskCard(
                    task=current_task,
                    height=task_length * height_of_minute,
                )
            )

            if i == len(self.task_list) - 1:
                break

            next_task = self.task_list[i + 1]
            next_start_hour, next_start_minute = map(int, next_task.start_time.split(":"))
            next_start_minute = (next_start_hour * 60) + next_start_minute

            gap = next_start_minute - (start_time + task_length)
            if gap > 0:
                self.task_cards.append(filler_container(height=gap * height_of_minute))

            start_time += task_length

        # self.content.controls.clear()
        # self.content.controls.extend(self.task_cards)
        # self.update()

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
