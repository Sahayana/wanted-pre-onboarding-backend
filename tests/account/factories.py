import factory

from app.account.models import User
from tests.helpers import get_random_string


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
