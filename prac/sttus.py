from fastapi import FastAPI, status, HTTPException
from basem import user


app = FastAPI()

people = []

@app.post("/reg", status_code= status.HTTP_201_CREATED) # HTTP status code
def users(user:user):
    people.append(user)
    return {"status": "success", # custom response
            "user details" : user }
@app.get("/{userid}")
def user(userid: int):
    if userid != 1:
        raise HTTPException(
            status_code= 404,
            detail="User not found"
        )
    return people
