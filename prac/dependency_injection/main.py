from fastapi import FastAPI, Depends, HTTPException, Header

app = FastAPI()



# token verification

def verify_token(token: str = Header(None)):
    if token != "My secret":
        raise HTTPException(
            status_code=401,
            detail="Unauthorised"
        )
    return{"message": "User authorised"}

@app.get("/verifytoken")
def verify_token(user: str = Depends(verify_token)):
    return user




def reusable_logic():
    return {"user":" Bishal"}


@app.get("/profile1")
def profile1(user = Depends(reusable_logic)):
    return user

@app.get("/profile2")
def profile2(user = Depends(reusable_logic)):
    return user