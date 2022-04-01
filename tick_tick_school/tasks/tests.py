# Test imports
from django.test import TestCase

# Model imports
from .models import Task
from tick_tick_school.subjects.models import Subject
from tick_tick_school.users.models import User


class TasksTestCase(TestCase):
    def setUp(self):
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
