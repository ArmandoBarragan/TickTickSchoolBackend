# DRF imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# Project imports
from .serializers import TaskSerializer
from .models import Task


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    action_permissions = {
        IsAuthenticated: ['retrieve', 'list']
        #  TODO Add the OwnerPermission here when it's ready
    }

    def list(self, request, *args, **kwargs):
        user = request.user

        if user.is_superuser:
            tasks = TaskSerializer(Task.objects.all(), many=True)
            return Response(tasks, status=status.HTTP_200_OK)

        elif user.is_authenticated:
            tasks = Task.objects.filter(user=user.pk)
            serialized_tasks = TaskSerializer(tasks, many=True)
            return Response(serialized_tasks, status=status.HTTP_200_OK)

        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False,
            methods=['GET'],
            url_path='subjects/tasks/<int:searched_subject>')
    def get_tasks_by_class(self, request, searched_subject, *args, **kwargs):
        user = request.user
        searched_subject = searched_subject

        tasks = Task.objects.filter(user=user.pk, subject=searched_subject)
        serialized_tasks = TaskSerializer(tasks, many=True)

        return Response(serialized_tasks, status=status.HTTP_200_OK)
