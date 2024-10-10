import mysql.connector
import os
from dataclasses import dataclass
from dotenv import load_dotenv

@dataclass
class Task():
    name: str = "Default Task"
    start_time: str = ""
    end_time: str = ""
    day: str = ""
    description: str = ""
    repition: str = ""
    author: int = 0
    color: str = None

class Database:
    def __init__(self, app_name: str = "LOCKEDIN"):
        self.APP_NAME = app_name
        load_dotenv()
        self.HOSTNAME = os.getenv("MYSQL_HOSTNAME")
        self.USERNAME = os.getenv("MYSQL_USERNAME")
        self.PASSWORD = os.getenv("MYSQL_PASSWORD")
        self.conn = mysql.connector.connect(
            host=self.HOSTNAME,
            user=self.USERNAME,
            password=self.PASSWORD
        )

        self.cursor = self.conn.cursor()
        if (self.cursor.execute(f"SHOW DATABASES LIKE '{self.APP_NAME}';")):
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
                                FOREIGN KEY(AUTHOR) REFERENCES USERS(UUID),
                                EVENT_NAME    VARCHAR(255)        NULL,
                                START_TIME    VARCHAR(255)        NULL,
                                END_TIME      VARCHAR(255)        NULL,
                                DESCRIPTION   TEXT                NULL,
                                DATE          DATE                NULL,
                                REPITION      VARCHAR(255)        NULL);""") #Mon Tue Wed Thu Fri Sat Sun
            self.conn.commit()
        else:
            self.cursor.execute(f"USE {self.APP_NAME};")
            self.conn.commit()

    def add_user(self, privilage: str, username: str, password: str):
        assert privilage in ["ADMIN", "USER"], "Privilage must be either ADMIN or USER"
        assert 8 <= len(password) <= 255, "Password must be atleast 8 characters long"
        assert 8 <= len(username) <= 255, "Username must be atleast 8 characters long"
        self.cursor.execute(f"USE {self.APP_NAME};")
        self.cursor.execute(f"INSERT INTO USERS (PRIVILAGE, USERNAME, PASSWORD) VALUES ('{privilage}', '{username}', '{password}');")
        self.conn.commit()

    def add_task(self, task: Task):
        self.cursor.execute(f"USE {self.APP_NAME};")
        self.cursor.execute(f"""INSERT INTO TASKS (
                            AUTHOR,
                            EVENT_NAME,
                            START_TIME,
                            END_TIME,
                            DESCRIPTION,
                            DAY,
                            SHARED_WITH,
                            REPITION)
                            VALUES ('{task.author}',
                            '{task.name}',
                            '{task.start_time}',
                            '{task.end_time}',
                            '{task.description}',
                            '{task.day}',
                            '{task.share_with}',
                            '{task.repition}');""")
        self.conn.commit()

    def check_task(self, task: Task):
        assert task.author, "Author must be provided"
        assert task.name, "Name must be provided"
        assert task.start_time, "Start Time must be provided"
        assert task.end_time, "End Time must be provided"
        assert task.day, "Day must be provided"


    def get_tasks(self, author):
        self.cursor.execute(f"USE {self.APP_NAME};")
        self.cursor.execute(f"SELECT * FROM TASKS WHERE AUTHOR = '{author}';")
        return self.cursor.fetchall()

    def login():
        pass

# USERS DATABASE
# SL.NO. | PRIVILAGE | USERNAME | PASSWORD

# TASKS DATABASE
# SL.NO. | AUTHOR | EVENT_NAME | START_TIME | END_TIME | DESCRIPTION | DAY | SHARED_WITH | REPITION