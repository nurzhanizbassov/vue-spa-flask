from flask import request
from flask_restx import Resource

from app.main.util.decorator import admin_token_required
from ..util.dto import RoleDto
from ..service.role_service import (
        get_all_roles,
        get_role
    )

api = RoleDto.api
_role = RoleDto.role


@api.route('/')
class RoleList(Resource):
    @api.doc('list_of_roles')
    @api.marshal_list_with(_role, envelope='data')
    def get(self):
        """List all roles"""
        return get_all_roles()


@api.route('/<id>')
@api.param('id', 'The Role identifier')
@api.response(404, 'Role not found.')
class Role(Resource):
    @api.doc('get a role')
    @admin_token_required
    @api.marshal_with(_role)
    def get(self, id):
        """get a role given its identifier"""
        role = get_role(id)
        if not role:
            api.abort(404)
        else:
            return role
