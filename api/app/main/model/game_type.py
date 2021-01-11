from .. import db, flask_bcrypt
from .base_model import BaseModel


class GameType(BaseModel):
    __tablename__ = 'game_type'

    def __init__(self, name_kz, name_ru, name_en):
        self.name_kz = name_kz
        self.name_ru = name_ru
        self.name_en = name_en

    name_kz = db.Column(db.String(64), nullable=True)
    name_ru = db.Column(db.String(64), nullable=True)
    name_en = db.Column(db.String(64))
    games = db.relationship('Game', backref='game_type', lazy=True)

    def to_dict(self):
        return dict(id=self.id,
                    name_kz=self.name_kz,
                    name_ru=self.name_ru,
                    name_en=self.name_en,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    updated_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    enabled=self.enabled)


    def __repr__(self):
        return "<GameType '{}'>".format(self.name_en)
