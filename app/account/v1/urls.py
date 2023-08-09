from django.urls import include, path

from app.account.v1.apis.user_api import LoginView, UserCreateApiView

app_name = "account"

urlpatterns = [
    path("/signup/", UserCreateApiView.as_view(), name="signup"),
    path("/login/", LoginView.as_view(), name="login"),
]
