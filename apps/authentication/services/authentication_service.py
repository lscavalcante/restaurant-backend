from django.contrib import auth
from django.utils import timezone
from rest_framework.exceptions import AuthenticationFailed, APIException

from apps.authentication.serializers.create_account_request import CreateAccountRequest
from apps.user.models import User


class AuthenticationService:

    @classmethod
    def login(cls, data):
        try:
            email = data.get('email', None)
            password = data.get('password', None)

            user = auth.authenticate(email=email, password=password)

            if not user:
                raise AuthenticationFailed('Credencial inválida, tente novamente.')
            if not user.is_active:
                raise AuthenticationFailed('Conta desativada, entre em contato com o administrador.')
            # if not user.is_verified:
            #     raise AuthenticationFailed(
            #         'A conta ainda não foi verificada, já foi enviado um e-mail para confirmação, verifique '
            #         'sua caixa de entrada ou sua caixa de spam para ativar a conta.'
            #     )

            user.last_login = timezone.now()

            user.save()

            return user
        except APIException as error:
            raise error
        except Exception as fatal_error:
            raise APIException(detail=fatal_error)

    @classmethod
    def create_account(cls, create_account_request: CreateAccountRequest) -> User:

        email = create_account_request.validated_data.get('email')
        password = create_account_request.validated_data.get('password')

        user = User.objects.filter(email=email).first()

        if user:
            raise AuthenticationFailed('User already exists')

        new_user = User.objects.create(**create_account_request.validated_data)
        new_user.set_password(password)
        new_user.save()

        return new_user
