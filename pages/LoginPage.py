from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class LoginPage(BasePage):
    user_name_element = (By.XPATH, "//input[@name='username12']")
    password_element = (By.XPATH, "//input[@name='password']")

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.webelementEnter(self.user_name_element, username)
        self.webelementEnter(self.password_element, username)
