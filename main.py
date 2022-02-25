from fastapi import FastAPI, Query
from enum import Enum
from pydantic import BaseModel
app = FastAPI()


# Request body

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float


@app.post("/items")
async def create_item(item: Item, q: list[str] = Query(["Anubhav", "Adarsh"], max_length=30)):
    print(item)
    return [item, q]

# Query parameters
ls = [{i: i * i} for i in range(10)]


@app.get("/all")
async def get_all(count: int = 0, limit: int = 100):
    if count >= 10:
        return {
            "message": "not enough data",
            "limit": limit
        }
    return {
        "ls": ls,
        "limit": limit
    }


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/api/v1/{data}")
async def get_data(data: str):
    ls = [ch for ch in data]
    valid = True
    for ch in data:
        if ch.isdigit():
            valid = False
        if ch.isspace():
            valid = False
    return {
        "message": "thank you for visiting us",
        "data": data,
        "split": ls,
        "validity": valid
    }


@app.get("/api/v1/sq/{data}")
async def get_square(data: int):
    return {
        "message": "success",
        "data": data,
        "square": data * data
    }


@app.get('/api/v1/ml/{model_name}')
async def get_ml_bot(model_name: ModelName):
    print(model_name)
    print(model_name.value)
    if model_name.value == ModelName.lenet.value:
        return {
            "bot": ModelName.lenet.value
        }
    if model_name.value == ModelName.resnet.value:
        return {
            "bot": ModelName.resnet.value
        }
    return {
        "bot": ModelName.alexnet.value
    }
