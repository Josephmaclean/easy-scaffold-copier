from flask import Flask
from werkzeug.utils import import_string
from flask_easy import FlaskEasy


def create_app(config="config.DevelopmentConfig"):
    app = Flask(__name__)
    cfg = import_string(config)
    app.config.from_object(cfg)
    return FlaskEasy().init_app(app)
