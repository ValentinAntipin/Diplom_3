from selenium.webdriver.common.by import By


class OrderFeedLocators:
    # Карточка заказа в ленте
    ORDER_CARD = (By.CLASS_NAME, "OrderFeed_lis__OLh59")

    # Модальное окно заказа
    ORDER_MODAL = (By.CLASS_NAME, "Modal_modal__container__")

    # Количество выполненных заказов за все время
    TOTAL_DONE = (By.XPATH, "//p[contains(text(),'Выполнено за все время')]/following-sibling::p")

    # Количество заказов, выполненных сегодня
    TODAY_DONE = (By.XPATH, "//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p")

    # Секция «В работе»
    IN_PROGRESS_SECTION = (By.XPATH, "//h3[text()='В работе']/following-sibling::ul")
