from fastapi import FastAPI

from .models import User

app = FastAPI()


@app.post("/signup")
async def signup(user: User):
    # Code to handle user signup goes here
    return {"message": "User signed up successfully"}


@app.get("/kanban")
async def get_kanban():
    # Code to fetch and return the Kanban board goes here
    return {"message": "Kanban board"}
