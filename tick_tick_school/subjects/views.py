# Drf imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

# Project imports
from tick_tick_school.utils.permissions import OwnerPermission
from .models import Subject
from .serializers import SubjectSerializer


class SubjectViewSet(ModelViewSet):
    permission_classes = [OwnerPermission]
    serializer_class = SubjectSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Subject.objects.filter(student=user)
