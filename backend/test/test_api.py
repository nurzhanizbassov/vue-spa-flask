"""
test_api.py

Contains simple unit test of the api endpoints.

"""
import unittest
import requests
import json


class TestSomewebappApi(unittest.TestCase):
    def test_home_page(self):
        response = requests.get('http://localhost:5000/api').json()
        expected_response = {
            "msg": "Some Web App Backend"
        }
        self.assertEqual(response, expected_response)

    def test_login(self):
        data = {
           'email': 'su0@somewebapp.kz',
           'password': '123456'
        }
        payload = json.loads(json.dumps(data))
        headers = {'content-type': 'application/json'}
        response = requests.post(
           'http://localhost:5000/api/login/',
           json=payload,
           headers=headers
        )
        print('response:', response)


if __name__ == '__main__':
    unittest.main()
