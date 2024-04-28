import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

class Config:
    """Base configuration class."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///scuba_diving_club.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """Development configuration class."""
    DEBUG = True

class TestingConfig(Config):
    """Testing configuration class."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL', 'sqlite:///test_scuba_diving_club.db')

class ProductionConfig(Config):
    """Production configuration class."""
    DEBUG = False

# Dictionary to hold all your configurations
config_by_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}

def get_config(config_name):
    """Retrieve and return the appropriate configuration subclass."""
    return config_by_name.get(config_name, 'development')
