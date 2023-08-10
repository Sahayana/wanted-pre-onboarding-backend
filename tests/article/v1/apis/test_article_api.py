from typing import Callable

import pytest
from django.test import Client
from django.urls import reverse
from rest_framework import status

from app.article.models import Ariticle
from app.article.pagination import ArticlePagination
from tests.account.factories import UserFactory
from tests.article.factories import ArticleFactory
from tests.helpers import authorization_header

pytestmark = pytest.mark.django_db


def test_게시글_작성시_유효하지않은_토큰_인증_오류_반환(client: Client):

    token = "invalid_token"
    article = ArticleFactory.build()

    data = {"title": article.title, "content": article.content}

    res = client.post(
        reverse("article:v1:articles-list"),
        data=data,
        content_type="application/json",
        **authorization_header(token),
    )

    assert res.status_code == status.HTTP_401_UNAUTHORIZED


def test_게시글_작성_성공시_데이터_반환(client: Client, get_token: Callable):

    user, token = get_token(client)

    article = ArticleFactory.build(user=user)

    data = {"title": article.title, "content": article.content}

    res = client.post(
        reverse("article:v1:articles-list"),
        data=data,
        content_type="application/json",
        **authorization_header(token),
    )

    assert res.status_code == status.HTTP_201_CREATED
    assert res.data["content"] == article.content
    assert res.data["title"] == article.title
    assert res.data["user"] == user.id


def test_게시글_수정_성공시_데이터_반환(client: Client, get_token: Callable):

    user, token = get_token(client)

    new_content = "modified"

    article = ArticleFactory.create(user=user)

    data = {"content": new_content}

    res = client.put(
        path=f"/article/v1/articles/{article.id}/",
        data=data,
        content_type="application/json",
        **authorization_header(token),
    )

    assert res.status_code == status.HTTP_200_OK
    assert res.data["content"] == new_content
    assert res.data["title"] == article.title
    assert res.data["user"] == user.id


def test_작성자_아닌_유저가_글_수정시_에러_반환(client: Client, get_token: Callable):

    user, token = get_token(client)

    author = UserFactory.create()
    article = ArticleFactory.create(user=author)

    new_content = "modified"
    data = {"content": new_content}

    res = client.put(
        path=f"/article/v1/articles/{article.id}/",
        data=data,
        content_type="application/json",
        **authorization_header(token),
    )

    assert res.status_code == status.HTTP_400_BAD_REQUEST
    assert res.data["error"] == "작성자만 수정할 수 있습니다."


def test_게시글_단건_조회_데이터_반환(client: Client):

    user = UserFactory.create()
    article = ArticleFactory.create(user=user)

    res = client.get(path=f"/article/v1/articles/{article.id}/")

    assert res.status_code == status.HTTP_200_OK
    assert res.data["content"] == article.content
    assert res.data["title"] == article.title
    assert res.data["user"] == user.id


def test_게시글_리스트_조회_페이지네이션_데이터_반환(client: Client):

    user = UserFactory.create()
    size = 15
    articles = ArticleFactory.create_batch(size=size, user=user)

    res = client.get(reverse("article:v1:articles-list"))

    assert res.status_code == status.HTTP_200_OK
    assert res.data["count"] == size
    assert res.data["previous"] is None
    assert res.data["next"] is not None
    assert len(res.data["results"]) == ArticlePagination.page_size
    assert res.data["results"][0]["id"] == [article.id for article in articles][-1]


def test_게시글_삭제시_메시지_반환(client: Client, get_token: Callable):

    user, token = get_token(client)
    article = ArticleFactory.create(user=user)

    res = client.delete(
        path=f"/article/v1/articles/{article.id}/", **authorization_header(token)
    )

    assert res.status_code == status.HTTP_204_NO_CONTENT
    assert res.data["msg"] == "게시글이 삭제되었습니다."
    assert Ariticle.objects.filter(id=article.id).exists() is not True
