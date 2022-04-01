from django.db import models


class Task(models.Model):
    STATUS_LIST = [
        ('pe', 'pendiente'),
        ('pr', 'en proceso'),
        ('t', 'terminada')
    ]

    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, blank=False, null=False)
    student = models.ForeignKey('users.User', on_delete=models.CASCADE, null=False)
    subject = models.ForeignKey('subjects.Subject', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_LIST, default='pe', blank=True),

    def __str__(self):
        return '{} of {}'.format(self.name, self.student)
