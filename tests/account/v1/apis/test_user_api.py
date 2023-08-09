from typing import Callable

import pytest
from django.test import Client
from django.urls import reverse
from rest_framework import status

from app.account.models import User
from tests.account import factories as f
from tests.helpers import get_access_token

pytestmark = pytest.mark.django_db


def test_유저생성(client: Client, create_user_data: Callable):

    user = f.UserFactory.build()

    data = create_user_data(user)

    res = client.post(
        reverse("account:v1:signup"), data=data, content_type="application/json"
    )

    assert res.status_code == status.HTTP_201_CREATED
    assert res.data["email"] == user.email
    assert User.objects.filter(email=user.email).exists() is True


def test_로그인_성공시_토큰반환(client: Client):
    email = "test@test.com"
    password = "password1234"

    f.UserFactory.create(email=email, password=password)

    data = {"email": email, "password": password}

    res = client.post(
        reverse("account:v1:login"), data=data, content_type="application/json"
    )

    assert res.status_code == status.HTTP_200_OK
    assert res.data["access_token"] is not None


def test_로그인_유저정보_없을시_에러메시지_반환(client: Client):

    email = "test@test.com"
    password = "password1234"

    f.UserFactory.create(email=email, password=password)

    unvalid_email = "unvalid@test.com"

    data = {"email": unvalid_email, "password": password}

    res = client.post(
        reverse("account:v1:login"), data=data, content_type="application/json"
    )

    assert res.status_code == status.HTTP_400_BAD_REQUEST
    assert res.data["error"] == "존재하지 않는 유저입니다."


def test_로그인_이메일_유효성검사_에러메시지_반환(client: Client):

    unvalid_email = "unvalidtest.com"
    password = "password1234"

    data = {"email": unvalid_email, "password": password}

    res = client.post(
        reverse("account:v1:login"), data=data, content_type="application/json"
    )

    assert res.status_code == status.HTTP_400_BAD_REQUEST
    assert res.data["error"] == "잘못된 이메일 양식입니다."


def test_로그인_비밀번호_유효성검사_에러메시지_반환(client: Client):

    email = "test@test.com"
    unvalid_password = "pas"

    data = {"email": email, "password": unvalid_password}

    res = client.post(
        reverse("account:v1:login"), data=data, content_type="application/json"
    )

    assert res.status_code == status.HTTP_400_BAD_REQUEST
    assert res.data["error"] == "비밀번호는 8자 이상입니다."
