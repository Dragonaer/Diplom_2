import requests
import allure

from helpers import *
from url import *
from data import *

class CreteOrderMethods:
    @staticmethod
    @allure.step("Создание заказа.")
    def create_order(ingredients):
        endpoint = 'api/orders'
        body = {
            "ingredients": ingredients
        }
        return requests.post(f'{URL.main_site}{endpoint}', json=body)
    
    