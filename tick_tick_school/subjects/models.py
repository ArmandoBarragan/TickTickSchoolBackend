from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.CharField(max_length=200)
    student = models.ForeignKey('users.User', on_delete=models.CASCADE)
    classroom = models.CharField(max_length=50)
