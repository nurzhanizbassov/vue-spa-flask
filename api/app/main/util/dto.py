from flask_restx import Namespace, fields
from ..model.game_type import GameType


class UserDto:
    api = Namespace('user', description='user related operations')

    role = api.model('role', {
        'id': fields.String(description='role identifier'),
        'name_kz': fields.String(required=True, description='name kazakh'),
        'name_ru': fields.String(required=True, description='name russian'),
        'name_en': fields.String(required=True, description='name english'),
    })

    user = api.model('user', {
        'id': fields.String(required=True, description='user id'),
        'email': fields.String(required=True, description='user email address'),
        'phone_number': fields.String(required=True, description='phone number'),
        'role': fields.Nested(role, description='role'),
        'username': fields.String(required=True, description='user username'),
        'enabled': fields.Boolean(required=True, description='enabled')
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })


class RoleDto:
    api = Namespace('role', description='role related operations')
    role = api.model('role', {
        'id': fields.String(description='role identifier'),
        'name_kz': fields.String(required=True, description='name kazakh'),
        'name_ru': fields.String(required=True, description='name russian'),
        'name_en': fields.String(required=True, description='name english'),
    })

class GameDto:

    api = Namespace('game', description='game related operations')

    game_type = api.model('game_type', {
        'id': fields.String(description='game_type identifier'),
        'name_kz': fields.String(required=True, description='name kazakh'),
        'name_ru': fields.String(required=True, description='name russian'),
        'name_en': fields.String(required=True, description='name english'),
    })

    game = api.model('game', {
        'id': fields.String(description='game identifier'),
        'game_type': fields.Nested(game_type, description='game_type'),
        'user_id': fields.String('user_id', description='user id'),
        'name_kz': fields.String(required=True, description='name kazakh'),
        'name_ru': fields.String(required=True, description='name russian'),
        'name_en': fields.String(required=True, description='name english'),
    })

class GameTypeDto:
    api = Namespace('game_type', description='game_type related operations')
    game_type = api.model('game_type', {
        'id': fields.String(description='game_type identifier'),
        'name_kz': fields.String(required=True, description='name kazakh'),
        'name_ru': fields.String(required=True, description='name russian'),
        'name_en': fields.String(required=True, description='name english'),
    })

