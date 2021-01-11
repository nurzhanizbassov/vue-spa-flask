from flask_restx import Api
from flask import Blueprint
from flask_cors import CORS

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.role_controller import api as role_ns
from .main.controller.game_controller import api as game_ns
from .main.controller.game_type_controller import api as game_type_ns

blueprint = Blueprint('api', __name__)
CORS(blueprint)

api = Api(blueprint,
          title='someapp backend api',
          version='1.0',
          description='someapp project'
          )

api.add_namespace(auth_ns)
api.add_namespace(user_ns, path='/user')
api.add_namespace(role_ns, path='/role')
api.add_namespace(game_ns, path='/game')
api.add_namespace(game_type_ns, path='/game-type')
