import jwt
import datetime
from .. import db, flask_bcrypt
from app.main.model.blacklist import BlacklistToken
from ..config import key
from .role import Role
from .game import Game
from flask import jsonify
from .base_model import BaseModel


class User(BaseModel):
    """ User Model for storing user related details """
    __tablename__ = "user"

    def __init__(
            self, email, username, phone_number,
            role_id, password, enabled=False):
        self.email = email
        self.username = username
        self.phone_number = phone_number
        self.role_id = role_id
        self.password = password
        self.enabled = enabled
        self.games = []

    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255))
    username = db.Column(db.String(50), unique=True)
    phone_number = db.Column(db.String(12), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    games = db.relationship('Game', backref='user', lazy=True)


    @property
    def password(self):
        raise AttributeError('password: write-only field')


    @password.setter
    def password(self, password):
        self.password_hash = (
            flask_bcrypt.generate_password_hash(password).decode('utf-8')
        )


    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)


    @staticmethod
    def encode_auth_token(user_id, email, role):
        """
        Generates the Auth Token
        :return: string
        """

        try:
            payload = {
                'id': user_id,
                'email': email,
                'role': role.name_en,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                'iat': datetime.datetime.utcnow(),
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, key)
            print('user. decode_auth_token. payload:', payload)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                return 'Token blacklisted. Please log in again.'
            else:
                return payload['id']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def __repr__(self):
        return "<User '{}'>".format(self.username)
