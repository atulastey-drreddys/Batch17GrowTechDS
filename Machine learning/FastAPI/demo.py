from  fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define a pydantic model for request validataion
class Item(BaseModel):
    name:str
    price: float
    IsOffer:bool = False

@app.get("/")
def read_out():
    return {"messege":"welcome to FastAPI tutorial"}

@app.get("/items/{item_id}")
def read_item(item_id:int,q:str=None):
    return {"item_id":item_id,"query":q}

@app.post("/item/{item_id}")
def create_item(item:Item):
    return {"messege":"Item Created Successfullyy","data":item.dict()}