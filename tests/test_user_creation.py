import allure
import pytest

from api_methods.user_creation import UserMethods
from data import TEST_USER


class TestCreateUser:

    @allure.title("Создание пользователя c данными зарегистрированного пользователя")
    @allure.description("Проверка создания пользователя с данными зарегистрированного пользователя")
    def test_create_user_authorized_user(self):
        with allure.step("Отправляем запрос на создание пользователя с данными зарегистрированного пользователя"):
            response = UserMethods.create_user(TEST_USER.email, TEST_USER.password, TEST_USER.name)
        assert response.status_code == 403, f"Expected status code 403, but got {response.status_code}"   
        assert response.json()["message"] == "User already exists"

        
    @allure.title("Создание пользователя без email")
    @allure.description("Проверка создания пользователя с рандомными валидными данными без email")
    def test_create_user_no_email(self, temp_user):
        with allure.step("Отправляем запрос на создание пользователя с рандомными данными без ввода email"):
            response = UserMethods.create_user_no_email(temp_user.password, temp_user.name)
        assert response.status_code == 403, f"Expected status code 403, but got {response.status_code}"
        assert response.json()["message"] == "Email, password and name are required fields"

    @allure.title("Создание пользователя без пароля")
    @allure.description("Проверка создания пользователя с рандомными валидными данными без пароля")
    def test_create_user_no_password(self, temp_user):
        with allure.step("Отправляем запрос на создание пользователя с рандомными данными без пароля"):
            response = UserMethods.create_user_no_password(temp_user.email, temp_user.name)
        assert response.status_code == 403, f"Expected status code 403, but got {response.status_code}"
        assert response.json()["message"] == "Email, password and name are required fields"



