"""Файл для проверки уникальности данных."""

from app.api.v1.models import User


async def check_unique_email(email: str):
    """Функция для проверки уникальности эмэйла."""
    if await User.exists(email=email):
        return False
    return True


async def check_unique_username(username: str):
    """Функция для проверки уникальности юзернэйма."""
    if await User.exists(username=username):
        return False
    return True
