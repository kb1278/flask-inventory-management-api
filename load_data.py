import pandas as pd
from app6 import app, db
from models import Product, Inventory, Sales

CSV_PATH = "clean_inventory2.csv"

def safe_float(x):
    try:
        return float(x)
    except:
        return 0.0

def safe_int(x):
    try:
        return int(float(x))
    except:
        return 0

df = pd.read_csv(
    CSV_PATH,
    dtype=str,
    engine="python",
    on_bad_lines="skip"
)

df.columns = df.columns.str.strip()
df = df.fillna("0")

expected_cols = [
    "Product_ID", "Product_Name", "Category",
    "Supplier_ID", "Supplier_Name",
    "Stock_Quantity", "Reorder_Level", "Reorder_Quantity",
    "Unit_Price", "Date_Received", "Last_Order_Date",
    "Expiration_Date", "Warehouse_Location",
    "Sales_Volume", "Inventory_Turnover_Rate",
    "Status"
]

missing_cols = [col for col in expected_cols if col not in df.columns]
if missing_cols:
    raise ValueError(f"Missing columns: {missing_cols}")

print("Rows loaded:", len(df))

with app.app_context():

    db.session.query(Sales).delete()
    db.session.query(Inventory).delete()
    db.session.query(Product).delete()
    db.session.commit()

    for _, row in df.iterrows():

        product = Product(
            product_id=row["Product_ID"],
            product_name=row["Product_Name"],
            category=row["Category"],
            supplier_id=row["Supplier_ID"],
            supplier_name=row["Supplier_Name"],
            unit_price=safe_float(row["Unit_Price"]),
            status=row["Status"]
        )

        inventory = Inventory(
            product_id=row["Product_ID"],
            stock_quantity=safe_int(row["Stock_Quantity"]),
            reorder_level=safe_int(row["Reorder_Level"]),
            reorder_quantity=safe_int(row["Reorder_Quantity"]),
            warehouse_location=row["Warehouse_Location"]
        )

        sales = Sales(
            product_id=row["Product_ID"],
            sales_volume=safe_int(row["Sales_Volume"]),
            inventory_turnover_rate=safe_float(row["Inventory_Turnover_Rate"])
        )

        db.session.add(product)
        db.session.add(inventory)
        db.session.add(sales)

    db.session.commit()

print("✅ ETL completed successfully")