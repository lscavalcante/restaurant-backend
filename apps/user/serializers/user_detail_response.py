from rest_framework.serializers import ModelSerializer

from apps.user.models import User


class UserDetailResponse(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
