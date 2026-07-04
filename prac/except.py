from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

# http exception

@app.get("/http_exc/{userid}")
def user(userid: int):
    if userid !=1:
        raise HTTPException(
            status_code=404,
            detail="User not found"

        )
    return{
        "Message":"User found"
    }



# custom error handling 

class usernotfoundexc(Exception):
    def __init__(self, name: str):
        self.name = name



@app.get("/custom_exc/{name}")
def user2(name: str):
    if name != "thanos":
        raise usernotfoundexc(name)
    return{
        "Message":f"User found {name}"
    }

# global error handler

@app.exception_handler(usernotfoundexc)
def user_not_found_exc_handler(request: Request, exc: usernotfoundexc):
    return JSONResponse(
        status_code=404,
        content={
            "status":"error",
            "message": f"User {exc.name} not found"}
    )

@app.get("/glob_exc/{name}")
def user2(name: str):
    if name != "thanos":
        raise usernotfoundexc(name)
    return{
        "Message":f"User found {name}"
    }



