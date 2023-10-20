"""Отвечает за отправку запросов."""

import httpx


async def RegistrationAdapter(data, url: str):
    """Отправка запроса на регистрацию пользователя."""
    async with httpx.AsyncClient() as client:
        r = await client.post(url, json={
            'data': {
                'username': data.username,
                'first_name': data.first_name,
                'last_name': data.last_name,
                'email': data.email,
                'password': data.password
            },
            'access': {
                'token': 'string'
            }

        })

    return [r.json(), r.status_code]


async def LoginAdapter(data, url: str):
    """Отправка запроса на авторизацию пользователя."""
    async with httpx.AsyncClient() as client:
        r = await client.post(url, json={
            'data': {
                'username': data.username,
                'password': data.password
            },
            'access': {
                'token': 'string'
            }

        })
    return [r.json(), r.status_code]
