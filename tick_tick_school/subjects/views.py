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

    def retrieve(self, request, pk=None, *args, **kwargs):
        user = request.user

        if pk is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        subject = Subject.objects.get(pk=pk)
        if subject.student.pk != user.pk:  # A user can't read a subject they didn't create
            return Response(status=status.HTTP_403_FORBIDDEN)

        return Response(SubjectSerializer(), status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        user = request.user
        subjects = Subject.objects.filter(user=user.pk)
        serialized_subjects = SubjectSerializer(subjects, many=True)
        return Response(serialized_subjects, status=status.HTTP_200_OK)
