import allure
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):

    @allure.step("Переход в ленту заказов")
    def go_to_order_feed(self, base_url):
        self.open(f"{base_url}/feed")

    @allure.step("Открытие модального окна заказа с индексом {index}")
    def open_order_modal(self, index=0):
        elements = self.find_elements(OrderFeedLocators.ORDER_CARD)
        elements[index].click()

    @allure.step("Проверка, что модальное окно заказа открыто")
    def is_modal_open(self):
        return self.is_visible(OrderFeedLocators.ORDER_MODAL)

    @allure.step("Получение общего количества выполненных заказов")
    def get_total_done_count(self):
        return int(self.get_text(OrderFeedLocators.TOTAL_DONE))

    @allure.step("Получение количества заказов, выполненных сегодня")
    def get_today_done_count(self):
        return int(self.get_text(OrderFeedLocators.TODAY_DONE))

    @allure.step("Проверка, что заказ с номером {order_number} отображается в ленте")
    def is_order_in_feed(self, order_number: str) -> bool:
        return order_number in self.driver.page_source

    @allure.step("Проверка, что заказ с номером {order_number} отображается в секции 'В работе'")
    def is_order_in_work_section(self, order_number: str) -> bool:
        try:
            work_section = self.driver.find_element(*OrderFeedLocators.IN_PROGRESS_SECTION)
            return order_number in work_section.text
        except NoSuchElementException:
            return False
