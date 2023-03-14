from typing import re

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

User = get_user_model()


class PasswordValidator:
    def __call__(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Пароль должен иметь не менее 8 символов")
        elif re.search('[0-9]', value) is None:
            raise serializers.ValidationError("Пароль должен содержать цифры")
        else:
            return value


class EmailValidator:
    def __call__(self, value):
        email = re.compile(r"[0-9A-Za-z]+@(mail|yandex)\.ru$")
        if not email.search(str(value)):
            raise serializers.ValidationError("Почта должна иметь домен mail или yandex")
        else:
            return value



class UserSerializer(ModelSerializer):
    birth_date = serializers.DateField(
        format='%d.%m.%Y',  # из базы дата будет вытаскиваться в формате "25.10.2021"
        input_formats=['%d.%m.%Y',
                       'iso-8601', ])
    password = serializers.CharField(validators=[PasswordValidator()])
    email = serializers.CharField(validators=[EmailValidator()])

    class Meta:
        model = User
        fields = '__all__'
