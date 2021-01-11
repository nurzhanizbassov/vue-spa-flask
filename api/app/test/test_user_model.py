import unittest

import datetime

from app.main import db
from app.main.model.user import User
from app.main.model.role import Role
from app.test.base import BaseTestCase


class TestUserModel(BaseTestCase):

    def add_user(self):
        role = Role('Standard', 'Стандартный', 'Стандартный')
        db.session.add(role)
        db.session.commit()

        user = User(
            email='test@test.kz',
            username='test',
            phone_number='123456789',
            role_id='1',
            password='123456',
            enabled=True
        )

        db.session.add(user)
        db.session.commit()
        return user


    def test_encode_auth_token(self):

        user = self.add_user()

        auth_token = User.encode_auth_token(user.id, user.email, user.role)
        self.assertTrue(isinstance(auth_token, bytes))


    def test_decode_auth_token(self):
        user = self.add_user()

        auth_token = User.encode_auth_token(user.id, user.email, user.role)
        self.assertTrue(isinstance(auth_token, bytes))
        self.assertTrue(User.decode_auth_token(auth_token.decode("utf-8")) == 1)


if __name__ == '__main__':
    unittest.main()
