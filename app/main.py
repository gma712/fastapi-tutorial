from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World!!!"}


@app.get("/{id}")
async def item(id):
    items = {
        "a": "hoge",
        "b": "fuga"
    }
    return {"item": f"{items[id]}"}
