class Config:
    DB_HOST = ""
    DB_USER = ""
    DB_NAME = ""
    DB_PASSWORD = ""
    DB_ENGINE = "{{cookiecutter.project_database}}"


class DevelopmentConfig(Config):
    pass


class ProductionConfig(Config):
    pass


class TestingConfig(Config):
    pass
