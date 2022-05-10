# DRF Token
from rest_framework.serializers import ModelSerializer
from rest_framework.authtoken.models import Token

# Project imports
from .models import Subject


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name', 'teacher', 'classroom', 'id']
        extra_kwargs = {
            'id': {'read_only': True}
        }

    def save(self, validated_data, token):
        validated_data.append('student', Token.objects.get(key=token).user)
        return Subject.objects.create(**validated_data)
