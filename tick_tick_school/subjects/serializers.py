from rest_framework.serializers import ModelSerializer
from .models import Subject


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ['name', 'teacher', 'student', 'classroom', 'pk']
        extra_kwargs = {
            'teacher': {'required': False},
            'classroom': {'required': False},
            'pk': {'readonly': True}
        }