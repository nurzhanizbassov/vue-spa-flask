from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required, token_required
from ..util.dto import GameDto
from ..service.game_service import (
        get_all_games,
        get_all_user_games,
        get_game,
        update_game,
        delete_game,
        create_game
    )

api = GameDto.api
_game = GameDto.game


@api.route('/')
class GameList(Resource):
    @api.doc('list_of_games')
    # @admin_token_required
    @api.marshal_list_with(_game, envelope='data')
    def get(self):
        """List all games"""
        return get_all_games()

    @api.doc('create a game')
    @api.marshal_with(_game)
    def post(self):
        """create a game"""
        return create_game(api.payload)


@api.route('/user/<id>')
@api.param('id', 'The user identifier')
class UserGameList(Resource):
    @api.doc('list_of_user_games')
    @token_required
    @api.marshal_list_with(_game, envelope='data')
    def get(self, id):
        """List all user games"""
        return get_all_user_games(id)


@api.route('/<id>')
@api.param('id', 'The game identifier')
@api.response(404, 'Game not found.')
class Game(Resource):
    @api.doc('get a game')
    @token_required
    @api.marshal_with(_game)
    def get(self, id):
        """get a game given its identifier"""
        game = get_game(id)
        if not game:
            api.abort(404)
        else:
            return game


    @api.doc('update a game')
    @token_required
    @api.marshal_with(_game)
    def put(self, id):
        """update a game given its identifier"""
        game = update_game(id, api.payload)
        if not game:
            api.abort(404)
        else:
            return game


    @api.doc('delete a game')
    @token_required
    @api.marshal_with(_game)
    def delete(self, id):
        """delete a game given its identifier"""
        return delete_game(id, api.payload)
