from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, Session


app = FastAPI()

Database_Url = "sqlite:///./test.db"

engine = create_engine(Database_Url, connect_args={"check_same_thread" : False})

sessionLocal = sessionmaker(bind=engine)

base = declarative_base()

class TODO(base):

    __tablename__ = "Todos"

    id = Column(Integer, primary_key=True, index=True)
    task = Column(String)
    completed = Column(Boolean, default=False)

base.metadata.create_all(bind=engine)


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home(db:Session = Depends(get_db)):
    
    return{"DB connected"}

