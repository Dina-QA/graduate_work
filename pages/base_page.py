from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = "https://ov_developer_user_852:3EDc8kb5nmuyxAWmEdx6QYhL5MQ2Ha@stage.onevillage.io/?1"

    def open_landing_page(self):
        self.driver.get(self.base_page)

    def find_element(self, locator: tuple, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can not find element by locator{locator}"
        )
