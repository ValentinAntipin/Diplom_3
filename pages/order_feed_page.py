import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators

class OrderFeedPage(BasePage):

    @allure.step("Открытие модального окна заказа с индексом {index}")
    def open_order_modal(self, index=0):
        self.driver.find_elements(*OrderFeedLocators.ORDER_CARD)[index].click()

    @allure.step("Проверка, что модальное окно заказа открыто")
    def is_modal_open(self):
        return self.is_visible(OrderFeedLocators.ORDER_MODAL)

    @allure.step("Получение общего количества выполненных заказов")
    def get_total_done_count(self):
        return int(self.driver.find_element(*OrderFeedLocators.TOTAL_DONE).text)

    @allure.step("Получение количества заказов, выполненных сегодня")
    def get_today_done_count(self):
        return int(self.driver.find_element(*OrderFeedLocators.TODAY_DONE).text)

    @allure.step("Проверка, что блок заказов в процессе виден")
    def is_order_in_progress_section_visible(self):
        return self.driver.find_element(*OrderFeedLocators.IN_PROGRESS_SECTION).is_displayed()
