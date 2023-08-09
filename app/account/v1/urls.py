from account.v1.apis.user_api import UserCreateApiView
from django.urls import include, path

app_name = "account"

urlpatterns = [path("/signup/", UserCreateApiView.as_view(), name="signup")]
