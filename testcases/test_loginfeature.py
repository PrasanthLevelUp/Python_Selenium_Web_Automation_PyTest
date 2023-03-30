import pytest

from conftest import Baseurl
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("browser")
class Test_login():

    def setup_class(self):
        self.driver.get(Baseurl)
        self.login_page = LoginPage(self.driver)

    def test_verifyTitle(self):
        self.login_page.login("Admin", "admin123")


    def teardown_class(self):
        self.driver.quit()

