login = 'play.allelleo@gmail.com'
password = 'oeyu ufox egkd qfwi'

subject = "Confirmation Code"
text = "1234"


import aiosmtplib
import asyncio 
import email

async def main():
    try:
        smtp_client = aiosmtplib.SMTP(
            hostname="smtp.gmail.com",
            port=587,
            start_tls=True,
            use_tls=False,
        )
        await smtp_client.connect()

        await smtp_client.login(login, password)
        await smtp_client.sendmail(login, 'dev.allelleo@internet.ru', f'Subject:{subject}\n{text}')
        print("[ SMTP ] : OK")
        smtp_client.close()
        return 0
    except:
        print("[ SMTP ] : NO")
        smtp_client.close()
        return 0

def test():
    asyncio.run(main())