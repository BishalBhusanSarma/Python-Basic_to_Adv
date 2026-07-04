import sqlite3
from fastapi import FastAPI

app = FastAPI()

conn = sqlite3.connect("test.db",check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""

    CREATE TABLE IF NOT EXISTS user (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               age INTEGER
               )
""")
conn.commit()


@app.get("/")
def home():
    return {"message": "database integrated"}

@app.post("/login")
def login(name: str, age: int):
    cursor.execute("""
        INSERT INTO user(name, age) VALUES(?,?)

    """, (name,age))
    conn.commit()
    return {"message":"Use created"}

@app.get("/allusers")
def all_users():
    cursor.execute("""
        SELECT * FROM user
    """)
    all_users = cursor.fetchall()
    return all_users

@app.get("/specific_user/{name}")
def specific_user(namez:str):
    cursor.execute(f"""
        SELECT * FROM user WHERE name = ?
    """, (namez,))
    user = cursor.fetchone()
    return user
