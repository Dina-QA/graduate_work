from selenium.webdriver.common.by import By


class LoginPageLocator:

    LOCATOR_EMAIL_LOGIN_FIELD = (By.ID, "email")
    LOCATOR_PASSWD_LOGIN_FIELD = (By.ID, "password")
    LOCATOR_SIGNIN_BUTTON = (By.XPATH, "//button[text()='SIGN IN']")
    LOCATOR_LOG_IN_TEXT = (By.XPATH, "//h2[text()='Log In']")
