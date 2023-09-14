from enum import Enum

from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TaskStatus(str, Enum):
    DRAFT = "Draft"
    TASK = "Task"
    ACTION = "Action"
    PROJECT = "Project"
    COMMISSION = "Commission"
    class Kanban(Base):
        __tablename__ = "kanbans"
    
        id = Column(Integer, primary_key=True, index=True)
        name = Column(String(100))
        user_id = Column(Integer, ForeignKey("users.id"))
    
        user = relationship("User")
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    password = Column(String(50))

    tasks = relationship("Task", back_populates="user")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    description = Column(String(500))
    status = Column(Enum(TaskStatus), default=TaskStatus.DRAFT)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="tasks")
