import os

from dotenv import load_dotenv

from .base import *

load_dotenv(".env.production")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wanted.settings.prod")

ALLOWED_HOSTS = ["*"]

DEBUG = bool(int(os.environ.get("DEBUG", 0)))


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ["MYSQL_DB_NAME"],
        "USER": os.environ["MYSQL_DB_USERNAME"],
        "PASSWORD": os.environ["MYSQL_DB_PASSWORD"],
        "PORT": os.environ["MYSQL_DB_PORT"],
        "HOST": os.environ["MYSQL_DB_HOST"],
    }
}
