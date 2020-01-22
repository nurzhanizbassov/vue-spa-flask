"""

application.py

Creates intance of Flask and registers all required objects
(config, db, blueprint 'api', CORS, redis etc).

"""

import redis

from flask import Flask
from flask_cors import CORS
from rq import Queue


def create_app(app_name='SOMEWEBAPP_API'):
    app = Flask(app_name)
    app.config.from_object('somewebapp_api.config.BaseConfig')

    from somewebapp_api.api import api
    CORS(api)
    app.register_blueprint(api, url_prefix="/api")

    from somewebapp_api.models import db
    db.init_app(app)

    # Configure Redis queue
    r = redis.Redis()
    q = Queue(connection=r)

    app.redis_queue = q

    return app
