import allure
import pytest

from api_methods.user_creation import UserMethods


class TestCreateUser:

    @allure.title("Создание пользователя c данными зарегистрированного пользователя")
    @allure.description(
        "Проверка создания пользователя с данными зарегистрированного пользователя"
    )
    def test_create_user_authorized_user(self, registered_user):
        user, _ = registered_user
        with allure.step(
            "Отправляем запрос на создание пользователя с данными зарегистрированного пользователя"
        ):
            response = UserMethods.create_user(user.email, user.password, user.name)
        
        assert (response.status_code == 403), \
            f"Expected status code 403, but got {response.status_code}"
        assert response.json()["message"] == "User already exists"

    @allure.title("Создание пользователя без email")
    @allure.description(
        "Проверка создания пользователя с рандомными валидными данными без email"
    )
    def test_create_user_no_email(self, user_to_create):
        with allure.step(
            "Отправляем запрос на создание пользователя с рандомными данными без ввода email"
        ):
            response = UserMethods.create_user_no_email(
                user_to_create.password, user_to_create.name
            )

        assert (response.status_code == 403), \
            f"Expected status code 403, but got {response.status_code}"
        assert (response.json()["message"] == "Email, password and name are required fields")
        
        user_to_create.token = response.json().get("accessToken")

    @allure.title("Создание пользователя без пароля")
    @allure.description(
        "Проверка создания пользователя с рандомными валидными данными без пароля"
    )
    def test_create_user_no_password(self, user_to_create):
        with allure.step(
            "Отправляем запрос на создание пользователя с рандомными данными без пароля"
        ):
            response = UserMethods.create_user_no_password(
                user_to_create.email,
                user_to_create.name,
            )
            
        assert (response.status_code == 403), \
            f"Expected status code 403, but got {response.status_code}"
        assert (response.json()["message"] == "Email, password and name are required fields")
        
        user_to_create.token = response.json().get("accessToken")
