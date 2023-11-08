import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.template.defaultfilters import random
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken

from apps.user.managers import CustomUserManager
from shared.abstract_class.audited_abstract import AuditedAbstract


class User(AbstractUser, AuditedAbstract):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    email = models.EmailField(_("email address"), unique=True)
    reset_token = models.CharField(max_length=32, null=True, blank=True)
    reset_token_expiry = models.DateTimeField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        db_table = "users"
        ordering = ["-updated_at"]

    def __str__(self):
        return f'{self.email} {self.id}'

    def get_tokens_for_user(self):
        refresh = RefreshToken.for_user(self)
        refresh.payload['email'] = self.email

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    @staticmethod
    def generate_forgot_password_token() -> int:
        return random(6)
