import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    @allure.step("Открываем страницу: {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Кликаем по элементу: {locator}")
    def click(self, locator):
        try:
            element = self.wait_for_element_clickable(locator)
            element.click()
        except TimeoutException:
            self.attach_screenshot("click_timeout")
            raise AssertionError(f"Элемент не кликабелен: {locator}")

    @allure.step("Заполняем поле: {locator} значением: {value}")
    def fill_field(self, locator, value):
        try:
            field = self.wait_for_element(locator)
            field.send_keys(value)
        except TimeoutException:
            self.attach_screenshot("fill_field_timeout")
            raise AssertionError(f"Поле не найдено для заполнения: {locator}")

    @allure.step("Получаем текст из элемента: {locator}")
    def get_text(self, locator):
        try:
            return self.wait_for_element(locator).text
        except TimeoutException:
            self.attach_screenshot("get_text_timeout")
            raise AssertionError(f"Текст не найден для элемента: {locator}")

    @allure.step("Проверяем, что элемент видим: {locator}")
    def is_visible(self, locator):
        try:
            return self.wait_for_element(locator).is_displayed()
        except TimeoutException:
            return False

    @allure.step("Ожидаем элемент на странице: {locator}")
    def wait_for_element(self, locator, timeout=10):
        timeout = timeout or self.timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Ожидаем кликабельность элемента: {locator}")
    def wait_for_element_clickable(self, locator, timeout=15):
        timeout = timeout or self.timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    @allure.step("Ожидаем несколько элементов: {locator}")
    def wait_for_elements(self, locator, timeout=10):
        timeout = timeout or self.timeout
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    @allure.step("Поиск одного элемента без ожидания: {locator}")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Поиск нескольких элементов без ожидания: {locator}")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Ожидаем, что URL содержит: {fragment}")
    def wait_for_url_to_contain(self, fragment, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(fragment))

    @allure.step("Получаем текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Перетаскиваем элемент: {source_locator} в элемент: {target_locator}")
    def drag_and_drop(self, source_locator, target_locator):
        try:
            source = self.wait_for_element(source_locator)
            target = self.wait_for_element(target_locator)
            ActionChains(self.driver).click_and_hold(source).move_to_element(target).release().perform()
        except TimeoutException:
            self.attach_screenshot("drag_and_drop_timeout")
            raise AssertionError(f"Не удалось перетащить элемент: {source_locator} в {target_locator}")

    def attach_screenshot(self, name):
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    @allure.step("Ожидаем, что элемент исчезнет с экрана: {locator}")
    def wait_for_element_to_disappear(self, locator, timeout=10):
        timeout = timeout or self.timeout
        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            allure.attach(self.driver.get_screenshot_as_png(), name="disappear_timeout",
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(f"Элемент не исчез: {locator}")

    @allure.step("Прокрутка элементов")
    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Ввод текста '{text}' в элемент {locator}")
    def send_keys(self, locator, text: str, timeout: int = 10):
        element = self.wait_for_element(locator, timeout)
        element.clear()
        element.send_keys(text)
