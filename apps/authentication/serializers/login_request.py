from rest_framework import serializers


class LoginRequest(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
