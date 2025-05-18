import allure
from pages.main_page import MainPage


@allure.title("Переход по клику на 'Конструктор'")
def test_go_to_constructor(driver):
    main = MainPage(driver)

    with allure.step("Кликаем по кнопку 'Конструктор'"):
        main.click_constructor()

    with allure.step("Проверяем, что секция конструктора отображается"):
        assert main.is_constructor_section_displayed(), "Секция конструктора не отображается"


@allure.title("Переход по клику на 'Лента заказов'")
def test_go_to_order_feed(driver):
    main = MainPage(driver)

    with allure.step("Кликаем по кнопку 'Лента заказов'"):
        main.click_order_feed()

    with allure.step("Проверяем, что URL содержит '/feed'"):
        assert "/feed" in driver.current_url


@allure.title("Открытие и закрытие всплывающего окна при клике по крестику")
def test_ingredient_modal_open_and_close(driver):
    main = MainPage(driver)

    with allure.step("Кликаем по первому ингредиенту"):
        main.click_ingredient()

    with allure.step("Проверяем, что модальное окно открылось"):
        assert main.is_modal_open(), "Модальное окно не открылось"

    with allure.step("Закрываем модальное окно"):
        main.close_modal()

    with allure.step("Проверяем, что модальное окно закрылось"):
        assert not main.is_modal_open(), "Модальное окно не закрылось"


@allure.title("Увеличивается счётчик ингредиента при добавлении")
def test_counter_increment_when_add_to_burger(driver):
    main = MainPage(driver)

    with allure.step("Получаем общее количество ингредиентов до добавления"):
        initial_count = main.get_total_ingredient_count()

    with allure.step("Кликаем по первому ингредиенту и закрываем модалку"):
        main.click_ingredient(0)
        main.close_modal()

    with allure.step("Получаем общее количество ингредиентов после добавления"):
        final_count = main.get_total_ingredient_count()

    with allure.step("Проверяем, что счётчик увеличился"):
        assert final_count > initial_count, "Счётчик ингредиента не увеличился"


@allure.title("Оформление заказа")
def test_place_order(driver, login_user):
    main = MainPage(driver)

    with allure.step("Кликаем по кнопке 'Оформить заказ'"):
        main.place_order()

    with allure.step("Проверяем, что заказ был успешно оформлен"):
        assert main.is_order_confirmed(), "Заказ не был подтверждён"
