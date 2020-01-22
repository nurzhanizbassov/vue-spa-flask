"""
exceptions.py

Contains custom exceptions for the Flask backend.

"""

class InvalidUserRoleException(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors
