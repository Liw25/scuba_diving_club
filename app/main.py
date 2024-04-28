from flask import Flask
from config import get_config
from database import init_db
from models import Base
from views import register_routes
import os


def create_app(config_name):
    """Factory function to create Flask app based on configuration."""
    # Create the Flask application
    app = Flask(__name__)

    # Load configuration from the config object by name
    app.config.from_object(get_config(config_name))

    # Initialize database
    init_db()

    # Register routes
    register_routes(app)

    return app


if __name__ == '__main__':
    # Get the environment name from env variable (default to development)
    env_name = os.getenv('FLASK_ENV', 'development')

    # Create the app using the factory function
    app = create_app(env_name)

    # Run the application
    app.run(host='0.0.0.0', port=5000, debug=app.config['DEBUG'])
