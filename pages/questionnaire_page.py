from pages.base_page import BasePage
from locators.questionnaire_page_locators import QuestionnairePageLocators
from time import sleep

class QuestionnairePage(BasePage):

    def should_be_questionnaire_page(self):
        nice_to_meet_you_text = self.find_element(QuestionnairePageLocators.LOCATOR_NICE_TO_MEET_YOU_TEXT)
        nice_to_meet_you_text.is_displayed()

    def close_questionnaire(self):
        sleep(2)
        close_button = self.find_element(QuestionnairePageLocators.LOCATOR_CLOSE_QUESTION_BUTTON)
        print("check close button %s"% close_button.is_displayed())
        close_button.click()
        sleep(10)

    def choose_patient_role(self):
        patient_button = self.find_element(QuestionnairePageLocators.LOCATOR_PATIENT_ROLE)
        patient_button.click()
