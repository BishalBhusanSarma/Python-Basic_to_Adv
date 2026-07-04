from pydantic import BaseModel
class task_inp(BaseModel):
    task: str
    status:bool