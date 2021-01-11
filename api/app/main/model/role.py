import json
from .. import db, flask_bcrypt
from .base_model import BaseModel


class Role(BaseModel):
    __tablename__ = 'role'

    def __init__(self,name_en, name_kz, name_ru):
        self.name_en = name_en
        self.name_kz = name_kz
        self.name_ru = name_ru

    name_en = db.Column(db.String(64))
    name_kz = db.Column(db.String(64), nullable=True)
    name_ru = db.Column(db.String(64), nullable=True)

    users = db.relationship('User', backref='role', lazy=True)

    def to_dict(self):
        return dict(id=self.id,
                    name_en=self.name_en,
                    name_kz=self.name_kz,
                    name_ru=self.name_ru,
                    created_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    updated_at=self.created_at.strftime('%Y-%m-%d %H:%M:%S'))


    def __repr__(self):
        return "<Role '{}'>".format(self.name_en)
