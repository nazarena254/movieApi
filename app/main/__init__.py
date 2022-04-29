from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask import Blueprint
from main import main 
main = Blueprint('main',__name__)
from config import DevConfig

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Registering the blueprint
    from app.main import main as main_blueprint #from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app  # Will add the views and forms

from . import views,error
