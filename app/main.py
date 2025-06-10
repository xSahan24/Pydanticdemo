from fastapi import FastAPI, HTTPException
from app.models import User

app = FastAPI()

@app.post("/users/")
def create_user(user: User):
    return {"message": "User created successfully", "user": user}
