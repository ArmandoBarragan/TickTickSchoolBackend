# DRF imports
from rest_framework.test import APITestCase, RequestsClient


class TestAPI(APITestCase):
    def setUp(self):
        self.client = RequestsClient()

    def test_endpoints(self):
        # User
        new_user = {
            'email': "user@gmail.com",
            'password': "super_pwd",
            'password_confirmation': "super_pwd",
            "first_name": "first",
            'last_name': 'user'
        }
        user_response = self.client.post('http://localhost:8000/users/', data=new_user)

        # Login
        login_data = {
            'username': 'user@gmail.com',
            'password': 'super_pwd'
        }
        login_response = self.client.post('http://localhost:8000/api-token-auth/', data=login_data)

        # Subject
        subject_data = {
            'student': 1,
            'name': 'Inteligencia Artificial',
            'teacher': 'Carlos Rubio',
        }
        subject_response = self.client.post('http://localhost:8000/subject/', data=subject_data)

        # Task
        task_data = {
            'student': 1,
            'subject': 1,
            'name': 'Task 1',
            'description': 'Description 1'
        }
        task_response = self.client.post('http://localhost:8000/task/', data=task_data)

        assert task_response.status_code == 200
        assert subject_response == 200
        assert login_response == 200
        assert user_response == 200
