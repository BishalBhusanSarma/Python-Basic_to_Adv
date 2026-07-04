from fastapi import FastAPI
from conect import connect, cursor, est_conn, fetchall
from bm import task_inp

app = FastAPI()


est_conn()

@app.get("/")
def all_tasks():
    all_t = fetchall()
    if all_t:

        return all_t
    return {"message":"No task exists"}

@app.get("/by_task_id/{task_id}")
def one_task(task_id):
    one_t = cursor.execute("""
        SELECT * FROM task WHERE id = ?
        """,(task_id,))
    task = one_t.fetchone()
    if task:
        return task
    return {"message":"Task not exist"}

@app.post("/add-task")
def add_task(p_task:task_inp):
    all_t = fetchall()

    if p_task in all_t:
        return {"message": "Task already exist"}
    else:
        cursor.execute("""
            INSERT INTO task(task,status) VALUES(?,?)
            """, (p_task.task,p_task.status))
        connect.commit()
        return{"message": "Task added"}
    
@app.put("/update/{task_id}")
def update_task(task_id:int, u_task:task_inp):
    all_t = fetchall()
    for tid in all_t:
        if task_id == tid[0]:
            
            cursor.execute("""
                UPDATE task
                SET task = ?, status = ?
                WHERE id = ?
                """, (u_task.task,u_task.status, task_id))
            connect.commit()
            return{"message": "Task updated"}
    return {"message": "Task not exist"}

@app.delete("/delete/{task_id}")
def delete_task(task_id:int):
    all_t = fetchall()
    for task in all_t:
        if task_id == task[0]:    
            cursor.execute("""
                    DELETE from task
                    WHERE id = ?
                    """, (task_id,))
            connect.commit()
            return{"message": "Task deleted"}
    return {"message": "Task not exist"}

