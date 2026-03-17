import allure
import pytest

from api_methods.login_user import UserLoginMethods
from data import TEST_USER

class TestLoginUser:
    @allure.title("Авторизация существующего пользователя")
    @allure.description("Проверка авторизации существующего пользователя")
    def test_login_user_valid(self):
        with allure.step("Отправляем запрос на авторизацию пользователя с заполнением всех полей"):
            response = UserLoginMethods.create_user(TEST_USER.email, TEST_USER.password, TEST_USER.name)
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        assert response.json()["success"] == True

    @allure.title("Авторизация пользователя с неверным email")
    @allure.description("Проверка авторизации пользователя с неверным email")
    def test_login_user_incorrect_email(self, user):
        with allure.step("Отправляем запрос на авторизацию пользователя с неверным email"):
            response = UserLoginMethods.create_user(user.email, TEST_USER.password, TEST_USER.name)
        assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"
        assert response.json()["message"] == "email or password are incorrect"

    @allure.title("Авторизация пользователя с неверным паролем")
    @allure.description("Проверка авторизации пользователя с неверным паролем")
    def test_login_user_incorrect_password(self, user):
        with allure.step("Отправляем запрос на авторизацию пользователя с неверным паролем"):
            response = UserLoginMethods.create_user(TEST_USER.email, user.password, TEST_USER.name)
        assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"
        assert response.json()["message"] == "email or password are incorrect"    

    
