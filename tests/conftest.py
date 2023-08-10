import pytest
from django.test import Client
from django.urls import reverse

from app.account.models import User
from tests.account.factories import UserFactory
from tests.helpers import get_access_token

pytestmark = pytest.mark.django_db


@pytest.fixture()
def create_user_data():
    def _create_user_data(user: User):

        data = {"email": user.email, "password": user.password}

        return data

    return _create_user_data


@pytest.fixture()
def get_token():
    def _get_token(client: Client):

        email = "test@test.com"
        password = "sahayanatest"
        user = UserFactory.create(email=email, password=password)

        data = {"email": email, "password": password}

        res = client.post(
            reverse("account:v1:login"), data=data, content_type="application/json"
        )

        return user, res.data["access"]

    return _get_token
