import json
# Drf imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# Project imports
from tick_tick_school.utils.permissions import OwnerPermission
from .models import Subject
from .serializers import SubjectSerializer


class SubjectViewSet(ModelViewSet):
    serializer_class = SubjectSerializer

    def get_permissions(self):
        if self.detail:
            permission_classes = [OwnerPermission]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        """ A user can only get the subjects they created. """
        user = self.request.user
        if user.is_authenticated:
            return Subject.objects.filter(student=user)

    def create(self, request, **kwargs):
        token = request.headers['Authorization'].replace('Token ', '')
        serializer = SubjectSerializer(data=request.data)

        if serializer.is_valid():
            created_object = serializer.save(serializer.validated_data, token)
            return Response(SubjectSerializer(created_object).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = Subject.objects.get(id=kwargs['pk'])
        instance_dict = instance.__dict__
        instance_dict.update(request.data)
        serializer = SubjectSerializer(data=instance_dict)

        if serializer.is_valid():
            updated_object = serializer.update(
                instance=instance,
                validated_data=serializer.validated_data,
            )
            return Response(SubjectSerializer(updated_object).data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
