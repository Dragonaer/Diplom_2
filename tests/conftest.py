import pytest
from helpers import test_user
from api_methods.user_creation import UserMethods


@pytest.fixture
def registered_user():
    user = test_user()
    response = UserMethods.create_user(user.email, user.password, user.name)
    token = response.json().get("accessToken")
    yield user, token
    UserMethods.delete_user(token)


@pytest.fixture
def user_to_create():
    user = test_user()
    yield user
    if user.token:
        UserMethods.delete_user(user.token)