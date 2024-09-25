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
    def __init__(self, task: Task, height: int = 50):
        super().__init__()
        self.name = task.name
        self.start_time = task.start_time
        self.end_time = task.end_time
        self.color = task.color

        self.bgcolor= ft.colors.with_opacity(opacity=0.5, color=self.color)
        self.border=ft.border.all(width=2, color=ft.colors.with_opacity(opacity=1, color=self.color))
        self.border_radius=ft.border_radius.all(10)
        self.height=height
        self.padding=ft.padding.all(0)
        self.margin=ft.margin.all(0)
        self.alignment=ft.alignment.top_left

        self.content =ft.Row(
                controls=[
                    ft.Container(width=1),
                    ft.Text(
                        value=self.name,
                        size=20,
                    ),
                    ft.IconButton(
                        icon="delete",
                    ),
                ],
                height=self.height,
                expand=True,
        )

class TaskColumn(ft.Container):
    def add_task(self, task: Task) -> None:
        colors = (
            ft.colors.RED_500,
            ft.colors.BLUE_500,
            ft.colors.GREEN_500,
            ft.colors.YELLOW_500,
            ft.colors.PURPLE_500,
            ft.colors.PINK_500
        )

        if (task.color != None):
            task.color = random.choice(colors)
        self.task_list.append(task)
        self.__task_builder()
        # if self.page is None:
            # self.update()

    def __start_and_end_indexing(self, task: Task) -> tuple[int]:
        start_time = task.start_time.split(":")
        end_time = task.end_time.split(":")
        start_index = int(start_time[0]) * 4 + int(start_time[1]) // 15 # 15 minutes
        end_index = int(end_time[0]) * 4 + int(end_time[1]) // 15 # 15 minutes
        # print(start_index, end_index) # Debugging
        return (start_index, end_index)

    def __task_builder(self) -> None:
        '''
        Takes a list of Tasks and builds the main task list
        '''
        total_index = 24 * (60 // 15)
        self.task_cards = []

        filler_container = lambda height: ft.Container(
            height=height,
            # border=ft.border.all(1, "red") # Debugging
        )

        if len(self.task_list) == 0:
            self.task_cards.append(ft.Container(height = total_index * 50))
            return

        for i in range(len(self.task_list)):
            current_task = self.task_list[i]
            current_task_index: tuple[int] = self.__start_and_end_indexing(current_task)
            current_task_length = current_task_index[1] - current_task_index[0]

            if i == 0 and current_task.start_time != 0: # if the first task doesn't start at 0
                self.task_cards.append(filler_container(height = (current_task_index[0] + 1) * 50))

            self.task_cards.append(TaskCard(current_task, height = current_task_length * 50))

            if i != len(self.task_list) - 1:
                next_task = self.task_list[i + 1]
                next_task_index: tuple[int] = self.__start_and_end_indexing(next_task)
                gap = next_task_index[0] - current_task_index[1]
                if gap != 0:
                    self.task_cards.append(filler_container(height = gap * 50))
            else:
                if current_task.end_time != total_index:
                    self.task_cards.append(filler_container(height = (total_index - current_task_index[1]) * 50))

        self.content.controls.clear()
        self.content.controls.extend(self.task_cards)


    def __init__(self):
        super().__init__()
        self.task_list: list[Task] = []
        self.task_cards: list[TaskCard] = []
        self.content = ft.Column(
            controls=self.task_cards,
            alignment=ft.CrossAxisAlignment.START,
            spacing=0,
        )
        self.expand=True
        # self.border=ft.border.all(1, "grey") # Debugging