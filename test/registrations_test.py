import unittest
import requests 



class T3(unittest.TestCase):
    def test_first(self):
        res = requests.post('http://127.0.0.1:8001/api/v1/auth/registration', json={
            'username': 'test',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@example.com',
            'password': 'test'
        })
        self.assertEqual(res.json(), {'status': 201, 'message': {'ru': 'Регистрация прошла успешно', 'en': 'Registration was successful'}}, "Регистрация пользлователя")

class T4(unittest.TestCase):
    def test_second(self):
        res = requests.post('http://127.0.0.1:8001/api/v1/auth/registration', json={
            'username': 'test1',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@example.com',
            'password': 'test'
        })
        self.assertEqual(res.json(), {'detail': {'message': {'en': 'Email is already registered','ru': 'Адрес электронной почты уже зарегистрирован'}}}, "Проверка почты на уникальность")

class T5(unittest.TestCase):
    def test_thrid(self):
        res = requests.post('http://127.0.0.1:8001/api/v1/auth/registration', json={
            'username': 'test',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@exam1ple.com',
            'password': 'test'
        })
        self.assertEqual(res.json(), {'detail': {'message': {'ru': 'Пользовательское имя уже зарегистрировано', 'en': 'Username is already registered'}}}, "Проверка юзернейма на уникальность")

if __name__ == "__main__":
    unittest.main()