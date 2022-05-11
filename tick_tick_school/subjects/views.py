import json
# Drf imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# Project imports
from .models import Subject
from .serializers import SubjectSerializer


class SubjectViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = SubjectSerializer

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
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
        token = request.headers['Authorization'].replace('Token ', '')
        instance = Subject.objects.get(id=kwargs['pk'])
        serializer = SubjectSerializer(instance=instance)

        if serializer.is_valid():
            updated_object = serializer.update(
                instance=instance,
                validated_data=serializer.validated_data,
                token=token
            )
            return Response(SubjectSerializer(updated_object).data, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
