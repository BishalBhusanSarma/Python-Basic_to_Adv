

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta, timezone
import psycopg2
import os
from dotenv import load_dotenv

# -------------------- CONFIG --------------------
load_dotenv()

SECRET_KEY = os.getenv("secretk")
ALGORITHM = os.getenv("algo")
# -------------------- FASTAPI --------------------

app = FastAPI()

# -------------------- PASSWORD HASHING --------------------

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")



# -------------------- DATABASE --------------------

conn = psycopg2.connect(
    host="localhost",
    database="students",
    user="postgres",
    password="1234",
    port=5432
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE,
    password VARCHAR(300)
)
""")

conn.commit()

# -------------------- MODELS --------------------

class User(BaseModel):
    username: str
    password: str


def hash_password(plain_password):
    return pwd_context.hash(plain_password)

def verify_password(plain_password, hashed_passsword):
    return pwd_context.verify(plain_password, hashed_passsword)

def jwt_token_gen(data : dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc)+ timedelta(minutes=1)

    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token):
    return jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])


@app.post("/reg/")
def register(user: User):
    hashed_password = hash_password(user.password)
    cur.execute("SELECT * FROM users WHERE username=%s", (user.username,))
    existing_user = cur.fetchone()

    if existing_user:
        raise HTTPException(status_code=400, detail="USER already exists")


    cur.execute("INSERT INTO users(username, password) VALUES(%s,%s)", (user.username, hashed_password))

    conn.commit()

    return {"message": "User registered successfully"}


@app.post("/login/")
def login(user: User):
    cur.execute("SELECT * FROM users WHERE username=%s", (user.username,))
    db_user = cur.fetchone()
    stored_password = db_user[2]
    conn.commit()
    if not db_user:
        raise HTTPException(status_code=400, detail="USER not exists")
    if not verify_password(user.password, stored_password):
        raise HTTPException(status_code=401, detail="Password didnt matched")
    
    
    if verify_password(user.password, stored_password):
        

       token = jwt_token_gen({"username":user.username})
       return {"message": "login successful", "token": token}