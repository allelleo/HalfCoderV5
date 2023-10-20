"""Сервис для регистрации пользователя."""

from app.api.v1.models import (
    User, Profile, Politic, Rating,
    RatingPerWeek, RatingPerMonth
)
from app.api.v1.adapters.auth.shemas import RegistrationShema
from app.api.v1.adapters.auth.exceptions import (
    EmailUniqueHTTPException,
    UsernameUniqueHTTPException,
    DataBaseHTTPException
)
from app.api.v1.service.checker import (
    check_unique_email, check_unique_username
)
from tortoise.transactions import in_transaction


async def RegistrationService(data: RegistrationShema):
    """Функция для регистрации пользователя."""
    if not await check_unique_email(data.email):
        raise EmailUniqueHTTPException
    if not await check_unique_username(data.username):
        raise UsernameUniqueHTTPException
    try:
        async with in_transaction() as transaction:
            profile = Profile()
            await profile.save(using_db=transaction)
            politic = Politic()
            await politic.save(using_db=transaction)
            rating = Rating()
            await rating.save(using_db=transaction)
            rating_per_week = RatingPerWeek()
            await rating_per_week.save(using_db=transaction)
            rating_per_month = RatingPerMonth()
            await rating_per_month.save(using_db=transaction)

            user = User(
                email=data.email,
                username=data.username,
                first_name=data.first_name,
                last_name=data.last_name,
                profile=profile,
                politic=politic,
                rating=rating,
                ratingWeek=rating_per_week,
                ratingMonth=rating_per_month
            )
            await user.set_password(data.password)
            await user.save(using_db=transaction)

            return {
                'status': 201,
                'message': {
                    'ru': 'Регистрация прошла успешно',
                    'en': 'Registration was successful'
                }
            }

    except Exception as e:
        print(str(e))
        raise DataBaseHTTPException
