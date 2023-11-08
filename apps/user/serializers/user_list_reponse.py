from rest_framework.serializers import ModelSerializer

from apps.user.models import User


class UserListResponse(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']
