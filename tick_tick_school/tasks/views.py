# DRF imports
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# Project imports
from tick_tick_school.utils.permissions import OwnerPermission
from .serializers import TaskSerializer
from .models import Task


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer

    def get_permissions(self):
        if self.detail:
            permission_classes = [OwnerPermission]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        """ A user can only get the tasks they created. """
        user = self.request.user
        if user.is_authenticated:
            return Task.objects.filter(student=user.pk)

    @action(
        detail=False,
        methods=['GET'],
        url_path='subjects/tasks/<int:searched_subject>'
    )
    def get_tasks_by_subject(self, request, searched_subject, *args, **kwargs):
        """ Filter tasks by subject. """
        user = request.user
        searched_subject = searched_subject

        tasks = Task.objects.filter(user=user.pk, subject=searched_subject)
        serialized_tasks = TaskSerializer(tasks, many=True)

        return Response(serialized_tasks, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        token = request.headers['Authorization'].replace('Token ', '')
        if serializer.is_valid():
            created_object = serializer.save(serializer.validated_data, token)
            return Response(TaskSerializer(created_object).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = Task.objects.get(id=kwargs['pk'])
        instance_dict = instance.__dict__
        instance_dict.update(request.data)
        serializer = TaskSerializer(data=instance_dict)

        if serializer.is_valid():
            updated_object = serializer.update(
                instance=instance,
                validated_data=serializer.validated_data,
            )
            return Response(TaskSerializer(updated_object).data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
