import unittest
import requests 



class T6(unittest.TestCase):
    def test_first(self):
        res = requests.post('http://127.0.0.1:8001/api/v1/auth/login', json={
            'username': 'test',
            'password': 'test'
        })
        self.assertEqual(type(res.json().get('token', 1)), str, "Логин пользлователя")

class T7(unittest.TestCase):
    def test_second(self):
        res = requests.post('http://127.0.0.1:8001/api/v1/auth/login', json={
            'username': 'sjdfbdksjfbdfsfdsf',
            'password': 'test'
        })
        self.assertEqual(res.json(), {'detail': {'message': {'ru': 'Пользователь с таким именем не найден', 'en': 'Not found user with this name'}}}, "Логин пользлователя с неверным именем")

class T8(unittest.TestCase):
    def test_thrid(self):
        res = requests.post('http://127.0.0.1:8001/api/v1/auth/login', json={
            'username': 'test',
            'password': 'JKBFDSBFIUSDBOFUDSBFOUSDBFSDF'
        })
        self.assertEqual(res.json(), {'detail': {'message': {'ru': 'Пароль не верный', 'en': 'Wrong password'}}}, "Логин пользлователя с неправильным паролем")

if __name__ == "__main__":
    unittest.main()