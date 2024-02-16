import json
from rest_framework.response import Response

# DRF imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import (
    IsAuthenticated,
    AllowAny,
)
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.authtoken.models import Token

# Project imports
from .models import User
from .serializers import (
    UserSerializer,
    UserCreationSerializer,
    UserLoginSerializer,
)


# User views
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['signup', 'login']:
            permissions = [AllowAny]
        else:
            permissions = [IsAuthenticated]  # TODO check usefulness of IsAccountOwner for this use case
        return [p() for p in permissions]

    @action(detail=False, methods=['POST'])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        email = serializer.validated_data['email']
        user = User.objects.get(email=email)
        token = Token.objects.get_or_create(user=user)[0].key
        data = {'token': token}
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def signup(self, request):
        serializer = UserCreationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user, token = serializer.create(serializer.validated_data)
        data = ({
            'user': UserSerializer(user).data,
            'token': token
        })
        return Response(data, status=status.HTTP_201_CREATED)
