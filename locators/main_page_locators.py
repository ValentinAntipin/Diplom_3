from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_LINK = (By.XPATH, "//a[contains(@href, '/feed')]")
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    INGREDIENT = (By.XPATH, "//a[contains(@href, '/ingredient')]")
    INGREDIENT_COUNTER = (By.CLASS_NAME, "counter")

    INGREDIENT_MODAL = (By.XPATH, "//div[contains(@class, 'modal') and contains(@class, 'container')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'modal__close')]")

    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_CONFIRMATION_TEXT = (By.CLASS_NAME, "order-details")
    CONSTRUCTOR_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")
    CONSTRUCTOR_DROP_ZONE = (By.CLASS_NAME, "BurgerConstruction_basket__29Cd7 mt-25")
