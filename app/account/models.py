from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email: str, password: str):

        user = self.model(email=self.normalize_email(email=email))

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_supersuer(self, email: str, password: str, username: str):

        user = self.create_user(email=email, password=password, username=username)

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


class User(AbstractBaseUser, PermissionsMixin):

    # fields
    email = models.EmailField(max_length=150, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="Date joined")
    last_login = models.DateTimeField(auto_now=True, verbose_name="Last login")

    # boolean
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # email login
    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return self.email
