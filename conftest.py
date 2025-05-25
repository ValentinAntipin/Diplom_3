import pytest
import requests
from selenium import webdriver
from pages.login_page import LoginPage
from data.data import generate_user
from data.constants import BASE_URL, API_URL


@pytest.fixture(params=("chrome", "firefox"))
def driver(request):
    browser_type = request.param
    if browser_type == "chrome":
        browser = webdriver.Chrome()
    elif browser_type == "firefox":
        browser = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser type")

    browser.maximize_window()
    browser.implicitly_wait(10)

    yield browser
    browser.quit()


@pytest.fixture
def login_user(driver):
    user = generate_user()

    # Регистрируем пользователя через API
    register_response = requests.post(f"{API_URL}/auth/register", json=user)

    # Логинимся через UI
    login_page = LoginPage(driver)
    login_page.open(f"{BASE_URL}/login")
    login_page.login(user["email"], user["password"])

    # Получаем access token через API
    login_response = requests.post(
        f"{API_URL}/auth/login",
        json={"email": user["email"], "password": user["password"]}
    )

    token = None
    if login_response.ok:
        token = login_response.json().get("accessToken")

    yield {
        "email": user["email"],
        "password": user["password"],
        "register_response": register_response,
        "login_response": login_response,
        "accessToken": token,
    }

    # Удаление пользователя после теста
    if token:
        headers = {"Authorization": token}
        requests.delete(f"{API_URL}/auth/user", headers=headers)


@pytest.fixture
def create_order(login_user):
    token = login_user["accessToken"]
    if not token:
        raise RuntimeError("Не удалось получить токен пользователя")

    headers = {"Authorization": token}
    ing_response = requests.get(f"{API_URL}/ingredients")
    if not ing_response.ok:
        raise RuntimeError("Не удалось получить список ингредиентов")

    ingredient_ids = [i["_id"] for i in ing_response.json()["data"][:2]]
    order_response = requests.post(
        f"{API_URL}/orders",
        headers=headers,
        json={"ingredients": ingredient_ids}
    )

    if not order_response.ok:
        raise RuntimeError("Не удалось создать заказ")

    return order_response.json()["order"]["number"]
