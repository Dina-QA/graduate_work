from selenium.webdriver.common.by import By


class SignupPageLocators:
    LOCATOR_FIRST_NAME_SIGNUP_FIELD = (By.ID, "firstName")
    LOCATOR_LAST_NAME_SIGNUP_FIELD = (By.ID, "lastName")
    LOCATOR_EMAIL_SIGNUP_FIELD = (By.ID, "email")
    LOCATOR_PASSWD_SIGNUP_FIELD = (By.ID, "password")
    LOCATOR_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Submit']")
    LOCATOR_SIGNUP_TEXT = (By.XPATH, "//h2[text()='Get Early Access']")
