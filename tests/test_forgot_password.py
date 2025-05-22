import allure
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from data.data import get_forgot_password_email
from locators.forgot_password_locators import ForgotPasswordLocators

@allure.title("Переход на страницу восстановления пароля по кнопке 'Восстановить пароль'")
def test_open_forgot_password_page(driver, base_url):
    login = LoginPage(driver)
    login.open(f"{base_url}/login")
    login.go_to_forgot_password()
    assert "/forgot-password" in driver.current_url


@allure.title("Ввод почты и клик по кнопке 'Восстановить'")
def test_restore_password_button(driver, base_url):
    forgot = ForgotPasswordPage(driver)
    forgot.open(f"{base_url}/forgot-password")
    forgot.fill_email(get_forgot_password_email())
    forgot.click_restore()

    forgot.wait_for_element(ForgotPasswordLocators.RESTORE_BUTTON)
    assert "/forgot-password" in driver.current_url


@allure.title("Кнопка показать/скрыть пароль подсвечивает поле ввода")
def test_show_hide_password_highlights_field(driver, base_url):
    forgot = ForgotPasswordPage(driver)
    forgot.open(f"{base_url}/forgot-password")
    forgot.fill_email(get_forgot_password_email())
    forgot.click_restore()

    forgot.wait_for_element(ForgotPasswordLocators.PASSWORD_EYE_ICON)  # Ожидаем, пока иконка станет кликабельной
    forgot.click_eye_icon()

    assert forgot.is_password_field_highlighted(), "Поле пароля не подсветилось после клика на иконку"
