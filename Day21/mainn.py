
from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    in_stock: bool


items_db = {
    1: {"name": "Laptop", "description": "Gaming Laptop", "price": 1200.0, "in_stock": True},
    2: {"name": "Phone", "description": "Latest smartphone", "price": 800.0, "in_stock": False},
    3: {"name": "Tablet", "description": "Portable tablet", "price": 500.0, "in_stock": True},
}

users_posts = {
    1: [
        {"id": 1, "title": "My first post", "status": "published"},
        {"id": 2, "title": "Draft post", "status": "draft"}
    ],
    2: [
        {"id": 3, "title": "Another user post", "status": "published"}
    ]
}


@app.get("/items/{item_id}")
def get_item(item_id: int, skip: int = 0, limit: int = 10):
    """Fetch item by ID and apply skip/limit for filtering"""
    if item_id not in items_db:
        return {"error": "Item not found"}
    item = items_db[item_id]
    return {"item_id": item_id, "item": item, "skip": skip, "limit": limit}


@app.post("/items/")
def create_item(item: Item):
    """Add a new item to the 'database'"""
    new_id = max(items_db.keys()) + 1
    items_db[new_id] = item.dict()
    return {"message": "Item created successfully", "item_id": new_id, "item": item}



@app.get("/users/{user_id}/posts")
def get_user_posts(user_id: int, status: Optional[str] = Query(None, description="Filter posts by status")):
    """Return posts by a user, optionally filtered by status (published/draft)"""
    if user_id not in users_posts:
        return {"error": "User not found"}

    posts = users_posts[user_id]
    if status:
        posts = [p for p in posts if p["status"] == status]
    return {"user_id": user_id, "posts": posts}
