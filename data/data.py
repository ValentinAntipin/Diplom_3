import random
import string

def generate_user():
    email = f"user_{random.randint(1000,9999)}@yandex.ru"
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return {"email": email, "password": password, "name": "Test User"}


def get_forgot_password_email():
    return "user_1709@yandex.ru"