import django.contrib.auth.password_validation as validators
from django.core import exceptions
from rest_framework import serializers

from apps.users.models import User


class PasswordValidationMixin:

    def validate(self, data):
        user = self.instance if self.instance else User(**data)
        # password = self.password if self.password else data.get('password')
        password = data.get('new_password', data.get('password'))
        errors = dict()
        try:
            validators.validate_password(password=password, user=user)
        except exceptions.ValidationError as e:
            errors['password'] = list(e.messages)

        if errors:
            raise serializers.ValidationError(errors)

        return super().validate(data)
