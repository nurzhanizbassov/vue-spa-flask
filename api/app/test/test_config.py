import os
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['SECRET_KEY'] is 'TossACoinToYourWitcher')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)

        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == (
                'postgresql://someapp:someapp@someapp-db:5432/someapp'
            )
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config['SECRET_KEY'] is 'TossACoinToYourWitcher')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == (
                'postgresql://someapp:someapp@someapp-test-db:5432/someapp'
            )
        )


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('app.main.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()
