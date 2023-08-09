# account 관련 helper 함수


def email_validater(email: str) -> bool:
    return "@" in email


def password_validater(password: str) -> bool:
    return len(password) >= 8
