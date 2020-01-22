"""

api.py
Set of api endpoints for communicating with the frontend SPA.

"""

import jwt
import time

from flask import Blueprint, jsonify, request, current_app
from somewebapp_api.models import (
    db, Game, GameType, User, Role
)
from somewebapp_api.exceptions import InvalidUserRoleException
from functools import wraps
from datetime import datetime, timedelta
from flask_cors import cross_origin

api = Blueprint('api', __name__)


def valid_role_required(user_role):
    def decorator(f):
        @wraps(f)
        def _verify(*args, **kwargs):
            auth_headers = request.headers.get('Authorization', '').split()

            invalid_msg = {
                'message': (
                    'Invalid token.'
                    ' Registration and/or authentication required'
                ),
                'authenticated': False
            }
            expired_msg = {
                'message': 'Expired token. Authenticate again.',
                'authenticated': False
            }

            if len(auth_headers) != 2:
                return jsonify(invalid_msg), 401

            try:

                payload = _decode_jwt(auth_headers[1])
                user = User.query.filter_by(email=payload['email']).first()

                if not user:
                    raise RuntimeError('User not found')

                if (
                    user_role != 'ADMIN' and
                    current_app.config['USER_ROLES'][user.role_id] !=
                    user_role):
                    raise InvalidUserRoleException(
                        'User with role {} tried to access resource '
                        'allowed for the {} role only.'
                        .format(current_app.config['USER_ROLES'][user.role_id],
                                user_role),
                        'errors'
                    )
                return f(user, *args, **kwargs)
            except jwt.ExpiredSignatureError:
                return jsonify(expired_msg), 401
            except (jwt.InvalidTokenError, Exception) as e:
                print(e)
                return jsonify(invalid_msg), 401

        return _verify
    return decorator


def _decode_jwt(token):
    return jwt.decode(token, current_app.config['SECRET_KEY'])


@api.route('/register/', methods=['POST'])
def register():
    data = request.get_json()
    print('register. data: ', data)

    if not _validate_email(data['email']):
        return jsonify('email_already_exists'), 200
    elif not _validate_phone_number(data['phoneNumber']):
        return jsonify('phone_number_already_exists'), 200
    elif not _validate_username(data['username']):
        return jsonify('username_not_valid'), 200
    elif not _validate_password(data['password']):
        return jsonify('password_not_valid'), 200
    elif not _validate_role(data['roleId']):
        return jsonify('role_not_valid'), 200

    user = User(
            email=data['email'],
            username=data['username'],
            phone_number=data['phoneNumber'],
            password=data['password'],
            role_id=data['roleId'],
            enabled=False)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201


def _validate_email(email):
    return not User.query.filter_by(email=email).all()


def _validate_phone_number(phone_number):
    return not User.query.filter_by(phone_number=phone_number).all()


def _validate_username(username):
    return len(username) >= 6 and len(username) <= 64


def _validate_password(password):
    return len(password) >= 6


def _validate_role(role_id):
    roles = [r.id for r in Role.query.all()]
    return int(role_id) in roles


@api.route('/login/', methods=['POST'])
def login():
    data = request.get_json()
    user = User.authenticate(**data)

    if not user:
        return jsonify(
            {'message': 'Invalid credentials',
             'authenticated': False}), 401

    token = jwt.encode({
        'email': user.email,
        'role': user.role.name_en,
        'iat': datetime.utcnow(),
        'exp': datetime.utcnow() + timedelta(minutes=30)},
        current_app.config['SECRET_KEY'])
    return jsonify({'token': token.decode('UTF-8')})


@api.route('/')
def home():
    response = {'msg': 'Some Web App Backend'}
    return jsonify(response)


@api.route('/users/')
@valid_role_required('ADMIN')
def get_all_users(self):
    users = User.query.order_by(User.id.asc()).all()

    response = [u.to_dict() for u in users]

    return jsonify(response)


