import os

from .base import *

# from wanted.enviorment import get_secret


# get_secret("prod")

ALLOWED_HOSTS = ["*"]

DEBUG = bool(int(os.environ.get("DEBUG", 0)))


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
