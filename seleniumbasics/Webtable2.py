import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import date

chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
driver.get("https://www.redbus.in/")
driver.implicitly_wait(3)
driver.maximize_window()

select_date = "14-Feb-2023"

date_list = select_date.split('-')

driver.find_element(By.XPATH, "//input[@id='onward_cal']").click()

current_month = driver.find_element(By.XPATH, "//td[@class='monthTitle']").text

next = driver.find_element(By.XPATH, "//td[@class='next']/button")

flag = True

while flag:
    if date_list[1] in current_month:
        flag = False
    else:
        driver.find_element(By.XPATH, "//td[@class='next']/button").click()
        time.sleep(2)
        current_month = driver.find_element(By.XPATH, "//td[@class='monthTitle']").text

dates = driver.find_elements(By.XPATH, "//div[@id='rb-calendar_onward_cal']//td")

for i in dates:
    if i.text == date_list[0]:
        i.click()
        break






