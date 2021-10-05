from pages.base_page import BasePage
from locators.londing_page_locators import LandingPageLocators


class LandingPage(BasePage):

    def should_be_landing_page(self):
        self.elements_are_present_at_landing_page()

    def elements_are_present_at_landing_page(self):
        check_text_landing_page = "Let’s build your cancer team"
        title_text = self.find_element(LandingPageLocators.LOCATOR_TITLE_TEXT)
        assert title_text == check_text_landing_page, f"{title_text} is not equal to {check_text_landing_page}"

    def open_signup_page(self):
        get_started_button = self.find_element(LandingPageLocators.LOCATOR_GET_STARTED_BUTTON)
        get_started_button.click()

    def open_login_page(self):
        log_in_button = self.find_element(LandingPageLocators.LOCATOR_LOGIN_BUTTON)
        log_in_button.click()
