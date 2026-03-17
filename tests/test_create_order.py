import allure
import pytest

from api_methods.create_order import CreteOrderMethods
from api_methods.login_user import UserLoginMethods

from data import *

class TestCreteOrder:
    @allure.title("Создание заказа с авторизацией")
    @allure.description("Проверка создания заказа с авторизацией")
    def test_create_order_with_auth(self):
        with allure.step("Отправляем запрос на авторизацию пользователя с заполнением всех полей"):
            response = UserLoginMethods.create_user(TEST_USER.email, TEST_USER.password, TEST_USER.name)
        with allure.step("Добавляем ингридиенты в заказ"):
            response = CreteOrderMethods.create_order('61c0c5a71d1f82001bdaaa6d')
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        assert response.json()["success"] == True

    @allure.title("Создание заказа без авторизации")
    @allure.description("Проверка создания заказа без авторизации")
    def test_create_order_without_auth(self):
        with allure.step("Добавляем ингридиенты в заказ"):
            response = CreteOrderMethods.create_order('61c0c5a71d1f82001bdaaa6d')
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        assert response.json()["success"] == True


    @allure.title("Создание заказа без ингридиента")
    @allure.description("Проверка создания без ингридиента")
    def test_create_order_without_ingredients(self):
        with allure.step("Добавляем ингридиенты в заказ"):
            response = CreteOrderMethods.create_order("")
        assert response.status_code == 400, f"Expected status code 400, but got {response.status_code}"
        assert response.json()["message"] == ORDER_NO_INGREDIENTS_MSG


    @allure.title("Создание заказа с неверным хешем ингридиента")
    @allure.description("Проверка создания с неверным хешем ингридиента")
    def test_create_order_invalid_hash_ingredients(self):
        with allure.step("Добавляем ингридиенты в заказ"):
            response = CreteOrderMethods.create_order("1234")
        assert response.status_code == 500, f"Expected status code 500, but got {response.status_code}"