import os
from app import create_app

# Read the environment and create the app instance
config_name = os.getenv('FLASK_ENV', 'development')
app = create_app(config_name)

if __name__ == '__main__':
    # Run the development server
    app.run()
