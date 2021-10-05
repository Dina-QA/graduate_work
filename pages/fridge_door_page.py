import allure
from pages.base_page import BasePage
from locators.fridge_door_page_locators import FridgeDoorPageLocators
from allure_commons.types import AttachmentType


class FridgeDoorPage(BasePage):

    def should_be_fridge_page(self):
        self.elements_are_present_at_fridge_page()

    def elements_are_present_at_fridge_page(self):
        # allure.attach(
        #     self.driver.get_screenshot_as_png(),
        #     name="pns",
        #     attachment_type=AttachmentType.PNG
        # )
        name_user = "Dina"
        check_text_fridge_page = f"👋 {name_user}, welcome to OneVillage!"
        welcome_text = self.find_element(FridgeDoorPageLocators.LOCATOR_WELCOME_AFTER_CLOSE_QUESTION_TEXT).text
        print(welcome_text)
        assert welcome_text == check_text_fridge_page, f"{welcome_text} is not equal to {check_text_fridge_page} "

