import allure
from pages.base_page import BasePage
from locators.login_locators import LoginLocators


class LoginPage(BasePage):

    @allure.step("Открываем страницу логина: {url}")
    def open(self, url):
        super().open(url)

    @allure.step("Вводим email: {email}")
    def enter_email(self, email):
        self.fill_field(LoginLocators.EMAIL, email)

    @allure.step("Вводим пароль: {password}")
    def enter_password(self, password):
        self.fill_field(LoginLocators.PASSWORD, password)

    @allure.step("Нажимаем кнопку 'Войти'")
    def click_login_button(self):
        self.click(LoginLocators.LOGIN_BUTTON)

    @allure.step("Авторизуемся как пользователь: {email}")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    @allure.step("Проверяем, что отображается сообщение об ошибке")
    def get_error_message(self):
        return self.get_text(LoginLocators.ERROR_MESSAGE)

    @allure.step("Переход на страницу восстановления пароля")
    def go_to_forgot_password(self):
        self.click(LoginLocators.FORGOT_PASSWORD_LINK)