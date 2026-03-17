from fastapi import FastAPI

app = FastAPI()

items = [
    {"id": 1, "name": "Apple", "price": 0.5},
    {"id": 2, "name": "Banana", "price": 0.3},
    {"id": 3, "name": "Orange", "price": 0.8},
]


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.get("/items")
async def get_items():
    return items

@app.get("/items/{item_id}")
async def get_items_by_id(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    return {"error": "Item not found"}
