from django.db import models

from tick_tick_school.utils.base_model import Property


class Subject(Property):
    name = models.CharField(max_length=100)
    teacher = models.CharField(max_length=200, null=True, blank=True)
    student = models.ForeignKey('users.User', on_delete=models.CASCADE)
    classroom = models.CharField(max_length=50, null=True, blank=True)

    def get_owner(self):
        return self.student

    def __str__(self):
        return '{} of {}'.format(self.name, self.student)
