from django.urls import include, path

app_name = "article"

urlpatterns = [
    path("v1/", include("app.article.v1.urls", namespace="v1")),
]
