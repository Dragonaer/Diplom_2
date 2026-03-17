import requests
import allure

from helpers import *
from url import *
from data import *

class UserLoginMethods:
    @staticmethod
    @allure.step("Авторизация пользователя.")
    def create_user(email, password, name):
        endpoint = 'api/auth/login'
        body = {
            "email": email,
            "password": password,
            "name": name,
        }
        return requests.post(f'{URL.main_site}{endpoint}', json=body)
      