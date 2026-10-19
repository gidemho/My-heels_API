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
