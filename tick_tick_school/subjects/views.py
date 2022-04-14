# Drf imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

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
