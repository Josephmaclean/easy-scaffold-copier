from werkzeug.utils import import_string
from flask_easy import FlaskEasy


cfg = import_string("config.DevelopmentConfig")


def create_app(config=cfg):
    app = FlaskEasy().init_app(**{
        "import_name": __name__,
        "config": config
    })
    return app
