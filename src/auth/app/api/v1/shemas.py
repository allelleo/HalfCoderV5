"""Файл со схемами."""

from pydantic import BaseModel, EmailStr


class RegistrationShema(BaseModel):
    """Схема данных для регистрации."""

    username: str
    first_name: str
    last_name: str
    email: EmailStr
    password: str


class LoginShema(BaseModel):
    """Схема данных для логина."""

    username: str
    password: str


class AdapterAccess(BaseModel):
    """Схема данных для доступа к адаптеру."""

    token: str

class RegisterAdapterOutput(BaseModel):
    """Данные которые возвращает адаптер регситрации."""

    res: dict
    status_code: int
    uuid: str
    email: str
