import os

from .base import *

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "wanted",
        "USER": "root",
        "PASSWORD": "wanted",
        "PORT": "3306",
        "HOST": "host.docker.internal",  # Docker mysql connection to Django on window operating.
    }
}
