import re

from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from datetime import date, timedelta

User = get_user_model()


class PasswordValidator:
    def __call__(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Пароль должен иметь не менее 8 символов")
        elif re.search('[0-9]', value) and re.search('[a-zA-z]', value) is None:
            raise serializers.ValidationError("Пароль должен содержать цифры и буквы")
        else:
            return value


class EmailValidator:
    def __call__(self, value):
        email = re.compile(r"[0-9A-Za-z]+@(mail|yandex)\.ru$")
        if not email.search(str(value)):
            raise serializers.ValidationError("Почта должна иметь домен mail или yandex")
        else:
            return value


class AgeValidator:
    def __call__(self, value):
        age = (date.today() - value) // timedelta(days=365.2425)
        if age < 18:
            raise serializers.ValidationError("Писать посты могут только пользователи, достигшие 18 лет")
        else:
            return value


class UserSerializer(ModelSerializer):
    password = serializers.CharField(validators=[PasswordValidator()])
    email = serializers.CharField(validators=[EmailValidator()])

    def create(self, validated_data):
        reader = super().create(validated_data)
        reader.set_password(reader.password)
        reader.save()
        return reader

    def update(self, instance, validated_data):
        reader = super().update(instance, validated_data)
        validated_data.pop('birth_date')
        reader.set_password(reader.password)
        reader.save()
        return reader

    class Meta:
        model = User
        fields = '__all__'
