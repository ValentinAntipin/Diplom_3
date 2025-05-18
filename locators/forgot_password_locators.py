from selenium.webdriver.common.by import By

class ForgotPasswordLocators:
    EMAIL_INPUT = (By.NAME, "name")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_EYE_ICON = (By.CLASS_NAME, "input__icon")
    ACTIVE_PASSWORD_FIELD = (By.CLASS_NAME, "input_status_active")
