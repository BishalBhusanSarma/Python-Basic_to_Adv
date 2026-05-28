from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None
    brand : str

itemz = {
    1:{
    "brand": "Apple",
    "price": 250000,
    "model": "m1 pro",
    "year": 2029
    },
    2:{
    "brand": "Lenovo",
    "price": 300000,
    "model": "Legion",
    "year": 2025
    },
    3:{
    "brand": "hp",
    "price": 650000,
    "model": "alienwear",
    "year": 2039
    }
}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id+1000, "Brand": item.brand, "price": item.price, "In offer": "yes" if item.is_offer == True else "no"}

@app.post("/items/")
def post_item(item: Item):
    return {"Message":"Item created",
            "data":item}

@app.get("/getitems/{itemz_id}")
def get_itemz(itemz_id: int):
    return itemz[itemz_id]

@app.get("/getbyname")
def get_by_brand(brand: str | None):
    
    for item_id in itemz:
        b = itemz[item_id]["brand"].lower()
        if b == brand.lower():
            return itemz[item_id]
    return {"Item not found"}