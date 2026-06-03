# 📦 Flask Inventory Management API

A full-stack backend system for managing inventory, products, and sales data using Flask, SQLAlchemy, and SQLite.

Built as a portfolio project to demonstrate backend development, relational database design, and data analytics using Python.

---

# 🚀 Features

- Full CRUD operations for products (Create, Read, Update, Delete)
- Relational database design (Products, Inventory, Sales)
- Low stock detection for restocking alerts
- Top-selling product analytics
- Inventory valuation calculations
- System-wide KPI statistics
- CSV data ingestion using Pandas
- RESTful JSON API responses

---

# 🛠 Tech Stack

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- Pandas

---

# 📁 Project Structure

app6.py              → Main Flask API application  
models.py            → Database models (Product, Inventory, Sales)  
load_data.py         → ETL script for CSV data ingestion  
clean_inventory2.csv → Dataset  
inventory.db         → SQLite database  

---

# 🗄 Database Design

## Products Table
- product_id (Primary Key)
- product_name
- category
- supplier_id
- supplier_name
- unit_price
- status

## Inventory Table
- stock_quantity
- reorder_level
- reorder_quantity
- warehouse_location

## Sales Table
- sales_volume
- inventory_turnover_rate

---

# 🔌 API Endpoints

## Health Check
GET /

## Products
GET /products  
GET /product/<product_id>  
POST /product  
PUT /product/<product_id>  
DELETE /product/<product_id>  

---

# 📊 Analytics Endpoints

## System Stats
GET /stats  
Returns:
- total_products  
- total_inventory_records  
- total_sales_records  

---

## Low Stock
GET /low-stock  
Returns products where stock is below reorder level.

---

## Top Selling Products
GET /top-selling  
Returns top 10 products by sales volume.

---

## Inventory Value
GET /inventory-value  

Formula:
Unit Price × Stock Quantity  

Example response:
{
  "inventory_value": 12500.50
}

---

# ⚙️ Setup Instructions

## 1. Clone repository
git clone https://github.com/your-username/inventory-management-api.git  
cd inventory-management-api  

## 2. Create virtual environment
python -m venv venv  

Activate:

Windows:
venv\Scripts\activate  

Mac/Linux:
source venv/bin/activate  

## 3. Install dependencies
pip install flask flask-sqlalchemy pandas  

## 4. Load dataset
python load_data.py  

## 5. Run application
python app6.py  

## 6. Open in browser
http://127.0.0.1:5000/

---

# 🎯 Project Highlights

- Built a full REST API using Flask and SQLAlchemy  
- Designed a normalized relational database (Products, Inventory, Sales)  
- Implemented ETL pipeline using Pandas for CSV ingestion  
- Developed API-based analytics endpoints (stock, sales, KPI metrics)  
- Built scalable backend architecture for inventory management systems  

---

# 🚀 Future Improvements

- User authentication system (Admin login)  
- Near real-time stock updates using frontend polling or WebSocket integration  
- Predictive restocking using machine learning  
- Cloud deployment (Render / Azure)
