# Flask Inventory Management API

A backend REST API for managing inventory, products, and sales data using Flask, SQLAlchemy, and SQLite.  
Built as a portfolio project to demonstrate backend development, database design, and data analytics using Python.

---

## 🚀 Features

- Full CRUD operations for products (Create, Read, Update, Delete)
- Relational database design (Products, Inventory, Sales)
- Low stock detection for restocking alerts
- Top-selling products analytics
- Total inventory value calculation
- Aggregated system statistics
- CSV data ingestion using Pandas
- JSON REST API responses

---

## 🛠 Tech Stack

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- Pandas

---

## 📁 Project Structure

app1.py → Main Flask API application  
models.py → Database models (Product, Inventory, Sales)  
clean_inventory2.csv → Cleaned dataset  
data_loader.py → Script to load CSV into database  
inventory.db → SQLite database

---

## 🗄 Database Design

### Products Table
- product_id (Primary Key)
- product_name
- category
- supplier_id
- supplier_name
- unit_price
- status

### Inventory Table
- stock_quantity
- reorder_level
- reorder_quantity
- warehouse_location

### Sales Table
- sales_volume
- inventory_turnover_rate

---

## 🔌 API Endpoints

### Health Check
GET /

### Products
GET /products  
GET /product/<product_id>  
POST /product  
PUT /product/<product_id>  
DELETE /product/<product_id>  

### Analytics

GET /stats  
Returns:
- total_products
- total_inventory_records
- total_sales_records

GET /low-stock  
Returns products where stock quantity is below reorder level.

GET /top-selling  
Returns top 10 products sorted by sales volume.

## 💰 GET /inventory-value  
Returns total inventory value calculated as:  
**Unit Price × Stock Quantity**

---

## 📊 Example Response

```json
{
  "inventory_value": 12500.50
}
```

---

## ⚠️ Example Low Stock Response (GET /low-stock)

```json
[
  {
    "product_id": "29-205-1132",
    "product_name": "Sushi Rice",
    "stock_quantity": 22,
    "reorder_level": 72
  }
]
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/your-username/inventory-management-api.git
cd inventory-management-api
```

---

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

---

### 3. Install dependencies
```bash
pip install flask flask-sqlalchemy pandas
```

---

### 4. Run the Flask app
```bash
python app1.py
```

---

### 5. Load data into the database
```bash
python data_loader.py
```

---

### 6. Test API
Open in browser or Postman:

```
http://127.0.0.1:5000/
```

Example endpoints:

```
http://127.0.0.1:5000/products
http://127.0.0.1:5000/stats
http://127.0.0.1:5000/low-stock
```

