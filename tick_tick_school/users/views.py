# DRF imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Project imports
from .models import User
from .serializers import UserSerializer, UserCreationSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    action_permissions = {
        IsAuthenticated: ['retrieve', 'list']
        #  TODO Add the OwnerPermission here when it's ready
    }

    def create(self, request, *args, **kwargs):
        serialized_user = request.POST['user']
        user_data = UserCreationSerializer(serialized_user)

        import pdb; pdb.set_trace()
