"""Файл зависимостей."""

from fastapi import Depends
from .providers import Authentication

from app.api.v1.models import User
from app.api.v1.shemas import GetCurrentUserShema

class AuthenticationDepends:
    def __init__(self):
        self.auth = Authentication()
    
    def get_user_id(self, token:GetCurrentUserShema):
        try:
            return self.auth.decode(token.token)['user_id']
        except ValueError as e:
            print(e)

auth = AuthenticationDepends()

async def get_current_user(user_id:int = Depends(auth.get_user_id)) -> User:
    user = await User.get_or_none(id=user_id)
    return user
