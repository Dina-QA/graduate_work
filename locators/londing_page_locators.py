from selenium.webdriver.common.by import By


class LandingPageLocators:
    LOCATOR_GET_STARTED_BUTTON = (By.XPATH, "//button[text()='Get Started']")
    LOCATOR_TITLE_TEXT = (By.CSS_SELECTOR, ".css-1sqcmeu.el0jnqq4")
    LOCATOR_LOGIN_BUTTON = (By.XPATH, "//button[text()='Log In']")