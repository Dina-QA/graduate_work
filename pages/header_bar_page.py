from pages.base_page import BasePage
from locators.heade_bar_page_locators import HeaderBarLocators


class HeaderBarPage(BasePage):

    def log_out(self):
        menu_drop_down = self.find_element(HeaderBarLocators.LOCATOR_MENU_DROP_DOWN)
        menu_drop_down.click()
        log_out_button = self.find_element(HeaderBarLocators.LOCATOR_LOGOUT_BUTTON)
        log_out_button.click()

    def open_cart_page(self):
        cart_icon = self.find_element(HeaderBarLocators.LOCATOR_CART_BUTTON)
        cart_icon.click()
