from fastapi import FastAPI
from basem import todo

tasks=[]

app = FastAPI()


@app.get("/")
def all_tasks():
    return tasks

@app.post("/add_task")
def add_task(task:todo):
    tasks.append(task)
    return{"message": "Task added", "Task": task}

@app.put("/update/{id}")
def update(id:int, new_task:todo, notify = True): # path + query + body combo

    for index, s_task in enumerate(tasks):          # s_task - specific task
        if s_task.id == id:
            tasks[index] = new_task
            return{"message": "Task updated","notify" : notify, "Task": new_task}
    return{"error": "Not updated"}

@app.delete("/delete/{id}")
def delete(id: int):
    for index, s_task in enumerate(tasks):
        if s_task.id == id:
            tasks.pop(index)
            return{"Message": "Task deleted"}
    return{"Message": "Task not deleted"}