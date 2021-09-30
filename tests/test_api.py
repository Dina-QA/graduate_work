import allure


@allure.feature(" Check user exist in the system by e-mail, Reset password")
def test_api_scenario(login_api):
    with allure.step("Check user exist in the system by e-mail"):
        login_api.check_user_exist("dina@onevillage.io")
    with allure.step("User can reset password"):
        login_api.reset_password("dina@onevillage.io")
