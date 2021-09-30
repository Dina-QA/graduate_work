from selenium.webdriver.common.by import By


class HeaderBarLocators:

    LOCATOR_MENU_DROP_DOWN = (By.CSS_SELECTOR, "//button[text()='Dina']")
    LOCATOR_LOGOUT_BUTTON = (By.XPATH, "//button[text()='Log Out']")
    LOCATOR_CART_BUTTON = (By.CSS_SELECTOR, ".css-1v2z8uw.eonk1x81")
    