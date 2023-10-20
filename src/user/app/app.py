"""Файл приложения."""

from .api.v1.adapters.auth.received import adapter as auth_received_adapter
from .database import init
from .api.v1.controller import controller as user_v1_controller
from fastapi import FastAPI

app = FastAPI(title='HalfCoder User MicroService')


app.include_router(user_v1_controller, prefix='/api/v1/user', tags=['user'])

init(app)


app.include_router(
    auth_received_adapter,
    prefix='/api/v1/adapter/auth',
    tags=[
        'adapters',
        'auth'
    ]
)
