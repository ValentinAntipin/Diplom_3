from selenium.webdriver.common.by import By

class AccountLocators:
    # Кнопка/ссылка в хедере, ведущая в личный кабинет
    HEADER_PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")

    # Заголовок на странице профиля (можно использовать как индикатор загрузки)
    PROFILE_PAGE_HEADER = (By.XPATH, "//a[text()='Профиль']")

    # Вкладка 'История заказов'
    ORDER_HISTORY_TAB = (By.XPATH, "//a[text()='История заказов']")

    # Кнопка 'Выход'
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
