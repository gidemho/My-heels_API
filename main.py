from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="My Heels API",
    description="API for the My Heels footwear business",
    version="1.0.0"
)


@app.get("/")
def home():
    return{
        "message": "Welcome to My Heels API",
        "business": "My Heels",
        "tagline": "Elegance in every step" 
    }
products = [
    {
        "id": 1,
        "name": "Classic Heels",
        "category": "Heels",
        "price": 25000,
        "size": 38,
        "stock": 1
    },
    {
        "id": 2,
        "name": "Elegant Flat Shoes",
        "category": "Flats",
        "price": 18000,
        "size": 39,
        "stock": 15
    }
]
@app.get("/products")
def get_all_products():
    return products
    
@app.get("/products/{product_id}")
def get_products(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

        raise HTTPException(
            status_code=404,
            detail="product not found"
        )