from passlib.context import CryptContext
from jose import jwt, JWTError
import os
from dotenv import load_dotenv
from datetime import datetime, timezone, timedelta

pwd_hsh = CryptContext(schemes=["argon2"], deprecated = "auto")

load_dotenv()
secretk = os.getenv('secretk')
algo = os.getenv('algo')

uname = {"username": "bishal", "exp" : datetime.now(timezone.utc) + timedelta(seconds=30) }
passw2 = input("Enter password")
passw = pwd_hsh.hash("1234")

x = pwd_hsh.verify(passw2, passw)

token = jwt.encode(uname, key=secretk , algorithm=algo)
if x is True:
    print("Password matched")
    print(token)
else:
    print("Password didnt matched")


  
