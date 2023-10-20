"""Сервис логина."""

from app.config import AUTH_ADAPTER_URL
from app.api.v1.adapters.user.emitted import LoginAdapter
from app.api.v1.shemas import LoginShema


class LoginService:
    """Класс сервиса логина."""

    def __init__(self):
        """Функция инициализации."""
        self.adapter_url: str = AUTH_ADAPTER_URL
        self.data: LoginShema | None = None

    def set_data(self, data: LoginShema):
        """Функция для записи данных."""
        self.data = data

    async def call_adapter(self):
        """Функция для вызова адаптера."""
        self.response = await LoginAdapter(
            self.data,
            self.adapter_url + 'api/v1/adapter/auth/login'
        )
        return self.response

    async def proccess_response(self, authentication):
        """Функция для обработки ответа."""
        if self.response[1] == 200:
            user_id = self.response[0]['user_id']
            return {'token': authentication.login(user_id)}
        else:
            return self.response[0]
