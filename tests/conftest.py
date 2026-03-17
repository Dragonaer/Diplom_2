import pytest
from helpers import create_test_user
from api_methods.user_creation import UserMethods

@pytest.fixture
def registered_user():
    user = create_test_user()
    response = UserMethods.create_user(user.email, user.password, user.name)
    token = response.json().get('accessToken')
    yield user, token
    UserMethods.delete_user(token)



@pytest.fixture
def temp_user():
    return create_test_user()

