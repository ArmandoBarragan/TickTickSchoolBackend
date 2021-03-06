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
        data_with_user = {'student': Token.objects.get(key=token).user}
        data_with_user.update(validated_data)
        return Subject.objects.create(**data_with_user)

    def update(self, instance, validated_data, *args, **kwargs):
        updated_object = Subject.objects.filter(pk=instance.pk).update(**validated_data)
        return Subject.objects.get(pk=updated_object)
