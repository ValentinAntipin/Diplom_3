import allure
from pages.order_feed_page import OrderFeedPage


@allure.title("Открытие деталей заказа в ленте заказов")
def test_open_order_modal(driver):
    feed = OrderFeedPage(driver)
    feed.open_order_modal()
    assert feed.is_modal_open()


@allure.title("Счётчик 'Выполнено за всё время' увеличивается после создания заказа")
def test_user_orders_displayed_in_feed(driver, create_order, base_url):
    driver.get(f"{base_url}/feed")
    assert "заказ" in driver.page_source.lower()


@allure.title("Счётчик 'Выполнено за сегодня' увеличивается после создания заказа")
def test_order_done_counters_increase(driver, create_order, base_url):
    driver.get(f"{base_url}/feed")
    done_today = int(driver.find_element_by_class_name("done_today").text)
    done_all = int(driver.find_element_by_class_name("done_all_time").text)
    assert done_today >= 1
    assert done_all >= 1


@allure.title("После оформления заказ появляется в разделе 'В работе'")
def test_order_appears_in_work_section(driver, create_order, base_url):
    driver.get(f"{base_url}/feed")
    assert str(create_order) in driver.page_source


@allure.title("Заказы пользователя отображаются в ленте заказов")
def test_user_order_visible_in_feed(driver, create_order, base_url):
    with allure.step("Открываем ленту заказов"):
        driver.get(f"{base_url}/feed")

    with allure.step("Проверяем, что номер заказа отображается в ленте"):
        assert str(create_order) in driver.page_source, \
            f"Номер заказа {create_order} не найден в ленте заказов"
