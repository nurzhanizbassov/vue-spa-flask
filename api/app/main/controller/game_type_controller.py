from flask import request
from flask_restx import Resource

from app.main.util.decorator import token_required
from ..util.dto import GameTypeDto
from ..service.game_type_service import (
    get_all_game_types,
    get_game_type
)

api = GameTypeDto.api
_game_type = GameTypeDto.game_type


@api.route('/')
class GameTypeList(Resource):
    @api.doc('list_of_game_types')
    @token_required
    @api.marshal_list_with(_game_type, envelope='data')
    def get(self):
        """List all game types"""
        return get_all_game_types()


@api.route('/<id>')
@api.param('id', 'The Role identifier')
@api.response(404, 'Role not found.')
class GameType(Resource):
    @api.doc('get a game type')
    @token_required
    @api.marshal_with(_game_type)
    def get(self, id):
        """get a game_type given its identifier"""
        game_type = get_game_type(id)
        if not game_type:
            api.abort(404)
        else:
            return game_type
