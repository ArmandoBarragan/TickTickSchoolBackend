# Django imports
from django.urls import reverse

# DRF imports
from rest_framework.test import APITestCase
from rest_framework import status

# Project imports
from tick_tick_school.users.views import UserViewSet
from tick_tick_school.tasks.views import TaskViewSet
from tick_tick_school.subjects.views import SubjectViewSet


class APITests(APITestCase):
    def test_create_account(self):
        url = 'users/signup/'
        self.assertEqual(url, reverse('users:signup'))
        data = {
            'email': 'abp@gmail.com',
            'password': 'super_pwd',
            'password_confirmation': 'super_pwd',
            'first_name': 'Armando',
            'last_name': 'Barragan'
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        url = 'api-token-auth'
        data = {
            'username': 'abp@gmail.com',
            'password': 'super_pwd'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_subject(self):
        url = 'subjects/'
        data = {
            'name': 'Conmut',
            'student': '1',
            'teacher': 'Angelica Fierro'
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        url = 'task/'
        data = {
            'name': 'Task1',
            'subject': 1,
            'student': 1,
            'description': 'Description1'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getting_account(self):
        login_data = {
            'username': 'abp@gmail.com',
            'password': 'super_pwd',
        }

        login_response = self.client.post('api-token-auth', login_data, format="json")
        token = login_response.body['token']

        url = 'users/1/'
        self.client.session.headers.update({'Authorization': 'Token {}'.format(token)})

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getting_subject(self):
        url = 'subjects/1/'
        self.client.get(url, format="json")
        self.assertEqual()

    def test_getting_task(self):
        url = 'task/1/'
        self.client.get(url, format="json")
        self.assertEqual()
