import json
from rest_framework.response import Response

# DRF imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.authtoken.models import Token

# Project imports
from .models import User
from .serializers import UserSerializer, UserCreationSerializer, UserLoginSerializer


# User views
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    # User's possible permissions
    def get_permissions(self):
        """Assign permissions based on action."""
        if self.action in ['signup', 'login']:
            permissions = [AllowAny]
        elif self.action in ['update', 'partial_update', 'profile', 'retrieve']:
            permissions = [IsAuthenticated]  # TODO check usefulness of IsAccountOwner for this use case
        else:
            permissions = [IsAdminUser]  # This permission is not used yet. We will see in the future
        return [p() for p in permissions]

    # Login method
    @action(detail=False, methods=['POST'])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            import pdb; pdb.set_trace()
            email = serializer.validated_data['email']
            user = User.objects.get(email=email)
            token = Token.objects.get_or_create(user=user)[0].key

            data = {'token': token}
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    # Sign up method
    @action(detail=False, methods=['POST'])
    def signup(self, request):
        serializer = UserCreationSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user, token = serializer.create(serializer.validated_data)
        data = ({
            'user': UserSerializer(user).data,
            'token': token
        })
        return Response(data, status=status.HTTP_201_CREATED)


