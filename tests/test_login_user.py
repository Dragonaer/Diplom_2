import allure
import pytest

from api_methods.login_user import UserLoginMethods


class TestLoginUser:
    @allure.title("Авторизация существующего пользователя")
    @allure.description("Проверка авторизации существующего пользователя")
    def test_login_user_valid(self, registered_user):
        user, _ = registered_user
        with allure.step(
            "Отправляем запрос на авторизацию пользователя с заполнением всех полей"
        ):
            response = UserLoginMethods.login_user(user.email, user.password)
        assert (
            response.status_code == 200
        ), f"Expected status code 200, but got {response.status_code}"
        assert response.json()["success"] == True

    @allure.title("Авторизация пользователя с неверным email")
    @allure.description("Проверка авторизации пользователя с неверным email")
    def test_login_user_incorrect_email(self, registered_user):
        user, _ = registered_user
        with allure.step(
            "Отправляем запрос на авторизацию пользователя с неверным email"
        ):
            response = UserLoginMethods.login_user(
                user.email[:-1], user.password
            )
        assert (
            response.status_code == 401
        ), f"Expected status code 401, but got {response.status_code}"
        assert response.json()["message"] == "email or password are incorrect"

    @allure.title("Авторизация пользователя с неверным паролем")
    @allure.description("Проверка авторизации пользователя с неверным паролем")
    def test_login_user_incorrect_password(self, registered_user):
        user, _ = registered_user
        with allure.step(
            "Отправляем запрос на авторизацию пользователя с неверным паролем"
        ):
            response = UserLoginMethods.login_user(
                user.email, user.password[:-1]
            )
        assert (
            response.status_code == 401
        ), f"Expected status code 401, but got {response.status_code}"
        assert response.json()["message"] == "email or password are incorrect"
