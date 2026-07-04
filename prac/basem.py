from pydantic import BaseModel

class user(BaseModel):
    name: str
    age: int

class Address(BaseModel):
    user: user       # Nested model as it calls the user model inside address model
    city: str
    pin: int

class todo(BaseModel):
    id:int
    task:str
    comp:bool