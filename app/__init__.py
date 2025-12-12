from flask import Flask, render_template
from app.config import DevelopmentConfig, TestingConfig, ProductionConfig
from app.extensions import db, migrate
from flask import render_template
from app.forms import ContactForm

config_map = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}


def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config_map[config_name])

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    from app.posts import posts_bp
    from app.users import users_bp
    from app.products import products_bp

    app.register_blueprint(posts_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(products_bp)

    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html"), 404

    @app.context_processor
    def inject_theme():
        from flask import request
        theme = request.cookies.get("theme", "light")
        return {"theme": theme}

    @app.route("/contact", methods=["GET", "POST"])
    def contact():
        form = ContactForm()
        return render_template("contact.html", form=form)

    @app.route("/")
    def index():
        return render_template("index.html")

    return app
