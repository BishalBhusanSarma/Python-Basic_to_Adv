
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    fname:str
    lname:str
    age:int
    sal:float

class userResp(BaseModel):
    fname:str
    age:int
    
people=[]

@app.post("/reg")
def reg_user(user:User):
    people.append(user)
    return{"message":"User registered", "details": user}


@app.get("/user_by age", response_model=List[userResp])
def get_user():
    return [p for p in people if p.age > 18]