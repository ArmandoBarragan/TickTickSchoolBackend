# Test imports
from django.test import TestCase
from rest_framework.test import APIClient

# Model imports
from tick_tick_school.tasks.models import Task
from tick_tick_school.subjects.models import Subject
from tick_tick_school.users.models import User


class TasksTestCase(TestCase):
    def setUp(self):
        """ Create database instances of every table"""
        self.user = User.objects.create_user(
            email="abp@gmail.com",
            first_name="armando",
            last_name="barragan",
            password="super_password.123"
        )
        self.subject = Subject.objects.create(
            student=self.user,
            name="Inteligencia Artificial",
            teacher="Carlos Rubio",
            classroom="A2"
        )
        self.task = Task.objects.create(
            student=self.user,
            subject=self.subject,
            name="Tarea 1",
            status="pe",
            description="Descripcion de la tarea 1"
        )

    def test_models(self):
        """ Check if all registers were created correctly"""
        self.assertIsNotNone(self.user)
        self.assertIsNotNone(self.subject)
        self.assertIsNotNone(self.task)