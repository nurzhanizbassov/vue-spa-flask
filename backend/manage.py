"""
manage.py

Contains command for db migrations and
populating data.

"""

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from somewebapp_api.application import create_app
from somewebapp_api.models import (
        db, Role, User, Game, GameType
        )

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)

# Migration utility command
manager.add_command('db', MigrateCommand)

@manager.command
def insert_data():

    # Roles
    role_0 = Role('Admin', 'Админ', 'Админ')
    role_1 = Role('Standard', 'Стандартный', 'Стандартный')
    roles = [role_0, role_1]
    db.session.bulk_save_objects(roles)
    db.session.commit()

    # Users
    admin = User('admin@somewebapp.kz', 'admin', '+77070000001', 'admin',
                 1, True)
    su0 = User('su0@somewebapp.kz', 'su0', '+77070000002', '123456', 2, True)
    su1 = User('su1@somewebapp.kz', 'su1', '+77070000003', '123456', 2, True)
    users = [admin, su0, su1]
    db.session.bulk_save_objects(users)
    db.session.commit()

    # Game types
    game_type_0 = GameType(
            'Real Time Strategy',
            'Стратегия в реальном времени',
            'Стратегия в реальном времени')
    game_type_1 = GameType(
            'First Person Shooter',
            'Шутер от первого лица',
            'Шутер от первого лица')
    game_type_2 = GameType(
            'Role-Playing Game',
            'Ролевая Игра',
            'Ролевая Игра')

    game_types = [game_type_0, game_type_1, game_type_2]
    db.session.bulk_save_objects(game_types)
    db.session.commit()

    # Games
    game_0 = Game('Doom 2016', 'Doom 2016', 'Doom 2016', 1, 2)
    game_1 = Game('Metro: Exodus', 'Метро: Исход', 'Metro: Исход', 1, 2)
    game_2 = Game(
            'AOE 2: Definitive Edition',
            'Эпоха Империй 2: Definitive Edition',
            'Эпоха Империй 2: Definitive Edition',
            2, 2)
    game_3 = Game('Doom Eternal', 'Doom Eternal', 'Doom Eternal', 1, 3)
    game_4 = Game('Diablo 3', 'Diablo 3', 'Diablo 3', 3, 3)
    game_5 = Game('Warcraft', 'Warcraft', 'Warcraft', 1, 3)

    games = [game_0, game_1, game_2, game_3, game_4, game_5]
    db.session.bulk_save_objects(games)
    db.session.commit()


if __name__ == '__main__':
    manager.run()
