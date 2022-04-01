from rest_framework.serializers import ModelSerializer
from .models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'description', 'student', 'subject', 'status', 'pk']
        extra_kwargs = {
            'description': {'required': False},
            'status': {'required': False},
            'pk': {'readonly': True}
        }
