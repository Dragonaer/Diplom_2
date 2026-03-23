import requests
import random
import string
from data import *


# метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = "".join(random.choice(letters) for i in range(length))
    return random_string


def generate_random_email():
    domain = "test.com"
    username = generate_random_string(7)
    return f"{username}@{domain}"


def register_new_user_and_return_login_password():

    login_pass = []

    email = generate_random_email(15)
    password = generate_random_string(7)
    name = generate_random_string(7)

    payload = {"login": email, "password": password, "firstName": name}

    response = requests.post(
        "https://stellarburgers.education-services.ru/api/auth/register", data=payload
    )

    if response.status_code == 201:
        login_pass.append(email)
        login_pass.append(password)
        login_pass.append(name)

    return login_pass


def test_user():
    email = generate_random_email()
    password = generate_random_string(7)
    name = generate_random_string(7)
    return User(email, password, name)
