from app6 import app, db
from models import Product
import csv

with app.app_context():
    with open("your_file.csv", "r", encoding="utf-8") as file:

        reader = csv.reader(file)
        next(reader)  # skip header

        for row in reader:
            if len(row) < 10:
                continue

            product = Product(
                product_id=row[0],
                product_name=row[1],
                category=row[2],
                supplier_id=row[3],
                supplier_name=row[4],
                stock_quantity=int(row[5] or 0),
                reorder_level=int(row[6] or 0),
                reorder_quantity=int(row[7] or 0),
                unit_price=float(row[8] or 0),
                status=row[-1]
            )

            db.session.add(product)

        db.session.commit()

print("DONE ✔ Data inserted successfully")