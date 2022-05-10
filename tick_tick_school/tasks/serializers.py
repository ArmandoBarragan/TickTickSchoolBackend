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

    def create(self, validated_data, token):
        user = Token.objects.get(key=token).user
        import pdb; pdb.set_trace()
        validated_data.append('student', user)
        return Task.objects.create()