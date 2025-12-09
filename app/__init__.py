from flask import Flask

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY="dev-key",
)

from app import views
from app.users import users_bp
from app.products import products_bp

app.register_blueprint(users_bp)
app.register_blueprint(products_bp)

@app.context_processor
def inject_theme():
    from flask import request
    theme = request.cookies.get("theme", "light")
    return {"theme": theme}

