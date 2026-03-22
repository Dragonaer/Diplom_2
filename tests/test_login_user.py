import allure
import pytest

from api_methods.login_user import UserLoginMethods
from data import TEST_USER
from helpers import *

class TestLoginUser:
    @allure.title("Авторизация существующего пользователя")
    @allure.description("Проверка авторизации существующего пользователя")
    def test_login_user_valid(self):
        with allure.step("Отправляем запрос на авторизацию пользователя с заполнением всех полей"):
            response = UserLoginMethods.login_user(TEST_USER.email, TEST_USER.password)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        assert response.json()["success"] == True

    @allure.title("Авторизация пользователя с неверным email")
    @allure.description("Проверка авторизации пользователя с неверным email")
    def test_login_user_incorrect_email(self):
        temp_user = create_test_user()
        with allure.step("Отправляем запрос на авторизацию пользователя с неверным email"):
            response = UserLoginMethods.create_user(temp_user.email, TEST_USER.password, TEST_USER.name)
        assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"
        assert response.json()["message"] == "email or password are incorrect"

    @allure.title("Авторизация пользователя с неверным паролем")
    @allure.description("Проверка авторизации пользователя с неверным паролем")
    def test_login_user_incorrect_password(self):
        temp_user = create_test_user()
        with allure.step("Отправляем запрос на авторизацию пользователя с неверным паролем"):
            response = UserLoginMethods.create_user(TEST_USER.email, temp_user.password, TEST_USER.name)
        assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"
        assert response.json()["message"] == "email or password are incorrect"    

    
