import os

from .base import *

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ["MYSQL_DATABASE"],
        "USER": "root",
        "PASSWORD": os.environ["MYSQL_ROOT_PASSWORD"],
        "PORT": "33306",
        "HOST": "localhost",
    }
}
