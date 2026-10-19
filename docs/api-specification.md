# My Heels API Specification

Product

| Method | Endpoint | Purpose | Success Status |
|---|---|---|---|
| POST | /products | Create a product | 201 |
| GET | /products | List all products | 200 |
| GET | /products/{product_id} | Retrieve one product | 200 |
| PUT | /products/{product_id} | Update a product | 200 |
| DELETE | /products/{product_id} | Delete a product | 204 |

Error Responses
- 404: Product not found.
- 422: Request data fails validation.
- 400: Invalid application-level request.

- Planned Resources
- Customers
- Orders
- Order items
- Users and authentication


Request and Response Examples

POST /products

Purpose: Create a new shoe product.

Request body:
{
      "name": "Classic Black Heel",
      "sku": "MH-001",
      "size": "39",
      "colour": "Black",
      "price": 25000,
      "stock_quantity": 12
    }

Success status: 201 Created.

Response body:
{
      "id": 1,
      "name": "Classic Black Heel",
      "sku": "MH-001",
      "size": "39",
      "colour": "Black",
      "price": 25000,
      "stock_quantity": 12
     }
    
GET /products
Purpose: Retrieve all shoe products.
Success status: 200 OK.
Response body: A JSON array containing product objects.

GET /products/{product_id}
Purpose: Retrieve a specific product.
Success status: 200 OK.
Error status: 404 Not Found.

PUT /products/{product_id}
Purpose: Update an existing product.
Success status: 200 OK.
Error status: 404 Not Found.

DELETE /products/{product_id}
Purpose: Delete a product.
Success status: 204 No Content.
Error status: 404 Not Found.

Validation Rules
- Product SKU must be unique.
- Product price must be positive.
- Stock quantity cannot be negative.
- A requested product must exist before it can be updated or deleted.
