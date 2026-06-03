import pandas as pd
from datetime import datetime

from app1 import app
from models import db, Product, Inventory, Sales

CSV_PATH = r"C:\Users\bhamr\OneDrive\Documents\clean_inventory2.csv"

df = pd.read_csv(CSV_PATH)

with app.app_context():

    # Optional: clear existing data
    Sales.query.delete()
    Inventory.query.delete()
    Product.query.delete()
    db.session.commit()

    for _, row in df.iterrows():

        product = Product(
            product_id=str(row["Product_ID"]),
            product_name=row["Product_Name"],
            category=row["Category"],
            supplier_id=str(row["Supplier_ID"]),
            supplier_name=row["Supplier_Name"],
            unit_price=float(row["Unit_Price"]),
            status=row["Status"]
        )

        inventory = Inventory(
            product_id=str(row["Product_ID"]),
            stock_quantity=int(row["Stock_Quantity"]),
            reorder_level=int(row["Reorder_Level"]),
            reorder_quantity=int(row["Reorder_Quantity"]),
            warehouse_location=row["Warehouse_Location"]
        )

        sales = Sales(
            product_id=str(row["Product_ID"]),
            sales_volume=int(row["Sales_Volume"]),
            inventory_turnover_rate=float(row["Inventory_Turnover_Rate"])
        )

        db.session.add(product)
        db.session.add(inventory)
        db.session.add(sales)

    db.session.commit()

print("Data loaded successfully")