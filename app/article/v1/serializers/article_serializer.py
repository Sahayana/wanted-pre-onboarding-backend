from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from app.article.models import Ariticle


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ariticle
        fields = ("title", "content")


class ArticleUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ariticle
        fields = ("content",)


class ArticleReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ariticle
        fields = "__all__"
