import allure
from pages.base_page import BasePage
from locators.forgot_password_locators import ForgotPasswordLocators


class ForgotPasswordPage(BasePage):

    @allure.step("Открытие страницы восстановления пароля")
    def open_forgot_password_page(self, base_url: str):
        self.open(f"{base_url}/forgot-password")

    @allure.step("Ввод email и клик по кнопке 'Восстановить'")
    def restore_password(self, email: str):
        self.fill_email(email)
        self.click_restore()
        self.wait_until_restored()

    @allure.step("Заполнение поля Email: {email}")
    def fill_email(self, email: str):
        self.send_keys(ForgotPasswordLocators.EMAIL_INPUT, email)

    @allure.step("Клик по кнопке 'Восстановить'")
    def click_restore(self):
        self.click(ForgotPasswordLocators.RESTORE_BUTTON)

    @allure.step("Ожидание обработки формы восстановления")
    def wait_until_restored(self):
        self.wait_for_element(ForgotPasswordLocators.RESTORE_BUTTON)

    @allure.step("Клик по иконке 'Показать/скрыть пароль'")
    def click_eye_icon(self):
        self.click(ForgotPasswordLocators.PASSWORD_EYE_ICON)

    @allure.step("Показать/скрыть пароль")
    def reveal_password(self):
        self.wait_for_element(ForgotPasswordLocators.PASSWORD_EYE_ICON)
        self.click_eye_icon()

    @allure.step("Проверка, что пользователь находится на странице восстановления пароля")
    def is_on_forgot_password_page(self) -> bool:
        current = self.get_current_url()
        print("DEBUG URL:", current)
        return "/forgot-password" in current

    @allure.step("Проверка, что поле пароля подсвечено")
    def is_password_field_highlighted(self) -> bool:
        element = self.find_element(ForgotPasswordLocators.ACTIVE_PASSWORD_FIELD)
        css_class = element.get_attribute("class") or ""
        return "input_status_active" in css_class or "highlight" in css_class

    @allure.step("Проверка, что пользователь находится на странице сброса пароля")
    def is_on_reset_password_page(self) -> bool:
        current = self.get_current_url()
        print("DEBUG URL:", current)
        return "/reset-password" in current