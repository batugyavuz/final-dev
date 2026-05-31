from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_by_name

# Initialize database extension
db = SQLAlchemy()

def create_app(config_name='development'):
    """Application factory to create and configure the Flask app."""
    app = Flask(__name__)
    
    # Load configuration by name (development, production, etc.)
    config_obj = config_by_name.get(config_name, config_by_name['default'])
    app.config.from_object(config_obj)
    
    # Initialize extensions
    db.init_app(app)
    
    # Import and register blueprints
    from app.main import main_bp
    from app.items import items_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(items_bp, url_prefix='/items')
    
    return app
