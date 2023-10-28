"""Конетроллер для приема запросов."""

from fastapi import APIRouter
from .shemas import LoginShema, RegistrationShema
from .service.registration import RegistrationService
from .service.login import LoginService
from .providers import Authentication

auth = Authentication()
controller = APIRouter()




import aiosmtplib
import asyncio 
import email

async def main(email, code):
    try:
        login = 'play.allelleo@gmail.com'
        password = 'oeyu ufox egkd qfwi'

        subject = "Confirmation Code"
        smtp_client = aiosmtplib.SMTP(
            hostname="smtp.gmail.com",
            port=587,
            start_tls=True,
            use_tls=False,
        )
        await smtp_client.connect()

        await smtp_client.login(login, password)
        await smtp_client.sendmail(login, email, f'Subject:{subject}\n{code}')
        print("[ SMTP ] : OK")
        smtp_client.close()
        return 0
    except Exception as e:
        print("[ SMTP ] : NO")
        print(e)
        smtp_client.close()
        return 0

@controller.post('/login')
async def login(data: LoginShema):
    """Функция для логина."""
    service = LoginService()
    service.set_data(data)
    await service.call_adapter()
    jwt = await service.proccess_response(auth)
    return jwt

async def send_mail(uuid: str, email:str):
    print(f"Send mail to {email} via {uuid}")
    await main(email, uuid)

@controller.post('/registration')
async def registration(data: RegistrationShema):
    """Функция для регистрации."""
    service = RegistrationService()
    service.set_data(data)
    res = await service.call_adapter()
    if res[2] and res[3]:
        await send_mail(res[2], res[3])
    
    return res[0]
