import allure
from api.api import Api


@allure.feature("Check user exist in the system by e-mail, Reset password")
def test_api_scenario():
    with allure.step("Check user can log in to the system"):
        api = Api()
        api.login("dina@onevillage.io", "1234567890_OV")
    with allure.step("Check user exist in the system by e-mail"):
        api.check_user_exist("dina@onevillage.io")
    with allure.step("User can reset password"):
        api.reset_password("dina@onevillage.io")
    with allure.step("Check user can logout from the system"):
        api.logout()
