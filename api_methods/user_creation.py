import requests
import allure

from helpers import *
from url import *
from data import *


class UserMethods:
    @staticmethod
    @allure.step("Создание пользователя с заполнением всех полей.")
    def create_user(email, password, name):
        endpoint = 'api/auth/register'
        body = {
            "email": email,
            "password": password,
            "name": name,
        }
        return requests.post(f'{URL.main_site}{endpoint}', json=body)
        
    @staticmethod
    @allure.step("Создание пользователя без email.")
    def create_user_no_email(password, name):
        endpoint = 'api/auth/register'
        body = {
            "password": password,
            "name": name,
        }
        return requests.post(f'{URL.main_site}{endpoint}', json=body)
   
    
    @staticmethod
    @allure.step("Создание пользователя без пароля.")
    def create_user_no_password(email, name):
        endpoint = 'api/auth/register'
        body = {
            "email": email,
            "name": name,
        }
        return requests.post(f'{URL.main_site}{endpoint}', json=body)
    
    @staticmethod
    @allure.step("Создание пользователя без имени.")
    def create_user_no_name(email, password):
        endpoint = 'api/auth/register'
        body = {
            "email": email,
            "password": password,
        }
        return requests.post(f'{URL.main_site}{endpoint}', json=body)
    
       
    @staticmethod
    @allure.step("Удаление пользователя.")
    def delete_user(token):
        endpoint = 'api/auth/user'
        headers = {'Authorization': f'Bearer {token}'}
        return requests.delete(f'{URL.main_site}{endpoint}', headers=headers)