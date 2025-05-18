import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.account_locators import AccountLocators

class AccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Переход в личный кабинет через хедер")
    def go_to_profile(self):
        self.driver.find_element(*AccountLocators.HEADER_PROFILE_BUTTON).click()
        self.wait.until(EC.presence_of_element_located(AccountLocators.PROFILE_PAGE_HEADER))

    @allure.step("Переход в раздел 'История заказов'")
    def go_to_history(self):
        self.driver.find_element(*AccountLocators.ORDER_HISTORY_TAB).click()

    @allure.step("Выход из аккаунта")
    def logout(self):
        self.driver.find_element(*AccountLocators.LOGOUT_BUTTON).click()
