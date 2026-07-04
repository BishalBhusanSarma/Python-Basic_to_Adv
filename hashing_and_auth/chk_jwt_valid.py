from passlib.context import CryptContext
from jose import jwt, JWTError


import os
from dotenv import load_dotenv


load_dotenv()
secretk = os.getenv('secretk')
algo = os.getenv('algo')

token = input("Enter token: ")
try:
    payload = jwt.decode(token, key=secretk , algorithms=[algo])
    print("valid token")
    print(payload)
except JWTError:
    print("invalid token")