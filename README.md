# 📦 Flask Inventory Management API

A full-stack inventory management system built with **Flask, SQLAlchemy, and SQLite**, featuring RESTful APIs, data analytics, and an interactive dashboard.

This project demonstrates backend development, relational database design, ETL pipelines, and data visualisation using Python.

---

# 🧠 Architecture Overview

The system follows a modular backend architecture:

- Flask REST API handles CRUD operations and analytics
- SQLAlchemy manages relational database models
- Pandas ETL pipeline processes and loads CSV data
- Frontend dashboard consumes API endpoints for real-time insights
- Docker containerisation enables consistent deployment

---

# 🚀 Features

- Full CRUD operations for product management
- Relational database design (Products, Inventory, Sales)
- Low-stock detection for inventory alerts
- Top-selling product analytics
- Inventory valuation calculations
- System-wide KPI statistics
- CSV-based ETL pipeline using Pandas
- RESTful JSON API responses
- Interactive dashboard with API-driven visualisations
- Dockerised deployment with Gunicorn

---

# 🛠 Tech Stack

- Python 3
- Flask
- Flask-SQLAlchemy
- SQLite
- Pandas
- NumPy
- Matplotlib
- Gunicorn
- Docker

---

# 📁 Project Structure

- 🐍 `app6.py` – Flask application (routes & dashboard)
- 🗄️ `models.py` – Database models (Products, Inventory, Sales)
- 🔄 `load_data.py` – ETL pipeline for CSV ingestion
- 📊 `clean_inventory2.csv` – Source dataset
- 🗃️ `inventory.db` – SQLite database
- 🌐 `templates/index.html` – Dashboard UI
- ⚙️ `static/app.js` – Frontend logic (API calls, charts)
- 🎨 `static/style.css` – UI styling
- 📦 `requirements.txt` – Python dependencies
- 🐳 `Dockerfile` – Container configuration
- 🚫 `.dockerignore` – Excludes unnecessary files from Docker build
- 🚫 `.gitignore` – Excludes files from Git tracking

---

# 🔌 API Endpoints

## 🏠 Dashboard
- `GET /dashboard` → Loads interactive dashboard UI

## 🧾 Products
- `GET /products`
- `GET /product/<product_id>`
- `POST /product`
- `PUT /product/<product_id>`
- `DELETE /product/<product_id>`

## 📊 Analytics
- `GET /stats` → KPI summary
- `GET /low-stock` → Low stock alerts
- `GET /top-selling` → Top-selling products
- `GET /inventory-value` → Total stock value

---

# ⚙️ Setup Instructions

## Clone repository
git clone https://github.com/kb1278/flask-inventory-management-api.git
cd flask-inventory-management-api

## Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows

## Install dependencies
pip install -r requirements.txt

## Load dataset
python load_data.py

## Run application
python app6.py

## Open in browser
http://127.0.0.1:5000/dashboard

---

# 🐳 Run with Docker

docker build -t inventory-api .

docker run -p 5000:5000 inventory-api

---

# 🎯 Project Highlights

- Built a full REST API using Flask and SQLAlchemy
- Designed a normalized relational database architecture
- Implemented ETL pipeline using Pandas for data ingestion
- Developed analytics endpoints for business KPIs
- Built interactive dashboard with API-driven visualisations
- Containerised application using Docker and Gunicorn

---

# 🚀 Future Improvements

- User authentication system (Admin login)
- Real-time dashboard updates (WebSockets / polling)
- Machine learning-based demand forecasting
- Cloud deployment (Azure / Render / AWS)

---

