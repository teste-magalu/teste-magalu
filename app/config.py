import os
import secrets

basedir = os.path.abspath(os.path.dirname(__file__))

def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = f"Expected environment variable '{name}' not set."
        raise Exception(message)

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    # SECRET_KEY = secrets.token_hex(16)
    SECRET_KEY = os.urandom(16)
    ASSETS_DEBUG = True
    ENV = 'development'
    # FLASK_APP = "manage.py"

    #DATABASE ENVIRONMENT VARIABLES
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db_test.db'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False
    ENV = 'production'
    
    #DATABASE ENVIRONMENT VARIABLES
    POSTGRES_USER = get_env_variable('POSTGRES_USER')
    POSTGRES_PW = get_env_variable('POSTGRES_PW')
    POSTGRES_URL = get_env_variable('POSTGRES_URL')
    POSTGRES_DB = get_env_variable('POSTGRES_DB')

    DATABASE_URI = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}/{POSTGRES_DB}'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class StagingConfig(Config):
    """
    Staging configurations
    """
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_ECHO = True
    ASSETS_DEBUG = True

class TestingConfig(Config):
    """
    Testing configurations
    """
    TESTING = True
