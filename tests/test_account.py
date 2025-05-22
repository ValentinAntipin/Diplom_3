import allure
from pages.account_page import AccountPage

@allure.title("Переход по клику на 'Личный кабинет'")
def test_open_profile(driver, login_user):
    profile = AccountPage(driver)

    profile.go_to_profile()
    assert profile.is_on_profile_page()


@allure.title("Переход в раздел 'История заказов'")
def test_go_to_order_history(driver, login_user):
    profile = AccountPage(driver)

    profile.go_to_profile()
    profile.go_to_history()
    assert profile.is_on_order_history_page()


@allure.title("Выход из аккаунта")
def test_logout_from_profile(driver, login_user):
    profile = AccountPage(driver)

    profile.go_to_profile()
    profile.logout()
    assert profile.is_logged_out()
