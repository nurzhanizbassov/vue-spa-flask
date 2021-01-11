"""
manage.py

Contains command for db migrations and
populating data.

"""
import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db
from app.main.model import(
    user, blacklist, role, game,
    game_type)
from app.main.model.user import User
from app.main.model.role import Role
from app.main.model.game import Game
from app.main.model.game_type import GameType


# from someapp_api.application import create_app
# from someapp_api.models import (
#         db, Role, User, Game, GameType
#         )

# app = create_app('dev')
app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)


# Migration utility command
manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run(host='0.0.0.0')

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def insert_data():

    # Roles
    role_0 = Role('Admin', 'Админ', 'Админ')
    role_1 = Role('Standard', 'Стандартный', 'Стандартный')
    roles = [role_0, role_1]
    db.session.bulk_save_objects(roles)
    db.session.commit()

    # Users
    admin = User('admin@someapp.kz',
                 'admin',
                 '+77070000001',
                 1,
                 '123456',
                 True)
    su0 = User('su0@someapp.kz', 'su0', '+77070000002', 2, '123456', True)
    su1 = User('su1@someapp.kz', 'su1', '+77070000003', 2, '123456', True)
    users = [admin, su0, su1]
    db.session.bulk_save_objects(users)
    db.session.commit()

    # Game types
    game_type_0 = GameType(
            'Стратегия в реальном времени',
            'Стратегия в реальном времени',
            'Real Time Strategy')
    game_type_1 = GameType(
            'Шутер от первого лица',
            'Шутер от первого лица',
            'First Person Shooter')
    game_type_2 = GameType(
            'Ролевая Игра',
            'Ролевая Игра',
            'Role-Playing Game')

    game_types = [game_type_0, game_type_1, game_type_2]
    db.session.bulk_save_objects(game_types)
    db.session.commit()

    # Games
    game_0 = Game('Doom 2016', 'Doom 2016', 'Doom 2016', 1, 2)
    game_1 = Game('Метро: Исход', 'Metro: Исход', 'Metro: Exodus', 1, 2)
    game_2 = Game(
            'Эпоха Империй 2: Definitive Edition',
            'Эпоха Империй 2: Definitive Edition',
            'AOE 2: Definitive Edition',
            2, 2)
    game_3 = Game('Doom Eternal', 'Doom Eternal', 'Doom Eternal', 1, 3)
    game_4 = Game('Diablo 3', 'Diablo 3', 'Diablo 3', 3, 3)
    game_5 = Game('Warcraft', 'Warcraft', 'Warcraft', 1, 3)

    games = [game_0, game_1, game_2, game_3, game_4, game_5]
    db.session.bulk_save_objects(games)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