@api.route('/users/edit/', methods=['PUT'])
@valid_role_required('ADMIN')
def edit_users(self):
    users = request.get_json()

    for user in users:
        _update_user(user)

    response = {'msg': 'Users edited'}
    return jsonify(response), 200


@api.route('/users/remove/', methods=['POST'])
@valid_role_required('ADMIN')
def remove_user(self):
    user_id = request.get_json()['userId']
    user = User.query.filter_by(id=user_id).first()
    user.enabled = False
    db.session.commit()

    response = {'msg': 'User disabled'}
    return jsonify(response), 200


def _update_user(user):
    user_to_update = User.query.get(user['id'])
    user_to_update.enabled = user['enabled']
    db.session.commit()


@api.route('/roles/')
def get_all_roles():
    roles = Role.query.all()
    response = [r.to_dict() for r in roles]

    return jsonify(response)


@api.route('/game-types/')
@valid_role_required('STANDARD')
def get_all_game_types(self):
    game_types = GameType.query.all()
    response = [gt.to_dict() for gt in game_types]

    return jsonify(response)


@api.route('/games/')
@valid_role_required('STANDARD')
def get_games(self):
    auth_headers = request.headers.get('Authorization', '').split()
    payload = _decode_jwt(auth_headers[1])
    user = User.query.filter_by(email=payload['email']).first()
    games = Game.query.filter_by(user_id=user.id).filter_by(enabled=True).all()

    response = [g.to_dict() for g in games]

    return jsonify(response)


@api.route('/games/add/', methods=['POST'])
@valid_role_required('STANDARD')
def add_game(self):

    auth_headers = request.headers.get('Authorization', '').split()

    user_data = _decode_jwt(auth_headers[1])
    user = User.query.filter_by(email=user_data['email']).first()
    game_data = request.get_json()

    game = Game(
            game_data['nameEn'],
            game_data['nameKz'],
            game_data['nameRu'],
            game_data['gameTypeId'],
            user.id)
    db.session.add(game)
    db.session.commit()
    response = {'msg': 'Game added'}
    return jsonify(response), 200


@api.route('/games/edit/', methods=['PUT'])
@valid_role_required('STANDARD')
def edit_game(self):

    auth_headers = request.headers.get('Authorization', '').split()

    user_data = _decode_jwt(auth_headers[1])
    user = User.query.filter_by(email=user_data['email']).first()
    game_data = request.get_json()

    game_to_edit = Game.query.filter_by(id=game_data['gameId']).first()
    game_to_edit.name_en = game_data['nameEn']
    game_to_edit.name_kz = game_data['nameKz']
    game_to_edit.name_ru = game_data['nameRu']
    game_to_edit.game_type_id = game_data['gameTypeId']

    db.session.commit()
    response = {'msg': 'Game updated'}
    return jsonify(response), 200


@api.route('/games/remove/', methods=['DELETE'])
@valid_role_required('STANDARD')
def remove_game(self):

    auth_headers = request.headers.get('Authorization', '').split()

    user_data = _decode_jwt(auth_headers[1])
    user = User.query.filter_by(email=user_data['email']).first()

    game_data = request.get_json()

    game = Game.query.filter_by(
            id=game_data['gameId'],
            user_id=user.id).first()

    game.enabled = False

    if game:
        db.session.commit()
        response = {'msg': 'Game deleted'}
    else:
        response = {'msg': 'Game not found'}
    return jsonify(response), 200


@api.route("/task")
def some_task():

    if request.args.get("n"):

        q = current_app.redis_queue

        job = q.enqueue(send_email_task, request.args.get("n"))

        return f"Task ({job.id}) added to queue at {job.enqueued_at}"

    return "No value for count provided"


# TODO: Add real
def send_email_task(n):

    """ Function that returns len(n) and simulates a delay """

    delay = 2

    print("Task running")
    print(f"Simulating sending an email with {delay} second delay")

    time.sleep(delay)

    print(len(n))
    print("Task complete")

    return len(n)
