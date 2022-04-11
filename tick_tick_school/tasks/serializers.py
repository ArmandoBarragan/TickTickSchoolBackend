from rest_framework.serializers import ModelSerializer
from .models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'description', 'student', 'subject', 'status', 'id']
        extra_kwargs = {
            'description': {'required': False},
            'status': {'required': False},
            'id': {'read_only': True}
        }