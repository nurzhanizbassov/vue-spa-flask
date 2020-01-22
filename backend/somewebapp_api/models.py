"""
models.py

Contains classes mapped by ORM to the database tables.

"""

import jwt

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class BaseAppModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(
            db.DateTime,
            onupdate=datetime.utcnow)
    enabled = db.Column(db.Boolean, default=True)


class Role(BaseAppModel):
    __tablename__ = 'roles'

    def __init__(self,name_en, name_kz, name_ru):
        self.name_en = name_en
        self.name_kz = name_kz
        self.name_ru = name_ru

    name_en = db.Column(db.String(64))
    name_kz = db.Column(db.String(64), nullable=True)
    name_ru = db.Column(db.String(64), nullable=True)

    def to_dict(self):
        return dict(id=self.id,
                    name_en=self.name_en,
                    name_kz=self.name_kz,
                    name_ru=self.name_ru,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    updated_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'))

    def __str__(self):
        return str(self.id)


class User(BaseAppModel):
    __tablename__ = 'users'

    def __init__(
            self, email, username, phone_number,
            password, role_id, enabled):
        self.email = email
        self.username = username
        self.phone_number = phone_number
        self.password = generate_password_hash(password, method='sha256')
        self.role_id = role_id
        self.games = []
        self.enabled = enabled

    email = db.Column(db.String(64), unique=True, nullable=False)
    username = db.Column(db.String(64), nullable=True)
    phone_number = db.Column(db.String(12), unique=True)
    password = db.Column(db.String(255), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    role = db.relationship(Role, backref='users')
    games = db.relationship('Game', backref='user', lazy=True)

    @classmethod
    def authenticate(cls, **kwargs):
        email = kwargs.get('email')
        password = kwargs.get('password')

        if not email or not password:
            return None

        user = cls.query.filter_by(email=email).filter_by(enabled=True).first()
        if not user or not check_password_hash(user.password, password):
            return None

        return user

    def to_dict(self):
        return dict(id=self.id,
                    email=self.email,
                    username=self.username,
                    phone_number=self.phone_number,
                    role_id=self.role_id,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    updated_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    enabled=self.enabled)

    def __str__(self):
        return str(self.email)


class Game(BaseAppModel):
    __tablename__ = 'games'

    def __init__(self, name_en, name_kz, name_ru, game_type_id, user_id):
        self.name_en = name_en
        self.name_kz = name_kz
        self.name_ru = name_ru
        self.game_type_id = game_type_id,
        self.user_id = user_id

    name_en = db.Column(db.String(64))
    name_kz = db.Column(db.String(64), nullable=True)
    name_ru = db.Column(db.String(64), nullable=True)
    game_type_id = db.Column(
            db.Integer,
            db.ForeignKey('game_types.id'),
            nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        return dict(id=self.id,
                    name_en=self.name_en,
                    name_kz=self.name_kz,
                    name_ru=self.name_ru,
                    game_type_id=self.game_type_id,
                    user_id=self.user_id,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    updated_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    enabled=self.enabled)


class GameType(BaseAppModel):
    __tablename__ = 'game_types'

    def __init__(self, name_en, name_kz, name_ru):
        self.name_en = name_en
        self.name_kz = name_kz
        self.name_ru = name_ru

    name_en = db.Column(db.String(64))
    name_kz = db.Column(db.String(64), nullable=True)
    name_ru = db.Column(db.String(64), nullable=True)

    def to_dict(self):
        return dict(id=self.id,
                    name_en=self.name_en,
                    name_kz=self.name_kz,
                    name_ru=self.name_ru,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    updated_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    enabled=self.enabled)


    def __str__(self):
        return str(self.id)
