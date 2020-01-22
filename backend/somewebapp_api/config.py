"""
config.py

Contains settings for the Flask backend.

"""


class BaseConfig(object):
    DEBUG = True
    POSTGRES_SETTINGS = {
        'user': 'swa',
        'password': 'swa',
        'host': 'localhost',
        'port': '5432',
        'db': 'somewebapp'
    }
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
            POSTGRES_SETTINGS['user'],
            POSTGRES_SETTINGS['password'],
            POSTGRES_SETTINGS['host'],
            POSTGRES_SETTINGS['port'],
            POSTGRES_SETTINGS['db']
            )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Used for security (signing cookies). Should be set
    # to something long and comlicated.
    SECRET_KEY = 'zaplatiChekannoiMonetoi'

    USER_ROLES = {
        1: 'ADMIN',
        2: 'STANDARD'
    }

    CORS_HEADERS = 'Content-Type'
