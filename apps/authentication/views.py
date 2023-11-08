from rest_framework.decorators import action
from rest_framework import status, viewsets
from rest_framework.response import Response

from apps.authentication.serializers.create_account_request import CreateAccountRequest
from apps.authentication.serializers.login_request import LoginRequest
from apps.authentication.serializers.login_response import LoginResponse
from apps.authentication.services.authentication_service import AuthenticationService


class AuthenticationAPI(viewsets.GenericViewSet):

    @action(detail=False, methods=['POST'], url_path='login')
    def login(self, request):
        serializer = LoginRequest(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        AuthenticationService.login(data=serializer.validated_data)

        user = AuthenticationService.login(data=serializer.validated_data)

        return Response(LoginResponse(user).data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'], url_path='create-account')
    def create_account(self, request):
        create_account_request = CreateAccountRequest(data=request.data)
        create_account_request.is_valid(raise_exception=True)

        user = AuthenticationService.create_account(create_account_request)

        return Response(LoginResponse(user).data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'], url_path='forget-password')
    def forget_password(self, request):
        data = {}
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'], url_path='reset-password')
    def reset_password(self, request):
        data = {}
        return Response(data, status=status.HTTP_200_OK)
