from fastapi import FastAPI
from pydantic import BaseModel
from basem import user, Address

app = FastAPI()

@app.post("/login")
def login(user: user):
    return {"message": "user created", "details": user}


@app.post("/login_add")
def login(user: Address):
    return {"message": "user created", "details": user}

