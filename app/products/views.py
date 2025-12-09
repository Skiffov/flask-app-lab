from flask import render_template
from app.products import products_bp


@products_bp.route("/")
def index():
    products = [
        {"id": 1, "name": "Laptop", "price": 1000},
        {"id": 2, "name": "Mouse", "price": 25},
        {"id": 3, "name": "Keyboard", "price": 70},
    ]
    return render_template("products/index.html", products=products)
