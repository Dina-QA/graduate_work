from pages.base_page import BasePage
from locators.product_list_page_locators import ProductListPageLocators


class ProductListPage(BasePage):
    def should_be_product_list_page(self):
        check_text_product_list_page = "Meal Delivery"
        title_text = self.find_element(ProductListPageLocators.LOCATOR_TITLE_PAGE_TEXT).text
        assert title_text == check_text_product_list_page, f"{title_text} is not equal to {check_text_product_list_page}"

    def open_product_page(self):
        sunbasket_gift_credit_product = self.find_element(ProductListPageLocators.LOCATOR_SUNBASKET_GIFT_CREDIT_PRODUCT)
        sunbasket_gift_credit_product.click()
