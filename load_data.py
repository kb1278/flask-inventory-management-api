import pandas as pd

from app6 import app
from models import db, Product, Inventory, Sales

# ----------------------------
# CONFIG
# ----------------------------
CSV_PATH = "clean_inventory2.csv"

<<<<<<< HEAD
=======
# ----------------------------
# LOAD + CLEAN DATA
# ----------------------------
>>>>>>> 2474566 (Fix load_data ETL: CSV parsing, NaN handling, and type safety)
df = pd.read_csv(CSV_PATH, sep="\t")
df.columns = df.columns.str.strip()

# Replace missing values safely
df = df.fillna(0)

# ----------------------------
# LOAD INTO DATABASE
# ----------------------------
with app.app_context():

    # Clear existing data
    Sales.query.delete()
    Inventory.query.delete()
    Product.query.delete()
    db.session.commit()

    for _, row in df.iterrows():

        # ----------------------------
        # PRODUCT TABLE
        # ----------------------------
        product = Product(
            product_id=str(row["Product_ID"]),
            product_name=str(row["Product_Name"]),
            category=str(row["Category"]),
            supplier_id=str(row["Supplier_ID"]),
            supplier_name=str(row["Supplier_Name"]),
            unit_price=float(row["Unit_Price"]),
            status=str(row["Status"])
        )

        # ----------------------------
        # INVENTORY TABLE
        # ----------------------------
        inventory = Inventory(
            product_id=str(row["Product_ID"]),
            stock_quantity=int(float(row["Stock_Quantity"])),
            reorder_level=int(float(row["Reorder_Level"])),
            reorder_quantity=int(float(row["Reorder_Quantity"])),
            warehouse_location=str(row["Warehouse_Location"])
        )

        # ----------------------------
        # SALES TABLE
        # ----------------------------
        sales = Sales(
            product_id=str(row["Product_ID"]),
            sales_volume=int(float(row["Sales_Volume"])),
            inventory_turnover_rate=float(row["Inventory_Turnover_Rate"])
        )

        db.session.add(product)
        db.session.add(inventory)
        db.session.add(sales)

    db.session.commit()

<<<<<<< HEAD
print("Data loaded successfully")
=======
print("✅ Data loaded successfully")
>>>>>>> 2474566 (Fix load_data ETL: CSV parsing, NaN handling, and type safety)
