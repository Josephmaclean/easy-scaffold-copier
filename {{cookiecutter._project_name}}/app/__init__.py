from werkzeug.utils import import_string
from flask_easy import FlaskEasy


def create_app(config="config.DevelopmentConfig"):
    cfg = import_string(config)
    app = FlaskEasy().init_app(**{
        "import_name": __name__,
        "config": cfg
    })
    return app
