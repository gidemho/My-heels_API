# My Heels API — Design Decisions
Project Overview
My Heels is a shoe inventory and customer order management API
designed for small-scale shoe retailers and business owners.

Technology Stack
- Language: Python
- Framework: FastAPI
- Database: SQLite
- API Style: REST

Database Design
The database will contain five entities:
1. Products
2. Customers
3. Orders
4. OrderItems
5. Users
  
Design Decisions
- A relational database will maintain relationships between records.
- Products will have unique SKUs for identification.
- Foreign keys will connect customers, orders, products and order items.
- Order items will store the price at the time of purchase.
- Input validation will protect data integrity.
- Passwords will be hashed before storage.

Project Scope
Week 1 focuses on database design, API specification and product CRUD endpoints.
Authentication, testing and deployment will be developed in subsequent weeks.
