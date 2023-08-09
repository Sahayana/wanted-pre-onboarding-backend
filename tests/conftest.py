import pytest

from app.account.models import User

pytestmark = pytest.mark.django_db


@pytest.fixture()
def create_user_data():
    def _create_user_data(user: User):

        data = {"email": user.email, "password": user.password}

        return data

    return _create_user_data
