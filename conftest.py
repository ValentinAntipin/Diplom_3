import pytest
import requests
from selenium import webdriver
from pages.login_page import LoginPage
from data.data import generate_user
from data.constants import BASE_URL, API_URL


@pytest.fixture(scope="session")
def base_url():
    return BASE_URL


@pytest.fixture(scope="session")
def api_url():
    return API_URL


@pytest.fixture(params=("chrome", "firefox"))
def driver(request, base_url):
    browser_type = request.param
    if browser_type == "chrome":
        browser = webdriver.Chrome()
    elif browser_type == "firefox":
        browser = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser type")

    browser.maximize_window()
    browser.get(base_url)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@pytest.fixture
def login_user(driver, api_url, base_url):
    user = generate_user()

    register_response = requests.post(f"{api_url}/auth/register", json=user)

    login_page = LoginPage(driver)
    login_page.open(f"{base_url}/login")
    login_page.login(user["email"], user["password"])

    login_response = requests.post(
        f"{api_url}/auth/login",
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

    if token:
        headers = {"Authorization": token}
        requests.delete(f"{api_url}/auth/user", headers=headers)


@pytest.fixture
def create_order(login_user, api_url):
    token = login_user["accessToken"]
    if not token:
        return None

    headers = {"Authorization": token}
    ing_response = requests.get(f"{api_url}/ingredients")
    if not ing_response.ok:
        return None

    ingredient_ids = [i["_id"] for i in ing_response.json()["data"][:2]]
    order_response = requests.post(
        f"{api_url}/orders",
        headers=headers,
        json={"ingredients": ingredient_ids}
    )

    if not order_response.ok:
        return None

    return order_response.json()["order"]["number"]
