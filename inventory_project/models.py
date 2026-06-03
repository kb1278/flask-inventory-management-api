from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# -------------------------
# PRODUCT TABLE
# -------------------------
class Product(db.Model):
    __tablename__ = "products"

    product_id = db.Column(db.String, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    supplier_id = db.Column(db.String(50))
    supplier_name = db.Column(db.String(100))
    unit_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20))

    # Relationships (one-to-one style)
    inventory = db.relationship(
        "Inventory",
        backref="product",
        uselist=False,
        cascade="all, delete-orphan"
    )

    sales = db.relationship(
        "Sales",
        backref="product",
        uselist=False,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Product {self.product_name}>"


# -------------------------
# INVENTORY TABLE
# -------------------------
class Inventory(db.Model):
    __tablename__ = "inventory"

    id = db.Column(db.Integer, primary_key=True)

    product_id = db.Column(
        db.String,
        db.ForeignKey("products.product_id"),
        nullable=False
    )

    stock_quantity = db.Column(db.Integer, nullable=False)
    reorder_level = db.Column(db.Integer)
    reorder_quantity = db.Column(db.Integer)
    warehouse_location = db.Column(db.String(150))

    def __repr__(self):
        return f"<Inventory ProductID {self.product_id}>"


# -------------------------
# SALES TABLE
# -------------------------
class Sales(db.Model):
    __tablename__ = "sales"

    id = db.Column(db.Integer, primary_key=True)

    product_id = db.Column(
        db.String,
        db.ForeignKey("products.product_id"),
        nullable=False
    )

    sales_volume = db.Column(db.Integer)
    inventory_turnover_rate = db.Column(db.Float)

    def __repr__(self):
        return f"<Sales ProductID {self.product_id}>"