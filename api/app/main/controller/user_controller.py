from flask import request
from flask_restx import Resource
from app.main.util.decorator import admin_token_required
from ..util.dto import UserDto
from ..service.user_service import (
        create_user,
        get_all_users,
        get_user,
        update_users
    )

api = UserDto.api
_user = UserDto.user


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @admin_token_required
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        print('user_controller / reached')
        return get_all_users()

    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created.')
    @admin_token_required
    @api.doc('create a new user')
    def post(self):
        """Creates a new User """
        data = request.json
        return create_user(data=data)


@api.route('/<id>')
@api.param('id', 'The user identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @admin_token_required
    @api.marshal_with(_user)
    def get(self, id):
        """get a user given its identifier"""
        user = get_user(id)
        if not user:
            api.abort(404)
        else:
            return user


@api.route('/list/')
@api.response(404, 'Users not found.')
class UserList(Resource):
    @api.doc('Update users')
    @admin_token_required
    @api.marshal_with(_user)
    def put(self):
        """Updates users"""
        return update_users(api.payload)
