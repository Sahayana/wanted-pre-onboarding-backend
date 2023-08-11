import os

from .base import *

ALLOWED_HOSTS = ["*"]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "wanted",
        "USER": "root",
        "PASSWORD": "wanted",
        "PORT": "33306",
        "HOST": "host.docker.internal",
    }
}
