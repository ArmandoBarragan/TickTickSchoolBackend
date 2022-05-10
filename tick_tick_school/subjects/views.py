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

    def create(self, request):
        token = request.headers['Authorization'].remove('Token ')
        serializer = SubjectSerializer(data=request.data)

        if serializer.is_valid():
            created_object = serializer.save(serializer.validated_data, token)
            return Response(created_object, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)