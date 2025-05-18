import allure
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class MainPage(BasePage):

    @allure.step("Переход в раздел 'Конструктор'")
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Переход в 'Ленту заказов'")
    def click_order_feed(self):
        self.wait_for_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.click(MainPageLocators.ORDER_FEED_LINK)

    @allure.step("Клик по ингредиенту под индексом {index}")
    def click_ingredient(self, index=0):
        elements = self.driver.find_elements(*MainPageLocators.INGREDIENT)
        elements[index].click()

    @allure.step("Проверка, что модальное окно открыто")
    def is_modal_open(self):
        return self.is_visible(MainPageLocators.INGREDIENT_MODAL)

    @allure.step("Закрытие модального окна")
    def close_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Получение количества счётчиков ингредиентов")
    def get_counter_count(self):
        return len(self.driver.find_elements(*MainPageLocators.INGREDIENT_COUNTER))

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def place_order(self):
        self.click(MainPageLocators.PLACE_ORDER_BUTTON)


    @allure.step("Проверка, что заказ успешно оформлен")
    def is_order_confirmed(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(MainPageLocators.ORDER_CONFIRMATION_TEXT)
            )
            text = self.driver.find_element(*MainPageLocators.ORDER_CONFIRMATION_TEXT).text
            return "Ваш заказ начали готовить" in text or "идентификатор" in text
        except TimeoutException:
            return False

    @allure.step("Проверка, что секция конструктора отображается")
    def is_constructor_section_displayed(self):
        return self.is_visible(MainPageLocators.CONSTRUCTOR_HEADER)

    @allure.step("Подсчёт общего количества добавленных ингредиентов")
    def get_total_ingredient_count(self):
        counters = self.driver.find_elements(*MainPageLocators.INGREDIENT_COUNTER)
        total = 0
        for el in counters:
            text = el.text.strip()
            if text.isdigit():
                total += int(text)
        return total

