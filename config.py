class Config(object):
    TESTING = True
    ENV = 'development'
    FLASK_DEBUG = True
    CSRF_ENABLED = False
    SECRET_KEY = 'test-key'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    DB_SERVER = 'localhost'
    DB_USER = 'postgres'
    DB_PASSWORD = 'system1'
    DB_NAME = 'quesosfondiqr'

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_SERVER}/{self.DB_NAME}"


class ProductionConfig(Config):
    TESTING = False
    DB_SERVER = 'localhost'
    FLASK_ENV = 'production'
    FLASK_DEBUG = False
    FLASK_TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    pass


class TestingConfig(Config):
    DATABASE_URI = 'sqlite:///:memory:'
