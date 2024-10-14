import os, random, datetime, flet, dataclasses, dotenv, mysql.connector
from flet import colors
from dataclasses import dataclass
from dotenv import load_dotenv

@dataclass
class User():
    username: str
    password: str
    uuid: int = 0
    privilage: str = "USER"

    def __post_init__(self):
        assert self.privilage in ("ADMIN", "USER"), "Privilage must be either ADMIN or USER"
        assert 4 <= len(self.username) <= 255, "Username must be between 4 and 255 characters"
        assert 8 <= len(self.password) <= 255, "Password must be between 8 and 255 characters"

    def __str__(self):
        return f"User: {self.username}, ID: {self.uuid}, Privilage: {self.privilage}"

@dataclass
class Task():
    taskid: int = 0
    name: str = "Default Task"
    start_time: str = ""
    end_time: str = ""
    date: str = ""
    description: str = ""
    repition: str = ""
    author: int = 0
    source: str = None
    length: int = 0
    color: str = None

    def __post_init__(self) -> None:
        assert self.date or self.repition, "Date or repitition must be provided"
        assert not (self.date and self.repition), "Date and repitition is not allowed"
        assert 4 <= len(self.name), "Task name must be atleast 4 characters long"

        self.length = self.__task_length()
        self.colors = (
            colors.RED_500,
            colors.BLUE_500,
            colors.GREEN_500,
            colors.YELLOW_500,
            colors.PURPLE_500,
            colors.PINK_500
        )
        if not self.color or self.color not in self.colors:
            self.color = random.choice(self.colors)
    def __str__(self):
        return f"Task: {self.name}, ID: {self.taskid}, Author: {self.author}, Date: {self.date}, Repition: {self.repition}, Source: {self.source}"

    def __task_length(self) -> int:
        """
        Calculate the length of the task in minutes
        """
        start_time = self.start_time.split(":")
        end_time = self.end_time.split(":")
        start_index = int(start_time[0]) * 60 + int(start_time[1])
        end_index = int(end_time[0]) * 60 + int(end_time[1])
        return end_index - start_index


class Database:
    def __init__(self, app_name: str = "LOCKEDIN") -> None:
        self.APP_NAME = app_name
        load_dotenv()
        self.HOSTNAME = os.getenv("MYSQL_HOSTNAME")
        self.USERNAME = os.getenv("MYSQL_USERNAME")
        self.PASSWORD = os.getenv("MYSQL_PASSWORD")
        self.__connect()
        self.logged_in_user: User | None = None

    def __connect(self):
        self.conn = mysql.connector.connect(
            host=self.HOSTNAME,
            user=self.USERNAME,
            password=self.PASSWORD
        )
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"SHOW DATABASES LIKE '{self.APP_NAME}';")
        # print(type(self.cursor.fetchone()))
        if not self.cursor.fetchone():
            self.__create_database()
            pass

    def __create_database(self) -> None:
        # self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.APP_NAME};")
        self.cursor.execute(f"SHOW DATABASES LIKE '{self.APP_NAME}';")

        if not self.cursor.fetchone():
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.APP_NAME};")
        self.cursor.execute(f"USE {self.APP_NAME};")
        self.conn.commit()

        # Create Users Table
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS USERS (
                            UUID        INT          AUTO_INCREMENT PRIMARY KEY,
                            PRIVILAGE   VARCHAR(255),
                            USERNAME    VARCHAR(255),
                            PASSWORD    VARCHAR(255));""")

        # Create Tasks Table
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS TASKS (
                            TASKID        INT AUTO_INCREMENT PRIMARY KEY,
                            AUTHOR        INT,
                            FOREIGN KEY(AUTHOR) REFERENCES USERS(UUID),
                            TASK_NAME     VARCHAR(255)        NULL,
                            START_TIME    VARCHAR(255)        NULL,
                            END_TIME      VARCHAR(255)        NULL,
                            DESCRIPTION   TEXT                NULL,
                            DATE          DATE                NULL,
                            REPETITION    VARCHAR(255)        NULL,
                            SOURCE        VARCHAR(255)        NULL);""") #Mon Tue Wed Thu Fri Sat Sun
        self.conn.commit()

    def add_user(self, user: User) -> bool:
        self.cursor.execute(f"USE {self.APP_NAME};")
        if self.user_exists(user):
            print("User Already Exists")
            return False
        self.cursor.execute(f"INSERT INTO USERS (PRIVILAGE, USERNAME, PASSWORD) VALUES ('{user.privilage}', '{user.username}', '{user.password}');")
        self.conn.commit()
        return True

    def add_task(self, task: Task) -> None:
        self.cursor.execute(f"USE {self.APP_NAME};")
        self.cursor.execute(f"""INSERT INTO TASKS (
                            AUTHOR,
                            TASK_NAME,
                            START_TIME,
                            END_TIME,
                            DESCRIPTION,
                            DATE,
                            REPETITION,
                            SOURCE)
                            VALUES ('{task.author}',
                            '{task.name}',
                            '{task.start_time}',
                            '{task.end_time}',
                            '{task.description}',
                            '{task.date}',
                            '{task.repition}',
                            '{task.source}');""")
        self.conn.commit()

    def get_tasks(self, author: int) -> tuple[Task]:
        today = datetime.date.today()
        weekday = datetime.datetime.now().strftime("%A")[:3]
        self.cursor.execute(f"USE {self.APP_NAME};")
        self.cursor.execute(f"""SELECT * FROM TASKS
                            WHERE AUTHOR = '{author}'
                            AND (DATE = '{today}'
                                OR REPETITION REGEXP '{weekday}'
                            );"""
                            )
        tasks = []
        for row in self.cursor.fetchall():
            # print(row)
            task = Task(taskid=row[0], author=row[1], name=row[2], start_time=row[3], end_time=row[4], description=row[5], date=row[6], repition=row[7], source=row[8])
            tasks.append(task)
        return tuple(tasks)

    def login(self, username, password) -> User | str:
        self.cursor.execute(f"USE {self.APP_NAME};")
        if not self.user_exists(User(username=username, password=password)):
            return "User Does Not Exist"

        self.cursor.execute(f"SELECT * FROM USERS WHERE USERNAME = '{username}' AND PASSWORD = '{password}';")
        user = self.cursor.fetchall()[0]
        if user:
            print(user)
            self.logged_in_user = User(uuid=user[0], privilage=user[1], username=user[2], password=user[3])
            return None
        return "Incorrect Password"

    def user_exists(self, user: User) -> bool:
        self.cursor.execute(f"SELECT * FROM USERS WHERE USERNAME = '{user.username}';")
        if self.cursor.fetchall():
            return True
        return False


if __name__ == "__main__":
    db = Database()
    author = 1
    # db.add_user(User(privilage="ADMIN", username="admin", password="admin@123"))
    # db.add_user(User(privilage="USER", username="test1", password="123456789"))
    db.add_task(Task(author=author, name="Test Task", start_time="12:00", end_time="13:00", description="This is a test task", date="2024-10-11"))
    db.get_tasks(author)

# USERS DATABASE
# SL.NO. | PRIVILAGE | USERNAME | PASSWORD

# TASKS DATABASE
# SL.NO. | AUTHOR | EVENT_NAME | START_TIME | END_TIME | DESCRIPTION | DAY | SHARED_WITH | REPITION