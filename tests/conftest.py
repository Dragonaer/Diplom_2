import pytest
from url import *
from helpers import generate_random_string, generate_random_email
from data import *


@pytest.fixture(scope="function")
def user():
    email = generate_random_email()
    password = generate_random_string(7)
    name = generate_random_string(7)
    return User(email, password, name)
    
