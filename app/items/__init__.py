from flask import Blueprint

items_bp = Blueprint('items', __name__)

# Import routes at the bottom to avoid circular dependencies
from app.items import routes
