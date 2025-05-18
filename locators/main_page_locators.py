from selenium.webdriver.common.by import By

class MainLocators:
    CONSTRUCTOR_TAB = (By.XPATH, "//p[text()='Конструктор']")
    FEED_TAB = (By.XPATH, "//p[text()='Лента заказов']")
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    INGREDIENT_ITEM = (By.CLASS_NAME, "burger-ingredient")
    INGREDIENT_COUNTER = (By.CLASS_NAME, "counter")
    INGREDIENT_MODAL = (By.CLASS_NAME, "Modal_modal__container__")
    MODAL_CLOSE_BUTTON = (By.CLASS_NAME, "Modal_close__TnseN")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")