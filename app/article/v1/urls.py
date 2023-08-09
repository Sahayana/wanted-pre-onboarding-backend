from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app.article.v1.apis.article_api import ArticleViewSets

app_name = "article"

router = DefaultRouter()
router.register("moneybooks", ArticleViewSets, "articles")

urlpatterns = [
    path("", include(router.urls)),
]
