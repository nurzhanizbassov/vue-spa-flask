import uuid
import datetime

from app.main import db
from app.main.model.role import Role


def get_all_roles():
    return Role.query.all()


def get_role(id):
    return Role.query.filter_by(id=id).first()
