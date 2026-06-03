from flask import Flask, jsonify, request
from models import db, Product, Inventory, Sales

app = Flask(__name__)

# -------------------------
# DATABASE CONFIG
# -------------------------
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///inventory.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# -------------------------
# CREATE TABLES
# -------------------------
with app.app_context():
    db.create_all()


# -------------------------
# HEALTH CHECK
# -------------------------
@app.route("/")
def home():
    return jsonify({"message": "Inventory API running"})


# -------------------------
# GET ALL PRODUCTS
# -------------------------
@app.route("/products")
def get_products():
    products = Product.query.limit(100).all()

    return jsonify({
        "count": len(products),
        "data": [
            {
                "product_id": p.product_id,
                "product_name": p.product_name,
                "category": p.category,
                "unit_price": p.unit_price,
                "status": p.status
            }
            for p in products
        ]
    })


# -------------------------
# GET SINGLE PRODUCT
# -------------------------
@app.route("/product/<product_id>")
def get_product(product_id):
    product = db.session.get(Product, product_id)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    return jsonify({
        "product_id": product.product_id,
        "product_name": product.product_name,
        "category": product.category,
        "unit_price": product.unit_price,
        "status": product.status,
        "sales_volume": product.sales.sales_volume if product.sales else 0,
        "stock_quantity": product.inventory.stock_quantity if product.inventory else 0
    })


# -------------------------
# CREATE PRODUCT
# -------------------------
@app.route("/product", methods=["POST"])
def add_product():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No input data provided"}), 400

    required_fields = ["product_id", "product_name", "unit_price"]

    missing = [f for f in required_fields if f not in data]
    if missing:
        return jsonify({"error": f"Missing fields: {missing}"}), 400

    new_product = Product(
        product_id=data["product_id"],
        product_name=data["product_name"],
        category=data.get("category"),
        supplier_id=data.get("supplier_id"),
        supplier_name=data.get("supplier_name"),
        unit_price=float(data["unit_price"]),
        status=data.get("status")
    )

    db.session.add(new_product)
    db.session.commit()

    return jsonify({"message": "Product created successfully"}), 201


# -------------------------
# UPDATE PRODUCT
# -------------------------
@app.route("/product/<product_id>", methods=["PUT"])
def update_product(product_id):
    product = db.session.get(Product, product_id)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json()

    product.product_name = data.get("product_name", product.product_name)
    product.category = data.get("category", product.category)
    product.unit_price = data.get("unit_price", product.unit_price)
    product.status = data.get("status", product.status)

    db.session.commit()

    return jsonify({"message": "Product updated successfully"})


# -------------------------
# DELETE PRODUCT
# -------------------------
@app.route("/product/<product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = db.session.get(Product, product_id)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    db.session.delete(product)
    db.session.commit()

    return jsonify({"message": "Product deleted successfully"})

@app.route("/stats")
def stats():
    return jsonify({
        "total_products": Product.query.count(),
        "total_inventory_records": Inventory.query.count(),
        "total_sales_records": Sales.query.count()
    })



# -------------------------
# LOW STOCK PRODUCTS
# -------------------------
@app.route("/low-stock")
def low_stock():

    products = (
        db.session.query(Product, Inventory)
        .join(Inventory)
        .filter(Inventory.stock_quantity < Inventory.reorder_level)
        .all()
    )

    return jsonify([
        {
            "product_id": p.product_id,
            "product_name": p.product_name,
            "stock_quantity": i.stock_quantity,
            "reorder_level": i.reorder_level
        }
        for p, i in products
    ])


# -------------------------
# TOP SELLING PRODUCTS
# -------------------------
@app.route("/top-selling")
def top_selling():

    products = (
        db.session.query(Product, Sales)
        .join(Sales)
        .order_by(Sales.sales_volume.desc())
        .limit(10)
        .all()
    )

    return jsonify([
        {
            "product_id": p.product_id,
            "product_name": p.product_name,
            "sales_volume": s.sales_volume
        }
        for p, s in products
    ])


# -------------------------
# INVENTORY VALUE
# -------------------------
@app.route("/inventory-value")
def inventory_value():

    products = (
        db.session.query(Product, Inventory)
        .join(Inventory)
        .all()
    )

    total_value = sum(
        p.unit_price * i.stock_quantity
        for p, i in products
    )

    return jsonify({
        "inventory_value": round(total_value, 2)
    })

from flask import render_template

@app.route("/dashboard")
def dashboard():
    return render_template("index.html")



# -------------------------
# RUN APP
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)