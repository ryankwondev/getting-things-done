from enum import Enum

from sqlmodel import Field, SQLModel


class TaskStatus(str, Enum):
    DRAFT = "Draft"
    TASK = "Task"
    ACTION = "Action"
    PROJECT = "Project"
    COMMISSION = "Commission"
    DONE = "Done"


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str = Field(max_length=50)
    password: str = Field(max_length=50)


class Task(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str = Field(max_length=100)
    description: str = Field(max_length=500)
    status: TaskStatus = Field(default=TaskStatus.DRAFT)
    user_id: int = Field(foreign_key="user.id")
