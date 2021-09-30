from selenium.webdriver.common.by import By


class QuestionnairePageLocators:
    LOCATOR_NICE_TO_MEET_YOU_TEXT = (By.CSS_SELECTOR, ".css-yhxhb0")
    LOCATOR_CLOSE_QUESTION_BUTTON = (By.CSS_SELECTOR, ".css-1k6v5wb >svg >path")
    # LOCATOR_CLOSE_QUESTION_BUTTON = (By.XPATH, "/html/body/div[1]/div[1]/div/section/div/div/a/svg")
    LOCATOR_PATIENT_ROLE = (By.CSS_SELECTOR, ".css-1b5fxkk.e1hns8ek1")
