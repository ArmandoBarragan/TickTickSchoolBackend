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

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Task.objects.filter(user=user.pk)

    @action(detail=False,
            methods=['GET'],
            url_path='subjects/tasks/<int:searched_subject>')
    def get_tasks_by_subject(self, request, searched_subject, *args, **kwargs):
        user = request.user
        searched_subject = searched_subject

        tasks = Task.objects.filter(user=user.pk, subject=searched_subject)
        serialized_tasks = TaskSerializer(tasks, many=True)

        return Response(serialized_tasks, status=status.HTTP_200_OK)
