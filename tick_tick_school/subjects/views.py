# Drf imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

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
