import allure
from pages.main_page import MainPage


@allure.title("Переход по клику на 'Конструктор'")
def test_go_to_constructor(driver):
    page = MainPage(driver)
    page.click_constructor()
    assert page.is_on_constructor_section(), "Секция конструктора не отображается"


@allure.title("Переход по клику на 'Лента заказов'")
def test_go_to_order_feed(driver):
    page = MainPage(driver)
    page.click_order_feed()
    assert page.is_on_order_feed(), "Переход в 'Ленту заказов' не выполнен"


@allure.title("Открытие и закрытие всплывающего окна при клике по крестику")
def test_ingredient_modal_open_and_close(driver):
    page = MainPage(driver)

    page.click_ingredient()
    assert page.is_modal_open(), "Модальное окно не открылось"

    page.close_modal()
    page.wait_for_modal_to_close()
    assert page.is_modal_closed(), "Модальное окно не закрылось"


@allure.title("Увеличивается счётчик ингредиента при добавлении")
def test_counter_increment_when_add_to_burger(driver):
    page = MainPage(driver)

    initial_count = page.get_ingredient_counter(0)
    page.drag_ingredient_to_constructor(0)
    final_count = page.get_ingredient_counter(0)

    assert final_count > initial_count, f"Счётчик ингредиента не увеличился: было {initial_count}, стало {final_count}"


@allure.title("Оформление заказа")
def test_place_order(driver, login_user):
    page = MainPage(driver)

    page.drag_ingredient_to_constructor(0)
    page.place_order()

    assert page.is_order_confirmed(), "Заказ не был подтверждён"
