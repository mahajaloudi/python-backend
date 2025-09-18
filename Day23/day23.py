
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validator
from fastapi.responses import JSONResponse

app = FastAPI()


class Product(BaseModel):
    name: str
    price: float
    category: str

    
    @validator("price")
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError("Price must be greater than 0")
        return v


products_db = {
    1: {"name": "Laptop", "price": 1200.50, "category": "Electronics"},
    2: {"name": "Shoes", "price": 80.0, "category": "Fashion"},
}


@app.get("/products/{product_id}")
def get_product(product_id: int):
    if product_id not in products_db:
       
        raise HTTPException(status_code=404, detail="Product not found")
    return products_db[product_id]


@app.post("/products")
def add_product(product: Product):
    new_id = max(products_db.keys()) + 1
    products_db[new_id] = product.dict()

   
    return JSONResponse(
        status_code=201,
        content={
            "success": True,
            "message": "Product added successfully",
            "product_id": new_id,
        },
    )


@app.exception_handler(ValueError)
def value_error_handler(request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content={"error": str(exc)}
    )
