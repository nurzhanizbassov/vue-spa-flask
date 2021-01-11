from app.main.model.user import User
from ..service.blacklist_service import save_token
from app.main import db


class Auth:

    @staticmethod
    def login_user(data):
        try:
            # fetch the user data
            user = User.query.filter_by(email=data.get('email')).first()

            if not user.enabled:
                response_object = {
                    'status': 'fail',
                    'message': 'User not enabled.',
                }
                return response_object, 403

            result = user.check_password(data.get('password'));
            print('UAC. Auth. result:', result)
            if user and user.check_password(data.get('password')):
                auth_token = User.encode_auth_token(
                            user.id, user.email,
                            user.role
                        )

                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token.decode()
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500


    @staticmethod
    def logout_user(data):
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403


    @staticmethod
    def register_user(data):
        try:
            # fetch the user data
            user = User.query.filter_by(email=data.get('email')).first()
            if user:
                response_object = {
                    'status': 'fail',
                    'message': 'email already used.'
                }
                return response_object, 409

            user = User.query.filter_by(username=data.get('username')).first()
            if user:
                response_object = {
                    'status': 'fail',
                    'message': 'username already used.'
                }
                return response_object, 409

            user_to_register = User(
                    data.get('email'),
                    data.get('username'),
                    data.get('phoneNumber'),
                    data.get('roleId'),
                    data.get('password')
                )

            db.session.add(user_to_register)
            db.session.commit()

            response_object = {
                'status': 'success',
                'message': 'User successfully registered.'
            }
            return response_object, 200


        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500


    @staticmethod
    def get_logged_in_user(new_request):
        # get the auth token
        auth_token = new_request.headers.get('Authorization').split()[1]
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'user_id': user.id,
                        'email': user.email,
                        'role': user.role.name_en,
                        'created_on': str(user.created_on)
                    }
                }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401
