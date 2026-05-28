from fastapi import FastAPI
import db
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def home():
    return{"message" : "This is Home"}

@app.get("/getbyid/{id}")
def get_by_id(id : int):
    db.cur.execute("SELECT * FROM notes WHERE id = %s", (id,))
    data = db.cur.fetchone()
    
    return {"ID": data[0], "Title" :data[1], "Desc": data[2]}

#read
@app.get("/getall")
def get_all():
    db.cur.execute("SELECT * FROM notes")
    result= []
    for d in db.cur.fetchall():

        result.append({
            "ID": d[0],
            "Title": d[1],
            "Description": d[2]})
        
    return result

# add notes
@app.post("/add_notes/")
def post_add_notes(task : str, desc : str):
    db.cur.execute("INSERT INTO notes (task, description) VALUES(%s,%s)", (task,desc))
    db.conn.commit()
    return {"message": "Note added successfully"}

# delete
@app.delete("/remove/")
def delete_notes_by_id(id : int, task: str = None, desc: str = None):
    if id:
        db.cur.execute(
            'DELETE FROM notes WHERE id = %s',
            (id,)
        )

    elif task:
        db.cur.execute(
            'DELETE FROM notes WHERE task = %s',
            (task,)
        )
    elif desc:
        db.cur.execute(
            'DELETE FROM notes WHERE task = %s',
            (desc,)
        )
    db.conn.commit()
    return {"message": "Note Deleted successfully"}

# update
@app.post("/update/")
def post_update(id : int, task: str = None, desc: str = None):
    if task and desc:
        db.cur.execute("UPDATE notes SET task = %s, description = %s WHERE id = %s", (task,desc, id))
    elif task:
        db.cur.execute("UPDATE notes SET task = %s WHERE id = %s", (task,id))
    elif desc:
        db.cur.execute("UPDATE notes SET description = %s WHERE id = %s", (desc,id))
    db.conn.commit()
    return {"message": "Note Updated successfully"}
    



