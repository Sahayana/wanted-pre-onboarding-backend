from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from app.account.helpers import email_validater, password_validater
from app.account.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)

    class Meta:

        model = User
        fields = ("email", "password")

    def validate(self, attrs):

        if User.objects.filter(email=attrs["email"]).exists():
            raise ValidationError("존재하는 이메일 입니다.")

        if not email_validater(email=attrs["email"]):
            raise ValidationError("잘못된 이메일 양식입니다.")
        elif not password_validater(password=attrs["password"]):
            raise ValidationError("비밀번호는 8자 이상입니다.")

        return attrs
