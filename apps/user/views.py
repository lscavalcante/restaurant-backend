from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.user.models import User
from apps.user.serializers.user_list_reponse import UserListResponse


class UserAPI(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListResponse
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
