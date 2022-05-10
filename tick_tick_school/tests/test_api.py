# DRF imports
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

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
            'http://testserver/users/signup/',
            new_user
        )

        self.assertEqual(user_response.status_code, 201, f'expected Response code 201, instead get {user_response.status_code}')

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + user_response.data['token'])

        # Subject
        subject_data = {
            'student': 1,
            'name': 'Inteligencia Artificial',
            'teacher': 'Carlos Rubio',
        }
        subject_response = self.client.post(
            'http://testserver/subjects/',
            json=subject_data,
        )

        self.assertEqual(subject_response.status_code, 201)

        # Task
        task_data = {
            'student': 1,
            'subject': 1,
            'name': 'Task 1',
            'description': 'Description 1'
        }
        task_response = self.client.post(
            'http://testserver/tasks/',
            json=task_data,
            headers={'Authorization: Token {}'.format(token)}
        )

        self.assertEqual(task_response.status_code, 201)
