"""Сервис для логина пользователя."""

from app.api.v1.models import (
    User
)
from app.api.v1.adapters.auth.shemas import LoginShema
from app.api.v1.service.checker import (
    check_unique_username
)

from app.api.v1.adapters.auth.exceptions import (
    WrongPasswordHTTPException,
    NotFoundByUsernameHTTPException
)


async def LoginService(data: LoginShema):
    """Функция для логина пользователя."""
    if await check_unique_username(data.username):
        raise NotFoundByUsernameHTTPException
    try:
        user = await User.get(username=data.username)
    except User.DoesNotExist:
        raise NotFoundByUsernameHTTPException
    if not await user.check_password(data.password):
        raise WrongPasswordHTTPException

    return {
        'user_id': user.id,
    }
