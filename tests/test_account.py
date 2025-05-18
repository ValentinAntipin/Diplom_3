import allure
from pages.account_page import AccountPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@allure.title("Переход по клику на 'Личный кабинет'")
def test_open_profile(driver, login_user):
    profile = AccountPage(driver)

    with allure.step("Переход в личный кабинет"):
        profile.go_to_profile()

    with allure.step("Ожидание изменения URL и проверка результата"):
        WebDriverWait(driver, 5).until(EC.url_contains("/account/profile"))
        assert "/account/profile" in driver.current_url


@allure.title("Переход в раздел 'История заказов'")
def test_go_to_order_history(driver, login_user):
    profile = AccountPage(driver)

    with allure.step("Переход в личный кабинет"):
        profile.go_to_profile()

    with allure.step("Переход в историю заказов"):
        profile.go_to_history()

    with allure.step("Ожидание изменения URL и проверка результата"):
        WebDriverWait(driver, 5).until(EC.url_contains("/account/order-history"))
        assert "/account/order-history" in driver.current_url


@allure.title("Выход из аккаунта")
def test_logout_from_profile(driver, login_user):
    profile = AccountPage(driver)

    with allure.step("Переход в личный кабинет"):
        profile.go_to_profile()

    with allure.step("Выход из аккаунта"):
        profile.logout()

    with allure.step("Ожидание редиректа на /login и проверка"):
        WebDriverWait(driver, 5).until(EC.url_contains("/login"))
        assert "/login" in driver.current_url
