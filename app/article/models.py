from django.db import models

from wanted.settings.base import AUTH_USER_MODEL

# Create your models here.


class Ariticle(models.Model):

    user = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_articles"
    )
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "게시글"
