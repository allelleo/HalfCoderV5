import requests 

def test_first():
    res = requests.post('http://127.0.0.1:8001/api/v1/auth/registration', json={
        'username': 'test',
        'first_name': 'test',
        'last_name': 'test',
        'email': 'test@example.com',
        'password': 'test'
    })
    if res.json() == {'status': 201, 'message': {'ru': 'Регистрация прошла успешно', 'en': 'Registration was successful'}}:
        print(f"[ Registration 1 ] : OK")
    else:
        print(f"[ Registration 1 ] : NO")

def test_second():
    res = requests.post('http://127.0.0.1:8001/api/v1/auth/registration', json={
        'username': 'test1',
        'first_name': 'test',
        'last_name': 'test',
        'email': 'test@example.com',
        'password': 'test'
    })
    print(res.json())
    if res.json() == {'detail': {'message': {'en': 'Email is already registered','ru': 'Адрес электронной почты уже зарегистрирован'}}}:
        print(f"[ Registration 2 ] : OK")
    else:
        print(f"[ Registration 2 ] : NO")

def test_thrid():
    res = requests.post('http://127.0.0.1:8001/api/v1/auth/registration', json={
        'username': 'test',
        'first_name': 'test',
        'last_name': 'test',
        'email': 'test@exam1ple.com',
        'password': 'test'
    })
    if res.json() == {'detail': {'message': {'ru': 'Пользовательское имя уже зарегистрировано', 'en': 'Username is already registered'}}}:
        print(f"[ Registration 3 ] : OK")
    else:
        print(f"[ Registration 3 ] : NO")

if __name__ == "__main__":
    test_first()
    test_second()
    test_thrid()