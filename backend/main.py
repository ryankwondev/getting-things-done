from fastapi import FastAPI

from .models import User

app = FastAPI()


@app.post("/signup")
async def signup(user: User):
    # Code to handle user signup goes here
    return {"message": "User signed up successfully"}


@app.post("/login")
async def login(user: User):
    # Code to handle user login goes here
    return {"message": "User logged in successfully"}

@app.post("/logout")
async def logout():
    # Code to handle user logout goes here
    return {"message": "User logged out successfully"}

@app.post("/task")
async def register_task(task: Task):
    # Code to handle task registration goes here
    return {"message": "Task registered successfully"}

@app.put("/task")
async def modify_task(task: Task):
    # Code to handle task modification goes here
    return {"message": "Task modified successfully"}

@app.put("/kanban")
async def modify_kanban(kanban: Kanban):
    # Code to handle kanban modification goes here
    return {"message": "Kanban modified successfully"}

@app.get("/kanban")
async def get_kanban():
    # Code to fetch and return the Kanban board goes here
    return {"message": "Kanban board"}
