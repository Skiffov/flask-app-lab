from flask import Blueprint, render_template
from app.products.models import Product

products_bp = Blueprint(
    "products",
    __name__,
    url_prefix="/products"
)


@products_bp.route("/")
def index():
    products = Product.query.all()
    return render_template("products/templates/index.html", products=products)
