import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def fill_field(self, locator, value):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)).send_keys(value)

    def get_text(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text

    def is_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).is_displayed()

    def wait_for_element(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )