import os

from .base import *

ALLOWED_HOSTS = ["*"]

DEBUG = bool(int(os.environ["DEBUG"]))

SECRET_KEY = os.environ["SECRET_KEY"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ["MYSQL_DB_DBINSTANCEIDENTIFIER"],
        "USER": os.environ["MYSQL_DB_USERNAME"],
        "PASSWORD": os.environ["MYSQL_DB_PASSWORD"],
        "PORT": os.environ["MYSQL_DB_PORT"],
        "HOST": os.environ["MYSQL_DB_HOST"],
    }
}
