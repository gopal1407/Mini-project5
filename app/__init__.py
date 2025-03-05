from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from app.config import Config
from app.models import Customer, CustomerAccount, Product, Order, OrderItem


# Initialize the extensions (db, migrate, bcrypt, jwt)
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
jwt = JWTManager()

# The function that creates and configures the app
def create_app():
    app = Flask(__name__)  # Create a Flask app instance
    app.config.from_object(Config)  # Apply configurations from Config class

    # Initialize the extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Import inside function to avoid circular imports
    from app.routes import main  
    app.register_blueprint(main)

    return app  # Return the fully configured app
