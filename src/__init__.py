from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    from src.errors.handlers import errors
    from src.locations.routes import locations_bp
    from src.main.routes import main
    from src.product_movements.routes import product_movements_bp
    from src.products.routes import products_bp

    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.register_blueprint(main)
    app.register_blueprint(products_bp)
    app.register_blueprint(locations_bp)
    app.register_blueprint(product_movements_bp)
    app.register_blueprint(errors)

    return app
