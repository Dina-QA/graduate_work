from pages.base_page import BasePage
from locators.cart_page_locators import CartPageLocators


class CartPage(BasePage):
    def open_collections(self):
        get_started_button = self.find_element(CartPageLocators.LOCATOR_GET_STARTED_BUTTON)
        get_started_button.click()

    def check_product_in_cart(self):
        name_product = 'Sunbasket Gift Credit'
        sunbasket_gift_credit_product = self.find_element(CartPageLocators.LOCATOR_NAME_PRODUCT_TEXT).text
        assert sunbasket_gift_credit_product == name_product, f"{sunbasket_gift_credit_product} is not equal to {name_product}"

    def check_cart_is_empty(self):
        text_on_page = "Your Cart is Empty"
        cart_is_empty_text = self.find_element(CartPageLocators.LOCATOR_CART_IS_EMPTY_TEXT).text
        assert cart_is_empty_text == text_on_page, f"{cart_is_empty_text} is not equal to {text_on_page}"
