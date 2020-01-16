import os


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    DEBUG=False
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS', True)


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    ENV='development'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % (os.path.join(PROJECT_ROOT, "db.sqlite3"))
    DOMAIN = 'http://localhost:5000'


class TestingConfig(BaseConfig):
    ENV='testing'
    TESTING = True
    DOMAIN = 'http://testserver'
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
