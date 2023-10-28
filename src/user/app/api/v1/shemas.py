"""Файл со схемами."""

from pydantic import BaseModel

class GetCurrentUserShema(BaseModel):
    "Схема данных для получения текущего пользователя."

    token: str
