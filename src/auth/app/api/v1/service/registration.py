"""Сервис регистрации."""

from app.config import AUTH_ADAPTER_URL
from app.api.v1.adapters.user.emitted import RegistrationAdapter
from app.api.v1.shemas import RegistrationShema


class RegistrationService:
    """Класс сервиса регистрации."""

    def __init__(self):
        """Функция инициализации."""
        self.adapter_url: str = AUTH_ADAPTER_URL
        self.data: RegistrationShema | None = None

    def set_data(self, data: RegistrationShema):
        """Функция для записи данных."""
        self.data = data

    async def call_adapter(self):
        """Функция для вызова адаптера."""
        self.response = await RegistrationAdapter(
            self.data,
            self.adapter_url + 'api/v1/adapter/auth/registration'
        )
        return self.response
