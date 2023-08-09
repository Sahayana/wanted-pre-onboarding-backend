from typing import Callable

import pytest
from django.test import Client
from django.urls import reverse
from rest_framework import status

from app.account.models import User
from tests.account import factories as f

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
