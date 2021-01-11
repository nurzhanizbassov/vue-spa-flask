from .. import db, flask_bcrypt
from datetime import datetime


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(
            db.DateTime,
            onupdate=datetime.utcnow)
    enabled = db.Column(db.Boolean, default=True)
