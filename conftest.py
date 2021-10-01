from selenium import webdriver
import pytest
# from api.api import Api
import allure


# @pytest.fixture()
# @allure.feature("User can login/logout in the system")
# def login_api():
#     with allure.step("Check user can login in the system"):
#         api = Api()
#         api.login("dina@onevillage.io", "1234567890_OV")
#         yield api
#     with allure.step("Check user can logout in the system"):
#         api.logout()


# @pytest.fixture()
# def browser():
#     driver = webdriver.Chrome("./chromedriver 5")
#     driver.maximize_window()
#     driver.implicitly_wait(3)
#     yield driver
#     driver.quit()

@pytest.fixture()
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.failed:
        try:
            if 'browser' in item.fixturenames:
                browser = item.funcargs['browser']
            else:
                print('Does not have browser fixture')
                return
            allure.attach(browser.get_screenshot_as_png(), "Screenshot", attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(f"Failed to make screenshot: {e}")
