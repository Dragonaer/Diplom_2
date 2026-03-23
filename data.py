class User:
    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

        self.token = None



        
TEST_USER = User("loseva39@mail.ru", "qwerty", "Лиза")
ORDER_NO_INGREDIENTS_MSG = "Ingredient ids must be provided"
