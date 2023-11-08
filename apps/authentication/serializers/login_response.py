from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from apps.user.models import User


class LoginResponse(ModelSerializer):
    tokens = serializers.JSONField(source='get_tokens_for_user')

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'tokens']
