# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
#
#
# @pytest.fixture(scope="module")
# def launchbroswer():
#     chr_options = Options()
#     chr_options.add_experimental_option("detach", True)
#     global driver
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
#     yield
#     driver.quit()
#
#
# @pytest.fixture(scope="class")
# def launchbroswerclass(request):
#     chr_options = Options()
#     chr_options.add_experimental_option("detach", True)
#     request.cls.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chr_options)
#     yield
#     request.cls.driver.quit()
#
#
# def test_printUrl(launchbroswer):
#     driver.get("https://www.redbus.in/")
#
#
# def test_printUrl2(launchbroswer):
#     print(driver.current_url)
#
#
# @pytest.mark.usefixtures("launchbroswerclass")
# class Test_Redbus:
#     def test_entertheURl(self):
#         self.driver.get("https://www.redbus.in/")