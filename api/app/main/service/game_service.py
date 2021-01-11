import uuid
import datetime

from app.main import db
from app.main.model.game import Game


def get_all_games():
    return Game.query.all()


def get_all_user_games(id):
    games = Game.query.filter_by(user_id=id).filter_by(enabled=True).all()
    return games


def create_game(payload):

    game = Game(
        payload['nameKz'],
        payload['nameRu'],
        payload['nameEn'],
        payload['gameTypeId'],
        payload['userId']
    )

    db.session.add(game)
    db.session.commit()

    response_object = {
        'status': 'success',
        'message': 'Entity successfully created.',
    }
    return response_object, 200


def update_game(id, payload):

    game_to_edit = Game.query.filter_by(id=payload['gameId']).first()
    game_to_edit.name_en = payload['nameEn']
    game_to_edit.name_kz = payload['nameKz']
    game_to_edit.name_ru = payload['nameRu']
    game_to_edit.game_type_id = payload['gameTypeId']

    db.session.commit()

    response_object = {
        'status': 'success',
        'message': 'Entity successfully updated.',
    }
    return response_object, 200


def get_game(id):
    return Game.query.filter_by(id=id).first()


def delete_game(game_id, payload):

    game_to_delete = Game.query.filter_by(
            id=game_id,
            user_id=payload['userId']).first()

    if not game_to_delete:

        response_object = {
            'status': 'failure',
            'message': 'Entity not found.',
        }
        return response_object, 404

    game_to_delete.enabled = False
    db.session.commit()

    response_object = {
        'status': 'success',
        'message': 'Entity successfully deleted.',
    }
    return response_object, 200
