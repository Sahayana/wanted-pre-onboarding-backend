import os

from enviorment import get_secret

from .base import *

get_secret(env="prod")

ALLOWED_HOSTS = ["*"]

DEBUG = os.environ["DEBUG"]

SECRET_KEY = os.environ["SECRET_KEY"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ["NAME"],
        "USER": os.environ["USERNAME"],
        "PASSWORD": os.environ["MYSQL_ROOT_PASSWORD"],
        "PORT": os.environ["PORT"],
        "HOST": os.environ["HOST"],
    }
}
