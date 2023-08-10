from typing import Callable

import pytest

from app.account.v1.serializers.user_serializer import UserCreateSerializer
from tests.account import factories as f

pytestmark = pytest.mark.django_db


def test_유저생성(create_user_data: Callable):

    signed_user = f.UserFactory.build()

    data = create_user_data(signed_user)

    serializer = UserCreateSerializer(data=data)

    assert serializer.is_valid() is True

    user = serializer.save()

    assert user is not None
    assert user.email == signed_user.email


def test_유저생성시_email_유효성검사():

    unvalid_email = "sahayana.com"
    password = "sahayana"

    data = {"email": unvalid_email, "password": password}

    serializer = UserCreateSerializer(data=data)

    assert serializer.is_valid() is False
    assert str(serializer.errors["non_field_errors"][0]) == "잘못된 이메일 양식입니다."


def test_유저생성시_password_유효성검사():

    email = "sahayana@wanted.com"
    password = "sah"

    data = {"email": email, "password": password}

    serializer = UserCreateSerializer(data=data)

    assert serializer.is_valid() is False
    assert str(serializer.errors["non_field_errors"][0]) == "비밀번호는 8자 이상입니다."
