from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class User(BaseModel):
    id: int
    name: str
    rent: int

people = []

@app.post("/input")
def input(user:User):
    people.append(user)
    return {"message": "Entered user details are" , "Details" : user}

@app.get("/tun")
def tungu():
    return people

@app.put("/upadte/{idz}")
def updte(idz:int, updated_user:User):
    for index,ids in enumerate(people):
        if ids.id == idz:
            people[index] = updated_user
            return{
                "message": "User updated",
                "Data": updated_user
            }
    return{"Message": "Something went wrong, user not found"}

@app.delete("/remove/{user_id}")
def delete(user_id:int):
    for index, ids in enumerate(people):
        if ids.id == user_id:
            people.pop(index)
            return{
                "message": "User removed"
            }
    return{"Message": "Something went wrong, user not found"}



