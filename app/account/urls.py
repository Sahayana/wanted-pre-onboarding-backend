from django.urls import include, path

app_name = "account"

urlpatterns = [
    path("/v1", include("app.account.v1.urls", namespace="v1")),
]
