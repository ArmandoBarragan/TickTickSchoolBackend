# DRF imports
from rest_framework.test import APITestCase


class TestAPI(APITestCase):
    def test_endpoints(self):
        # User
        new_user = {
            'email': "user@gmail.com",
            'password': "super_pwd",
            'password_confirmation': "super_pwd",
            "first_name": "first",
            'last_name': 'user'
        }
        user_response = self.client.post(
            'http://testserver/users/',
            new_user
        )
        self.assertEqual(len(user_response.data), 1)
        token = user_response.data['user']

        # Login
        login_data = {
            'username': 'user@gmail.com',
            'password': 'super_pwd'
        }
        login_response = self.client.post(
            'http://testserver/api-token-auth/',
            json=login_data,
            headers={'Authorization: Token {}'.format(token)}
        )

        # Subject
        subject_data = {
            'student': 1,
            'name': 'Inteligencia Artificial',
            'teacher': 'Carlos Rubio',
        }
        subject_response = self.client.post(
            'http://testserver/subject/',
            json=subject_data,
            headers={'Authorization: Token {}'.format(token)}
        )

        # Task
        task_data = {
            'student': 1,
            'subject': 1,
            'name': 'Task 1',
            'description': 'Description 1'
        }
        task_response = self.client.post(
            'http://testserver/task/',
            json=task_data,
            headers={'Authorization: Token {}'.format(token)}
        )

        assert user_response == 200
        assert task_response.status_code == 200
        assert subject_response == 200
        assert login_response == 200
