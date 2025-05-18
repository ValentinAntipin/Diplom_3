from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators

class PasswordRecoveryPage(BasePage):
    def enter_email(self, email):
        self.driver.find_element(*PasswordRecoveryLocators.EMAIL_INPUT).send_keys(email)

    def click_recover_button(self):
        self.driver.find_element(*PasswordRecoveryLocators.RECOVER_BUTTON).click()

    def toggle_password_visibility(self):
        self.driver.find_element(*PasswordRecoveryLocators.SHOW_PASSWORD_BUTTON).click()

    def is_email_input_visible(self):
        return self.driver.find_element(*PasswordRecoveryLocators.EMAIL_INPUT).is_displayed()

    def is_password_field_highlighted(self):
        return self.driver.find_element(*PasswordRecoveryLocators.PASSWORD_FIELD_ACTIVE).is_displayed()
