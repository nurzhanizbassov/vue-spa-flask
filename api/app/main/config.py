"""
config.py

Contains settings for the Flask backend.

"""

class Config(object):
    DEBUG = False
    SECRET_KEY = 'TossACoinToYourWitcher'


class DevelopmentConfig(Config):
    DEBUG = True
    POSTGRES_SETTINGS = {
        'user': 'someapp',
        'password': 'someapp',
        'host': 'someapp-db',
        'port': '5432',
        'db': 'someapp'
    }

    # Dev db
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
            POSTGRES_SETTINGS['user'],
            POSTGRES_SETTINGS['password'],
            POSTGRES_SETTINGS['host'],
            POSTGRES_SETTINGS['port'],
            POSTGRES_SETTINGS['db']
            )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    USER_ROLES = {
        1: 'ADMIN',
        2: 'STANDARD'
    }

    CORS_HEADERS = 'Content-Type'


class TestingConfig(Config):
    DEBUG = True
    TESTING = True

    # Test db
    POSTGRES_SETTINGS = {
        'user': 'someapp',
        'password': 'someapp',
        'host': 'someapp-test-db',
        'port': '5432',
        'db': 'someapp'
    }
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
            POSTGRES_SETTINGS['user'],
            POSTGRES_SETTINGS['password'],
            POSTGRES_SETTINGS['host'],
            POSTGRES_SETTINGS['port'],
            POSTGRES_SETTINGS['db']
            )

    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
