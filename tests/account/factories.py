import random
import string

import factory
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from app.account.models import User


def get_random_string(length: int):

    letters = string.digits + string.ascii_lowercase
    random_str = "".join(random.choice(letters) for _ in range(length))
    return random_str


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.LazyAttribute(lambda o: f"{get_random_string(7)}@example.com")

    @factory.post_generation
    def password(self, create, extracted, **kwargs):
        if extracted:
            self.set_password(extracted)
        else:
            self.set_password("sahayana!")
