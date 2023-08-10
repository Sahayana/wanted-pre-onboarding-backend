from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from app.article.models import Ariticle
from app.article.pagination import ArticlePagination
from app.article.v1.serializers.article_serializer import (
    ArticleCreateSerializer,
    ArticleReadSerializer,
    ArticleUpdateSerializer,
)


class ArticleViewSets(viewsets.ModelViewSet):

    queryset = Ariticle.objects.all()
    pagination_class = ArticlePagination

    def get_permissions(self):
        if self.action in ["retrieve", "list"]:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action in ["retrieve", "list"]:
            serializer_class = ArticleReadSerializer
        elif self.action == "create":
            serializer_class = ArticleCreateSerializer
        elif self.action in ["update", "partial_update"]:
            serializer_class = ArticleUpdateSerializer

        return serializer_class

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"user": self.request.user})

        return context

    def retrieve(self, request, pk: int):
        """
        게시글 단건 조회합니다.
        """

        article = self.get_queryset.get(id=pk)
        serializer = self.get_serializer(article)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        """
        페이지네이션 적용된 게시글 목록을 조회합니다.

        조회당 게시글 10개 반환 (page_size=10)
        """

        articles = self.get_queryset()
        paginated_articles = self.paginate_queryset(articles)

        serializer = self.get_serializer(paginated_articles, many=True)

        return self.get_paginated_response(data=serializer.data)

    def create(self, request, *args, **kwargs):
        """
        새로운 게시글을 작성합니다.

        parameters
            - title
            - content
        """

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                data=ArticleReadSerializer(serializer.instance).data,
                status=status.HTTP_201_CREATED,
            )

    def update(self, request, *args, **kwargs):
        """
        게시글을 수정합니다.

        parameter
            -content
        """
        article = self.get_object()

        if request.user.id != article.user.id:
            return Response(
                data={"error": "작성자만 수정할 수 있습니다."}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(
            instance=article, data=request.data, partial=True
        )
        if serializer.is_vaild(raise_exception=True):
            serializer.save()
            return Response(
                ArticleReadSerializer(serializer.instance).data,
                status=status.HTTP_200_OK,
            )

    def destroy(self, request, *args, **kwargs):

        article = self.get_object()

        if article.user.id != request.user.id:
            return Response(
                data={"error": "작성자만 삭제할 수 있습니다."}, status=status.HTTP_400_BAD_REQUEST
            )

        self.perform_destroy(instance=article)
        return Response(
            data={"msg": "게시글이 삭제되었습니다."}, status=status.HTTP_204_NO_CONTENT
        )
