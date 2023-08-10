from django.contrib.auth import authenticate
from rest_framework import permissions, status, views
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from app.account.helpers import email_validater, password_validater
from app.account.models import User
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


class LoginView(TokenObtainPairView):

    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):

        email = request.data["email"]
        password = request.data["password"]

        if not email_validater(email=email):
            return Response(
                data={"error": "잘못된 이메일 양식입니다."}, status=status.HTTP_400_BAD_REQUEST
            )
        if not password_validater(password=password):
            return Response(
                data={"error": "비밀번호는 8자 이상입니다."}, status=status.HTTP_400_BAD_REQUEST
            )

        return super().post(request, *args, **kwargs)
