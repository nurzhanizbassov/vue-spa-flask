from .. import db, flask_bcrypt
from .base_model import BaseModel


class Game(BaseModel):
    __tablename__ = 'game'

    def __init__(self, name_kz, name_ru, name_en, game_type_id, user_id):
        self.name_kz = name_kz
        self.name_ru = name_ru
        self.name_en = name_en
        self.game_type_id = game_type_id,
        self.user_id = user_id

    name_kz = db.Column(db.String(64), nullable=True)
    name_ru = db.Column(db.String(64), nullable=True)
    name_en = db.Column(db.String(64))
    game_type_id = db.Column(
            db.Integer,
            db.ForeignKey('game_type.id'),
            nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def to_dict(self):
        return dict(id=self.id,
                    name_kz=self.name_kz,
                    name_ru=self.name_ru,
                    name_en=self.name_en,
                    game_type_id=self.game_type_id,
                    user_id=self.user_id,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    updated_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    enabled=self.enabled)


    def __repr__(self):
        return "<Game '{}'>".format(self.name_en)
