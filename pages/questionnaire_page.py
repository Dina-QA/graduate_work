from pages.base_page import BasePage
from locators.questionnaire_page_locators import QuestionnairePageLocators


class QuestionnairePage(BasePage):

    def should_be_questionnaire_page(self):
        nice_to_meet_you_text = self.find_element(QuestionnairePageLocators.LOCATOR_NICE_TO_MEET_YOU_TEXT)
        nice_to_meet_you_text.is_displayed()

    def choose_supporter_role(self):
        patient_button = self.find_element(QuestionnairePageLocators.LOCATOR_SUPPORTER_ROLE)
        patient_button.click()
        submit_button = self.find_element(QuestionnairePageLocators.LOCATOR_SUBMIT_BUTTON)
        submit_button.click()

    def fill_in_user_information(self):
        first_name_field = self.find_element(QuestionnairePageLocators.LOCATOR_FIRST_NAME_FIELD)
        first_name_field.click()
        first_name_field.send_keys("Gray")
        best_field = self.find_element(QuestionnairePageLocators.LOCATOR_BEST_FIELD)
        best_field.click()
        choose_kindest_list = self.find_element(QuestionnairePageLocators.LOCATOR_CHOOSE_KINDEST_LIST)
        choose_kindest_list.click()
        friend_field = self.find_element(QuestionnairePageLocators.LOCATOR_FRIEND_FIELD)
        friend_field.click()
        choose_parent_list = self.find_element(QuestionnairePageLocators.LOCATOR_CHOOSE_PARENT_LIST)
        choose_parent_list.click()
        grede_field = self.find_element(QuestionnairePageLocators.LOCATOR_GRADE_FIELD)
        grede_field.click()
        choose_i_list = self.find_element(QuestionnairePageLocators.LOCATOR_CHOOSE_I_LIST)
        choose_i_list.click()
        type_cancer_field = self.find_element(QuestionnairePageLocators.LOCATOR_TYPE_CANCER_FIELD)
        type_cancer_field.click()
        choose_bladder_list = self.find_element(QuestionnairePageLocators.LOCATOR_CHOOSE_BLADDER_LIST)
        choose_bladder_list.click()
        submit_button = self.find_element(QuestionnairePageLocators.LOCATOR_SUBMIT_BUTTON)
        submit_button.click()

    def close_questionnaire(self):
        close_button = self.find_element(QuestionnairePageLocators.LOCATOR_CLOSE_QUESTION_BUTTON)
        close_button.click()
