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

    def validate(self, attrs):
        user = self.context.get("user")
        article = Ariticle.objects.filter(id=attrs["id"])

        if user.id != article.user.id:
            raise ValidationError("작성자만 수정할 수 있습니다.")

        return attrs


class ArticleReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ariticle
        fields = "__all__"
