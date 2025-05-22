import allure
from selenium.common import TimeoutException

from .base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Переход в раздел 'Конструктор'")
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Переход в 'Ленту заказов'")
    def click_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_LINK)

    @allure.step("Клик по ингредиенту под индексом {index}")
    def click_ingredient(self, index=0):
        elements = self.wait_for_elements(MainPageLocators.INGREDIENT)
        if index < len(elements):
            elements[index].click()
        else:
            raise IndexError(f"Ингредиент с индексом {index} не найден. Всего элементов: {len(elements)}")

    @allure.step("Перетаскиваем ингредиент под индексом {index} в бургер")
    def drag_ingredient_to_constructor(self, index=0):
        elements = self.wait_for_elements(MainPageLocators.INGREDIENT)
        if index >= len(elements):
            raise IndexError(f"Ингредиент с индексом {index} не найден. Всего элементов: {len(elements)}")

        self.driver.execute_script("arguments[0].scrollIntoView(true);", elements[index])


        ingredient_xpath = f"({MainPageLocators.INGREDIENT[1]})[{index + 1}]"
        self.drag_and_drop(
            source_locator=(MainPageLocators.INGREDIENT[0], ingredient_xpath),
            target_locator=MainPageLocators.CONSTRUCTOR_DROP_ZONE
        )

    @allure.step("Проверка, что модальное окно открыто")
    def is_modal_open(self):
        return self.is_visible(MainPageLocators.INGREDIENT_MODAL)

    @allure.step("Закрытие модального окна")
    def close_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Получение количества счётчиков ингредиентов")
    def get_counter_count(self):
        return len(self.wait_for_elements(MainPageLocators.INGREDIENT_COUNTER))

    @allure.step("Подсчёт общего количества добавленных ингредиентов")
    def get_total_ingredient_count(self):
        counters = self.wait_for_elements(MainPageLocators.INGREDIENT_COUNTER)
        return sum(int(el.text.strip()) for el in counters if el.text.strip().isdigit())

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def place_order(self):
        self.click(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step("Проверка, что заказ успешно оформлен")
    def is_order_confirmed(self, timeout=10):
        try:
            element = self.wait_for_element(MainPageLocators.ORDER_CONFIRMATION_TEXT, timeout)
            return "Ваш заказ начали готовить" in element.text or "идентификатор" in element.text
        except Exception:
            return False

    @allure.step("Проверка, что секция конструктора отображается")
    def is_constructor_section_displayed(self):
        return self.is_visible(MainPageLocators.CONSTRUCTOR_HEADER)

    @allure.step("Проверка, что пользователь находится на ленте заказов")
    def is_on_order_feed(self):
        return "/feed" in self.get_current_url()

    @allure.step("Проверка, что модальное окно закрыто")
    def is_modal_closed(self):
        try:
            return not self.is_visible(MainPageLocators.INGREDIENT_MODAL)
        except TimeoutException:
            return True

    @allure.step("Проверка, что пользователь на странице конструктора")
    def is_on_constructor_section(self):
        return self.is_constructor_section_displayed()

    @allure.step("Ожидаем загрузку секции конструктора")
    def wait_for_constructor(self):
        self.wait_for_element(MainPageLocators.CONSTRUCTOR_HEADER)

    @allure.step("Ожидаем закрытие модального окна")
    def wait_for_modal_to_close(self, timeout=5):
        self.wait_for_element_to_disappear(MainPageLocators.INGREDIENT_MODAL, timeout)

    @allure.step("Получение счётчика для ингредиента с индексом {index}")
    def get_ingredient_counter(self, index):
        elements = self.find_elements(MainPageLocators.INGREDIENT_COUNTER)
        if index < len(elements):
            text = elements[index].text.strip()
            return int(text) if text.isdigit() else 0
        raise IndexError(f"Счётчик ингредиента с индексом {index} не найден. Всего элементов: {len(elements)}")
