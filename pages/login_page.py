from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocator


class LoginPage(BasePage):
    def should_be_login_page(self):
        text_check = "Log In"
        login_text = self.find_element(LoginPageLocator.LOCATOR_LOG_IN_TEXT).text
        assert login_text == text_check, f'{login_text} is not equal to {text_check}'

    def login(self, email: str, passwd: str):
        email_field = self.find_element(LoginPageLocator.LOCATOR_EMAIL_LOGIN_FIELD)
        email_field.clear()
        email_field.send_keys(email)
        passwd_field = self.find_element(LoginPageLocator.LOCATOR_PASSWD_LOGIN_FIELD)
        passwd_field.clear()
        passwd_field.send_keys(passwd)
        self.find_element(LoginPageLocator.LOCATOR_SIGNIN_BUTTON).click()
