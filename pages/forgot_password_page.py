import allure
from .base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators

class ForgotPasswordPage(BasePage):

    @allure.step("Ввод email для восстановления: {email}")
    def fill_email(self, email):
        self.fill_field(ForgotPasswordLocators.EMAIL_INPUT, email)

    @allure.step("Клик по кнопке 'Восстановить'")
    def click_restore(self):
        self.click(ForgotPasswordLocators.RESTORE_BUTTON)

    @allure.step("Клик по иконке показать/скрыть пароль")
    def click_eye_icon(self):
        self.click(ForgotPasswordLocators.PASSWORD_EYE_ICON)

    @allure.step("Проверка, что поле пароля активно (подсвечено)")
    def is_password_field_highlighted(self):
        return self.is_visible(ForgotPasswordLocators.ACTIVE_PASSWORD_FIELD)
