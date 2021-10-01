from pages.base_page import BasePage
from locators.product_page_locators import ProductPageLocators
from time import sleep


class ProductPage(BasePage):
    def add_product_to_cart(self):
        add_to_cart_button = self.find_element(ProductPageLocators.LOCATOR_ADD_TO_CART_BUTTON)
        add_to_cart_button.click()
        sleep(3)
