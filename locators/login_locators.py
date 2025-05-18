from selenium.webdriver.common.by import By

class LoginLocators:
    EMAIL = (By.XPATH, "//input[@name='name' or @name='email']")
    PASSWORD = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")
    REGISTER = (By.LINK_TEXT, "Зарегистрироваться")
