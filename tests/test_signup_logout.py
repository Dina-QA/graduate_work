from pages.landing_page import LandingPage
from pages.signup_page import SignupPage
from pages.questionnaire_page import QuestionnairePage
from pages.fridge_door_page import FridgeDoorPage
from pages.header_bar_page import HeaderBarPage
from pages.login_page import LoginPage
import allure
import random


@allure.feature("Check user can Sign Up in the system with valid data")
def test_signup_in_the_system(browser):
    firstname = 'Dina'
    lastname = 'Smith'
    email = f"dina+{random.randint(0, 500)}@onevillage.io"
    passwd = "1234567890_OV"
    with allure.step("Open Landing page"):
        landing_page = LandingPage(browser)
        landing_page.open_landing_page()
    with allure.step("Open Sing Up page"):
        landing_page.open_signup_page()
    with allure.step("Check Sign Up page displays"):
        signup_page = SignupPage(browser)
        signup_page.should_be_signup_page()
    with allure.step("Sign Up user in the system"):
        signup_page.signup(firstname, lastname, email, passwd)
    with allure.step("Close the questionnaire"):
        questionnaire_page = QuestionnairePage(browser)
        questionnaire_page.choose_patient_role()
        questionnaire_page.should_be_questionnaire_page()
        questionnaire_page.close_questionnaire()
    with allure.step("Check Fridge door page is open"):
        fridge_door_page = FridgeDoorPage(browser)
        fridge_door_page.should_be_fridge_page()
    with allure.step("Log Out user from the system"):
        header_bar_page = HeaderBarPage(browser)
        header_bar_page.log_out()
    with allure.step("Check Landing page is open"):
        landing_page.should_be_landing_page()
    with allure.step("Open Log In page"):
        landing_page.open_login_page()
    with allure.step("Check Log In page displays"):
        login_page = LoginPage(browser)
        login_page.should_be_login_page()
    with allure.step("Log In user to the system"):
        login_page.login(email, passwd)
    with allure.step("Close the questionnaire"):
        questionnaire_page.should_be_questionnaire_page()
        questionnaire_page.close_questionnaire()
    with allure.step("Check Fridge door page is open"):
        fridge_door_page.should_be_fridge_page()
