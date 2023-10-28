"""Конетроллер для приема запросов."""

from fastapi import APIRouter, Depends
from app.api.v1.shemas import GetCurrentUserShema
from app.api.v1.dependencies import get_current_user

controller = APIRouter()

@controller.post('/me')
async def me(user=Depends(get_current_user)):
    return user