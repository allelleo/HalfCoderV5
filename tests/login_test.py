import requests

def test_first():
    res = requests.post('http://127.0.0.1:8001/api/v1/auth/login', json={
            'username': 'test',
            'password': 'test'
        })
    if type(res.json().get('token', 1)) == str:
        print(f"[ Login 1 ] : OK")
    else:
        print(res.json())
        print(f"[ Login 1 ] : NO")

def test_second():
    res = requests.post('http://127.0.0.1:8001/api/v1/auth/login', json={
        'username': 'sjdfbdksjfbdfsfdsf',
        'password': 'test'
    })
    if res.json() == {'detail': 
            {'message':{'ru': 'Пользователь с таким именем не найден', 'en': 'Not found user with this name'}}
        }:
        print(f"[ Login 2 ] : OK")
    else:
        print(res.json())

        print(f"[ Login 2 ] : NO")

def test_thrid():
    res = requests.post('http://127.0.0.1:8001/api/v1/auth/login', json={
        'username': 'test',
        'password': 'JKBFDSBFIUSDBOFUDSBFOUSDBFSDF'
    })
    if res.json() ==  {'detail': {'message': {'ru': 'Пароль не верный', 'en': 'Wrong password'}}}:
        print(f"[ Login 3 ] : OK")
    else:
        print(res.json())

        print(f"[ Login 3 ] : NO")

if __name__ == "__main__":
    test_first()
    test_second()
    test_thrid()
