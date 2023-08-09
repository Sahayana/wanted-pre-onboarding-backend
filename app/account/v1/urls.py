from django.urls import include, path

from app.account.v1.apis.user_api import UserCreateApiView

app_name = "account"

urlpatterns = [path("/signup/", UserCreateApiView.as_view(), name="signup")]
