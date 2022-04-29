from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask import Blueprint
main = Blueprint('main',__name__)

from main import main 
from app import app

def create_app(config_name):
    #....
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # setting config
    from .request import configure_request
    configure_request(app)

    return app

from . import views,error    

# # Initializing application
# app = Flask(__name__,instance_relative_config = True)
# # we pass instance_relative_config as parameter which allow us to connect to the instance/folder
# #  when the app instance is created.

# # Setting up configuration
# app.config.from_object(DevConfig)
# app.config.from_pyfile('config.py')#connects to the config.py file and 
# # all its contents are appended to the app.config
# bootstrap = Bootstrap(app)

# from app import views
# from app import error