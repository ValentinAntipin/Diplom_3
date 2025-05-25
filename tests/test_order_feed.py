import allure
import pytest
from pages.order_feed_page import OrderFeedPage
from data.constants import BASE_URL


@allure.suite("Тесты ленты заказов")
@pytest.mark.usefixtures("driver")
class TestOrderFeed:

    @allure.title("Открытие деталей заказа в ленте заказов")
    def test_open_order_modal(self, driver):
        feed = OrderFeedPage(driver)
        feed.open_order_modal()
        assert feed.is_modal_open(), "Модальное окно заказа не открылось"

    @allure.title("Счётчик 'Выполнено за всё время' увеличивается после создания заказа")
    def test_total_done_counter_increases(self, driver, create_order):
        feed = OrderFeedPage(driver)
        feed.go_to_order_feed(BASE_URL)
        assert feed.get_total_done_count() >= 1, "Счётчик всех заказов не увеличился"

    @allure.title("Счётчик 'Выполнено за сегодня' увеличивается после создания заказа")
    def test_today_done_counter_increases(self, driver, create_order):
        feed = OrderFeedPage(driver)
        feed.go_to_order_feed(BASE_URL)
        assert feed.get_today_done_count() >= 1, "Счётчик заказов за сегодня не увеличился"

    @allure.title("После оформления заказ появляется в разделе 'В работе'")
    def test_order_appears_in_work_section(self, driver, create_order):
        feed = OrderFeedPage(driver)
        feed.go_to_order_feed(BASE_URL)
        assert feed.is_order_in_work_section(str(create_order)), "Заказ не появился в 'В работе'"

    @allure.title("Заказы пользователя отображаются в ленте заказов")
    def test_user_order_visible_in_feed(self, driver, create_order):
        feed = OrderFeedPage(driver)
        feed.go_to_order_feed(BASE_URL)
        assert feed.is_order_in_feed(str(create_order)), \
            f"Номер заказа {create_order} не найден в ленте заказов"
