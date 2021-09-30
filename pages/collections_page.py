from pages.base_page import BasePage
from locators.collections_page_locators import CollectionsPageLocators


class CollectionsPage(BasePage):

    def should_be_collections_page(self):
        check_text_collections_page = 'Collections'
        title_text = self.find_element(CollectionsPageLocators.LOCATOR_TITLE_PAGE_TEXT).text
        assert title_text == check_text_collections_page, f"{title_text} is not equal to {check_text_collections_page}"

    def open_meal_delivery_section(self):
        meal_delivery_section = self.find_element(CollectionsPageLocators.LOCATOR_MEAL_DELIVERY_SECTION)
        meal_delivery_section.click()

