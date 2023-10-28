"""Файл с провайдерами."""

import jwt
from app.config import SECRET_KEY, ALGORITHM


class Authentication:
    """Класс для авторизации."""

    def __init__(self):
        """Функция инициализации."""
        self.SECRET_KEY: str = SECRET_KEY
        self.ALGORITHM: str = ALGORITHM

    def login(self, user_id: int) -> str:
        """Функция получения токена."""
        return jwt.encode({'user_id': user_id},
                          self.SECRET_KEY, algorithm=self.ALGORITHM)

    def decode(self, token: str) -> dict | ValueError:
        """Функция декодирования токена."""
        try:
            return jwt.decode(token, SECRET_KEY, algorithms=[self.ALGORITHM])
        except Exception as e:
            print(e)
            raise ValueError
