from selenium.webdriver.common.by import By


class CartPageLocators:
    LOCATOR_GET_STARTED_BUTTON = (By.XPATH, "//button[text()='Get started']")
    LOCATOR_NAME_PRODUCT_TEXT = (By.XPATH, "//div[text()='Sunbasket Gift Credit']")
    LOCATOR_CART_IS_EMPTY_TEXT = (By.XPATH, "//p[text()='Your Cart is Empty']")
