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

select_date = "20-Dec-2022"

dates = select_date.split("-")

driver.find_element(By.ID, "onward_cal").click()

td = driver.find_elements(By.XPATH, "//div[@id='rb-calendar_onward_cal']//td")

for ele in td:
    if ele.text == dates[0]:
        ele.click()
        break






