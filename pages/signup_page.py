from pages.base_page import BasePage
from locators.signup_page_locators import SignupPageLocators
from time import sleep

class SignupPage(BasePage):
    def should_be_signup_page(self):
        signup_text = self.find_element(SignupPageLocators.LOCATOR_SIGNUP_TEXT)
        sleep(0.5)
        signup_text = signup_text.text
        text_check = 'Get Early Access'
        assert signup_text == text_check, f'{signup_text} is not equal to {text_check}'

    def signup(self, firstname: str, lastname: str, email: str, passwd: str):
        first_name = self.find_element(SignupPageLocators.LOCATOR_FIRST_NAME_SIGNUP_FIELD)
        first_name.send_keys(firstname)
        last_name = self.find_element(SignupPageLocators.LOCATOR_LAST_NAME_SIGNUP_FIELD)
        last_name.send_keys(lastname)
        email_field = self.find_element(SignupPageLocators.LOCATOR_EMAIL_SIGNUP_FIELD)
        email_field.clear()
        email_field.send_keys(email)
        passwd_field = self.find_element(SignupPageLocators.LOCATOR_PASSWD_SIGNUP_FIELD)
        passwd_field.clear()
        passwd_field.send_keys(passwd)
        self.find_element(SignupPageLocators.LOCATOR_SUBMIT_BUTTON).click()
