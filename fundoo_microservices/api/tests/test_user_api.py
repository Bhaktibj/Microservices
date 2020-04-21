import requests
from ..settings import BASE_URL
import json


class TestUserApi:
    """ This class is used for testing the all apis"""

    def test_register(self):
        url = BASE_URL + '/register/user'
        data = {'first_name': 'Bhakti2', 'last_name': 'Jadhav2', 'email': 'Bhakti3@gmail.com',
                'password': 'Bhakti3@123', 'phone_number': '9008567887'}
        request_data = json.dumps(data)
        response = requests.post(url, request_data)
        print(response.text)
        return response.status_code == 200

    def test_activation(self):
        url = BASE_URL + '/activate/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ2YXIiOiJCaGFrdGkzQGdtYWlsLmNvbSJ9.HnneHCvz2d8CBBYs7fG2sICQPjQuNPihvMBwbyGhXis'
        response = requests.get(url)
        return response.status_code == 200

    def test_login(self):
        url = BASE_URL + '/login/user'
        data = {'email': 'Bhakti2@gmail.com', 'password': 'Bhakti2@123'}
        requests_data = json.dumps(data)
        response = requests.post(url, requests_data)
        return response.status_code == 200

    def test_forgot_password(self):
        url = BASE_URL + '/forgot/password'
        data = {'email': 'Bhakti2@gmail.com'}
        requests_data = json.dumps(data)
        response = requests.post(url, requests_data)
        return response.status_code == 200

    def test_reset_password(self):
        url = BASE_URL + '/reset/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ2YXIiOiJCaGFrdGkyQGdtYWlsLmNvbSJ9.2I6CdN-0fTE0wYabUwMztWQDyhel-PK98Cm_y5wLv5E'
        data = {'new_password': 'Admin@123'}
        requests_data = json.dumps(data)
        response = requests.post(url, requests_data)
        return response.status_code == 200


