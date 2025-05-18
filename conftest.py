import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.login_page import LoginPage
from data.data import generate_user

BASE_URL = "https://stellarburgers.nomoreparties.site"
API_URL = f"{BASE_URL}/api"

def get_browser(browser):
    if browser == "chrome":
        return webdriver.Chrome()
    elif browser == "firefox":
        return webdriver.Firefox()
    else:
        raise ValueError("This browser type is not supported")

@pytest.fixture(params=("chrome", "firefox"))
def driver(request):
    browser = get_browser(request.param)
    browser.maximize_window()
    browser.get(BASE_URL)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()

@pytest.fixture
def login_user(driver):
    # Генерация данных пользователя
    user = generate_user()

    # Создание пользователя через API
    register_response = requests.post(
        f"{API_URL}/auth/register",
        json=user
    )
    assert register_response.ok, f"Ошибка регистрации: {register_response.text}"

    # Авторизация через UI
    login_page = LoginPage(driver)
    login_page.open(f"{BASE_URL}/login")
    login_page.login(user["email"], user["password"])

    # Авторизация через API для получения токена
    login_response = requests.post(
        f"{API_URL}/auth/login",
        json={"email": user["email"], "password": user["password"]}
    )
    assert login_response.ok, f"Ошибка авторизации: {login_response.text}"
    token = login_response.json()["accessToken"]

    yield {"email": user["email"], "password": user["password"], "accessToken": token}

    # Удаление пользователя
    headers = {"Authorization": token}
    delete_response = requests.delete(f"{API_URL}/auth/user", headers=headers)
    assert delete_response.ok, f"Ошибка удаления пользователя: {delete_response.text}"

@pytest.fixture
def create_order(login_user):
    token = login_user["accessToken"]
    headers = {"Authorization": token}

    # Получение ингредиентов
    ing_response = requests.get(f"{API_URL}/ingredients")
    assert ing_response.ok, "Ошибка получения ингредиентов"
    ingredient_ids = [i["_id"] for i in ing_response.json()["data"][:2]]

    # Создание заказа
    order_response = requests.post(
        f"{API_URL}/orders",
        headers=headers,
        json={"ingredients": ingredient_ids}
    )

    assert order_response.ok, "Ошибка создания заказа"
    return order_response.json()["order"]["number"]


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL