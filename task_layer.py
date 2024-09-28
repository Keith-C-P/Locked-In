import flet as ft
import dataclasses
import random

@dataclasses.dataclass
class Task():
    name: str = "Default Task"
    start_time: str = ""
    end_time: str = ""
    color: str = ""

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
        # self.expand = True

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
    def __init__(self, min_height: int = 50, time_division: int = 15, header_height: int = 50, height: int = 900, width: int = 1000):
        super().__init__()
        self.task_list: list[Task] = []
        self.task_cards: list[TaskCard] = []
        self.border_radius=ft.border_radius.all(10)
        self.min_height = min_height
        self.total_height = header_height + (60 // time_division) * height
        self.time_division = time_division
        self.colors = (
            ft.colors.RED_500,
            ft.colors.BLUE_500,
            ft.colors.GREEN_500,
            ft.colors.YELLOW_500,
            ft.colors.PURPLE_500,
            ft.colors.PINK_500
        )

        # Styling
        self.height = header_height + (60 // time_division) * height
        self.width = width
        # self.expand=True
        self.border=ft.border.all(1, "red") # Debugging

        # Content
        self.content = ft.Column(
            controls=self.task_cards,
            alignment=ft.CrossAxisAlignment.START,
            spacing=0,
            scroll=ft.ScrollMode.HIDDEN,
        )

    def add_task(self, task: Task) -> None:
        print(f"Adding task: {task.name}, Start: {task.start_time}, End: {task.end_time}")
        if task.color is None:
            task.color = random.choice(self.colors)
        self.task_list.append(task)
        self.__task_builder()
        # if self.page is None:
        #     self.update()

    def __task_length(self, task: Task) -> int:
        start_time = task.start_time.split(":")
        end_time = task.end_time.split(":")
        start_index = int(start_time[0]) * 60 + int(start_time[1])
        end_index = int(end_time[0]) * 60 + int(end_time[1])
        return end_index - start_index

    def __task_builder(self) -> None:
        '''
        Takes a list of Tasks and builds the main task list
        '''
        total_intervals = (24 * 60) // self.time_division
        height_of_minute = self.total_height // total_intervals
        self.task_cards = []

        filler_container = lambda height: ft.Container(
            height=height,
            border=ft.border.all(1, "red") # Debugging
        )

        if len(self.task_list) == 0:
            return

        first_task = self.task_list[0]
        start_hour, start_minute = map(int, first_task.start_time.split(":"))
        start_index = start_hour * 60 + start_minute

        if start_index != 0:
            filler_height = start_index * height_of_minute
            self.task_cards.append(filler_container(height=filler_height))

        for i in range(len(self.task_list) - 1):
            current_task = self.task_list[i]
            task_length = self.__task_length(current_task)

            self.task_cards.append(
                TaskCard(
                    task=current_task,
                    height=task_length * height_of_minute
                )
            )

            next_task = self.task_list[i + 1]
            next_start_hour, next_start_minute = map(int, next_task.start_time.split(":"))
            next_start_index = next_start_hour * 60 + next_start_minute

            gap = next_start_index - (start_index + task_length)
            if gap > 0:
                self.task_cards.append(filler_container(height=gap * height_of_minute))

            start_index += task_length

        self.content.controls.clear()
        self.content.controls.extend(self.task_cards)
        # self.update()


def main(page: ft.Page):
    page.title = "Task Layer Test"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = 'dark'

    task_layer = Task_Layer(
        min_height=50,
        time_division=15,
        total_height=900,
        height=900,
        width=1000
    )
    task_layer.add_task(Task(name="Task 1", start_time="01:15", end_time="02:00"))
    task_layer.add_task(Task(name="Task 2", start_time="02:15", end_time="05:00"))
    task_layer.add_task(Task(name="Task 3", start_time="05:00", end_time="05:15"))
    page.add(task_layer)

if __name__ == "__main__":
    ft.app(target=main)
