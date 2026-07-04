from fastapi import FastAPI


app = FastAPI()

#query parameter
@app.get("/users")
def users(name):
    return {"name" : name}



#optional query parameter
@app.get("/users_opt")
def users(name: str = None):
    return {"name" : name}

#Default value query parameter
@app.get("/users_def")
def users(name: str = "Hi Man"):
    return {"name" : name}

#multiple query parameters

@app.get("/mult_q")
def mult_q(name:str = "vamos", salary:float = 55000.0):
    return {"name": name, "salary" : salary}