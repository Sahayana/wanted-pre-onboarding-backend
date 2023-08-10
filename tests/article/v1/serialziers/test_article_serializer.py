import pytest

from app.article.v1.serializers.article_serializer import (
    ArticleCreateSerializer,
    ArticleReadSerializer,
    ArticleUpdateSerializer,
)
from tests.account.factories import UserFactory
from tests.article.factories import ArticleFactory

pytestmark = pytest.mark.django_db


def test_게시글_생성_시리얼라이저():

    user = UserFactory.create()
    article = ArticleFactory.build(user=user)

    data = {"title": article.title, "content": article.content}

    serailizer = ArticleCreateSerializer(data=data)

    assert serailizer.is_valid() is True
    assert serailizer.data["title"] == article.title
    assert serailizer.data["content"] == article.content


def test_게시글_조회_시리얼라이저():

    user = UserFactory.create()
    article = ArticleFactory.create(user=user)

    serializer = ArticleReadSerializer(instance=article)
    data = serializer.data

    assert data["id"] == article.id
    assert data["title"] == article.title
    assert data["content"] == article.content
    assert data["user"] == article.user.id


def test_게시글_수정_시리얼라이저():

    user = UserFactory.create()
    article = ArticleFactory.create(user=user)

    data = {"content": "modified"}

    serializer = ArticleUpdateSerializer(instance=article, data=data, partial=True)

    assert serializer.is_valid() is True
    modifed_article = serializer.save()
    assert modifed_article.content == data["content"]
