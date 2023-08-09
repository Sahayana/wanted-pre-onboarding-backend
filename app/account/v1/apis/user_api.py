from django.contrib.auth import authenticate
from rest_framework import permissions, status, views
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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


class LoginView(views.APIView):

    permission_classes = [permissions.AllowAny]

    def obtain_token(self, user: User):

        token = TokenObtainPairSerializer.get_token(user=user)

        return str(token.access_token), str(token)

    def post(self, request):

        email = request.data["email"]
        password = request.data["password"]

        user = authenticate(email=email, password=password)

        if not user:
            return Response(
                data={"error": "Login failed"}, status=status.HTTP_400_BAD_REQUEST
            )

        access_token, refresh_token = self.obtain_token(user=user)

        return Response(
            data={"access token": access_token, "refresh token": refresh_token},
            status=status.HTTP_200_OK,
        )
