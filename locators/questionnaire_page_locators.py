from selenium.webdriver.common.by import By


class QuestionnairePageLocators:
    LOCATOR_NICE_TO_MEET_YOU_TEXT = (By.CSS_SELECTOR, ".css-yhxhb0")
    # LOCATOR_CLOSE_QUESTION_BUTTON = (By.CSS_SELECTOR, ".css-1k6v5wb >svg >path")
    LOCATOR_CLOSE_QUESTION_BUTTON = (By.XPATH, "//div[@id='__next']/div/div/section/div/div/a")
    LOCATOR_SUPPORTER_ROLE = (By.XPATH, "//span[text()='Supporter']")
    LOCATOR_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Submit']")
    LOCATOR_FIRST_NAME_FIELD = (By.NAME, "first_name_input")
    LOCATOR_BEST_FIELD = (By.CSS_SELECTOR, "#headlessui-listbox-button-1")
    LOCATOR_CHOOSE_KINDEST_LIST = (By.XPATH, "//div[text()='kindest']")
    LOCATOR_FRIEND_FIELD = (By.CSS_SELECTOR, "#headlessui-listbox-button-2")
    LOCATOR_CHOOSE_PARENT_LIST = (By.XPATH, "//div[text()='parent']")
    LOCATOR_GRADE_FIELD = (By.CSS_SELECTOR, "#headlessui-listbox-button-3")
    LOCATOR_CHOOSE_I_LIST = (By.XPATH, "//div[text()='I']")
    LOCATOR_TYPE_CANCER_FIELD = (By.CSS_SELECTOR, "#headlessui-listbox-button-4")
    LOCATOR_CHOOSE_BLADDER_LIST = (By.XPATH, "//div[text()='Bladder']")
