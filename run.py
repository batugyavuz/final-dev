import os
from app import create_app, db

# Read the environment and create the app instance
config_name = os.getenv('FLASK_ENV', 'development')
app = create_app(config_name)

# Ensure database tables are created automatically on startup
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # Run the development server
    app.run()
