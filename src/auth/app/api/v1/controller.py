"""Конетроллер для приема запросов."""

from fastapi import APIRouter
from .shemas import LoginShema, RegistrationShema
from .service.registration import RegistrationService
from .service.login import LoginService
from .providers import Authentication

auth = Authentication()
controller = APIRouter()


@controller.post('/login')
async def login(data: LoginShema):
    """Функция для логина."""
    service = LoginService()
    service.set_data(data)
    await service.call_adapter()
    jwt = await service.proccess_response(auth)
    return jwt


@controller.post('/registration')
async def registration(data: RegistrationShema):
    """Функция для регистрации."""
    service = RegistrationService()
    service.set_data(data)
    res = await service.call_adapter()
    return res[0]
