from flask import Flask

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY="dev")

# реєстрація блюпринтів
from app.users import users_bp
from app.products import products_bp

app.register_blueprint(users_bp)
app.register_blueprint(products_bp)

# старі маршрути з lab2, якщо ти їх залишив
from app import views  # noqa
