
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

# postgres://ctaldselrhabie:9a826534bba7e4ee5b22ead1f5399633313957a8fd9497c3ac8d37ebc2a1cb6b@ec2-54-152-175-141.compute-1.amazonaws.com:5432/d8u99e7hchnnce