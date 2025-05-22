import allure
from pages.base_page import BasePage
from locators.account_locators import AccountLocators

class AccountPage(BasePage):
    @allure.step("Переход в личный кабинет через хедер")
    def go_to_profile(self):
        self.click(AccountLocators.HEADER_PROFILE_BUTTON)
        self.wait_for_element(AccountLocators.PROFILE_PAGE_HEADER)

    @allure.step("Переход в раздел 'История заказов'")
    def go_to_history(self):
        self.click(AccountLocators.ORDER_HISTORY_TAB)

    @allure.step("Выход из аккаунта")
    def logout(self):
        self.click(AccountLocators.LOGOUT_BUTTON)

    @allure.step("Проверяем, что открыта страница профиля")
    def is_on_profile_page(self):
        self.wait_for_url_to_contain("/account/profile")
        return "/account/profile" in self.get_current_url()

    @allure.step("Проверяем, что открыта страница истории заказов")
    def is_on_order_history_page(self):
        self.wait_for_url_to_contain("/account/order-history")
        return "/account/order-history" in self.get_current_url()

    @allure.step("Проверяем, что произошёл выход и открыт логин")
    def is_logged_out(self):
        self.wait_for_url_to_contain("/login")
        return "/login" in self.get_current_url()

