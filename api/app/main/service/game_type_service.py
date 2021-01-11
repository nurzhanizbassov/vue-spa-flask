import uuid
import datetime

from app.main import db
from app.main.model.game_type import GameType


def get_all_game_types():
    return GameType.query.all()


def get_game_type(id):
    return GameType.query.filter_by(id=id).first()
