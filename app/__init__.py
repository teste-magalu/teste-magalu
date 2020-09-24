from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_cors import CORS
from app.config import DevelopmentConfig, TestingConfig, ProductionConfig

db = SQLAlchemy()

def create_app(**config_overrides):
    app = Flask(__name__)

    # Load config
    # app.config.from_pyfile('settings.py')
    from app.config import get_env_variable
    environment = get_env_variable('ENV')

    if environment == 'development':
        # app.config.from_object('app.config.DevelopmentConfig')
        app.config.from_object(DevelopmentConfig)
    if environment == 'testing':
        app.config.from_object(TestingConfig)
    if environment == 'production':
        app.config.from_object(ProductionConfig)

    # apply overrides for tests
    app.config.update(config_overrides)

    # initialize db
    db.init_app(app)
    migrate = Migrate(app, db)

    # cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    # import blueprints
    from .blueprints.routes import api_v1

    # register blueprints
    app.register_blueprint(api_v1, url_prefix='/api/v1')

    return app

from .blueprints import routes
