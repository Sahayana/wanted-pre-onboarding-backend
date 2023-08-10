import factory

from app.article.models import Ariticle
from tests.account.factories import UserFactory
from tests.helpers import get_random_string


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ariticle

    user = factory.SubFactory(UserFactory)
    title = factory.LazyAttribute(lambda o: f"{get_random_string(10)}")
    content = factory.LazyAttribute(lambda o: f"{get_random_string(10)}")
