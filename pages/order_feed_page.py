import allure
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):

    @allure.step("Переход в ленту заказов")
    def go_to_order_feed(self, base_url):
        self.open(f"{base_url}/feed")

    @allure.step("Открытие модального окна заказа с индексом {index}")
    def open_order_modal(self, index=0):
        elements = self.wait_for_elements(OrderFeedLocators.ORDER_CARD)
        if index < len(elements):
            self.scroll_into_view(elements[index])
            elements[index].click()
        else:
            raise IndexError(f"Заказ с индексом {index} не найден. Всего элементов: {len(elements)}")

    @allure.step("Проверка, что модальное окно заказа открыто")
    def is_modal_open(self):
        return self.is_visible(OrderFeedLocators.ORDER_MODAL)

    @allure.step("Получение общего количества выполненных заказов")
    def get_total_done_count(self):
        text = self.get_text(OrderFeedLocators.TOTAL_DONE)
        return int(text.strip()) if text.strip().isdigit() else 0

    @allure.step("Получение количества заказов, выполненных сегодня")
    def get_today_done_count(self):
        text = self.get_text(OrderFeedLocators.TODAY_DONE)
        return int(text.strip()) if text.strip().isdigit() else 0

    @allure.step("Проверка, что заказ с номером {order_number} отображается в ленте")
    def is_order_in_feed(self, order_number: str) -> bool:
        try:
            elements = self.wait_for_elements(OrderFeedLocators.ORDER_CARD)
            return any(order_number in el.text for el in elements)
        except TimeoutException:
            return False

    @allure.step("Проверка, что заказ с номером {order_number} отображается в секции 'В работе'")
    def is_order_in_work_section(self, order_number: str) -> bool:
        try:
            section = self.wait_for_element(OrderFeedLocators.IN_PROGRESS_SECTION)
            return order_number in section.text
        except TimeoutException:
            return False
