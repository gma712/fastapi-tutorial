from fastapi import FastAPI

from repository import Table

from infrastructure import Dynamodb

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!!!"}


@app.get("/item/{id}")
async def item(id):
    items = {
        "a": "hoge",
        "b": "fuga"
    }
    return {"item": f"{items[id]}"}


@app.get("/table/list")
async def list_tables():
    repository = Table(Dynamodb())
    return {"tables": repository.list_tables()}
