import random
import string

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from app.account.models import User


def get_access_token(user: User) -> str:
    """
    Factory로 생성한 더미유저의 access token 생성 및 반환
    """

    token = TokenObtainPairSerializer.get_token(user=user)

    return str(token.access_token)


def authorization_header(token):
    """
    header 인증
    """
    return {"HTTP_AUTHORIZATION": f"Bearer {token}"}


def get_random_string(length: int):

    letters = string.digits + string.ascii_lowercase
    random_str = "".join(random.choice(letters) for _ in range(length))
    return random_str
