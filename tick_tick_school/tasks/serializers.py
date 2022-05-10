# DRF imports
from rest_framework.serializers import ModelSerializer
from rest_framework.authtoken.models import Token

# Project imports
from .models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['name', 'description', 'subject', 'status', 'id']
        extra_kwargs = {
            'description': {'required': False},
            'status': {'required': False},
            'id': {'read_only': True}
        }

    def save(self, validated_data, token):
        data_with_user = {'student': Token.objects.get(key=token).user}
        data_with_user.update(validated_data)
        return Task.objects.create(**data_with_user)
