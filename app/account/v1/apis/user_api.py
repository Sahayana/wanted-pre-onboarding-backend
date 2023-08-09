from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from app.account.v1.serializers.user_serializer import UserCreateSerializer


class UserCreateApiView(CreateAPIView):

    serializer_class = UserCreateSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        """
        회원가입

        parameters
            - email
            - password
        """

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            data=serializer.error_messages, status=status.HTTP_400_BAD_REQUEST
        )
