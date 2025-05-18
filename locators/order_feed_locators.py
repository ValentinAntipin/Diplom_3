from selenium.webdriver.common.by import By

class OrderFeedLocators:
    ORDER_CARD = (By.CLASS_NAME, "OrderFeed_lis__OLh59")
    ORDER_MODAL = (By.CLASS_NAME, "Modal_modal__container__")
    TOTAL_DONE = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_DONE = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    IN_PROGRESS_SECTION = (By.XPATH, "//h3[text()='В работе']/following-sibling::ul")
