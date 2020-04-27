
import os
#default config
class BaseConfig():
    DEBUG = False
    SECRET_KEY = 'my key'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    print(SQLALCHEMY_DATABASE_URI)

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False

class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'