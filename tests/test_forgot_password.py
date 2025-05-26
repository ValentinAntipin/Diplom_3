import allure
import pytest

from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from data.data import get_forgot_password_email
from data.constants import BASE_URL


@allure.suite("Тесты восстановления пароля")
@pytest.mark.usefixtures("driver")
class TestForgotPassword:

    @allure.title("Переход на страницу восстановления пароля по кнопке 'Восстановить пароль'")
    def test_open_forgot_password_page(self, driver):
        login = LoginPage(driver)

        login.open(f"{BASE_URL}/login")
        login.go_to_forgot_password()

        forgot = ForgotPasswordPage(driver)
        assert forgot.is_on_forgot_password_page(), "Не произошёл переход на страницу восстановления пароля"

    @allure.title("Ввод почты и клик по кнопке 'Восстановить'")
    def test_restore_password_button(self, driver):
        forgot = ForgotPasswordPage(driver)

        forgot.open_forgot_password_page(BASE_URL)
        forgot.restore_password(get_forgot_password_email())

        assert forgot.is_on_reset_password_page(), "Не перешли на страницу сброса пароля после клика"

    @allure.title("Кнопка показать/скрыть пароль подсвечивает поле ввода")
    def test_show_hide_password_highlights_field(self, driver):
        forgot = ForgotPasswordPage(driver)

        forgot.open_forgot_password_page(BASE_URL)
        forgot.restore_password(get_forgot_password_email())
        forgot.click_eye_icon()

        assert forgot.is_password_field_highlighted(), \
            "Поле пароля не подсветилось после клика на иконку"
