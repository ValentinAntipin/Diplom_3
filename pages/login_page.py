import allure
from .base_page import BasePage
from locators.login_locators import LoginLocators

class LoginPage(BasePage):
    @allure.step("Открытие страницы логина: {url}")
    def open_login(self, url):
        self.open(url)

    @allure.step("Авторизация пользователя")
    def login(self, email, password):
        print(f"Попытка входа с email: {email}")
        self.fill_field(LoginLocators.EMAIL, email)
        self.fill_field(LoginLocators.PASSWORD, password)
        self.driver.save_screenshot("before_submit.png")
        self.click(LoginLocators.LOGIN_BUTTON)

    @allure.step("Переход на страницу восстановления пароля")
    def go_to_forgot_password(self):
        self.click(LoginLocators.FORGOT_PASSWORD_LINK)

    @allure.step("Переход на страницу регистрации")
    def go_to_register(self):
        self.click(LoginLocators.REGISTER)