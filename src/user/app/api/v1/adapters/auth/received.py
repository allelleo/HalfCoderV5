"""Файл для получения запросов."""

from fastapi import APIRouter
from app.api.v1.adapters.auth.service.registration import RegistrationService
from app.api.v1.adapters.auth.service.login import LoginService
from app.api.v1.adapters.auth.shemas import (
    LoginShema, RegistrationShema, AdapterAccess
)

adapter = APIRouter()


@adapter.post('/registration')
async def registration(data: RegistrationShema, access: AdapterAccess):
    """Регистрация пользователя."""
    return await RegistrationService(data)


@adapter.post('/login')
async def login(data: LoginShema, access: AdapterAccess):
    """Логин пользователя."""
    return await LoginService(data)

