
from typing import List, Optional
from pydantic import BaseModel, validator


class Product(BaseModel):
    name: str
    price: float
    category: str

   
    @validator("price")
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError("Price must be greater than 0")
        return value



class InventoryItem(BaseModel):
    product: Product
    quantity: int


class Store(BaseModel):
    name: str
    items: List[InventoryItem]



def run_examples():
    
    product1 = Product(name="Laptop", price=1200.50, category="Electronics")
    print("✅ Valid Product:", product1)

    
    try:
        Product(name="Cheap Phone", price=0, category="Electronics")
    except Exception as e:
        print("❌ Invalid Product:", e)

    
    store = Store(
        name="Tech Store",
        items=[
            InventoryItem(product=product1, quantity=5),
            InventoryItem(product=Product(name="Headphones", price=150, category="Audio"), quantity=10)
        ]
    )
    print("🏬 Store with Nested Models:", store)


if __name__ == "__main__":
    run_examples()
