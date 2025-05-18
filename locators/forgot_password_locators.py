from selenium.webdriver.common.by import By

class PasswordRecoveryLocators:
    EMAIL_INPUT = (By.NAME, "name")
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    SHOW_PASSWORD_BUTTON = (By.CLASS_NAME, "input__icon")
    PASSWORD_FIELD_ACTIVE = (By.CLASS_NAME, "input_status_active")
