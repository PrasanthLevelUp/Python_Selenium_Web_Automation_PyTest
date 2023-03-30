from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()

driver.find_element(By.ID,'OKTab').click()

time.sleep(2)

#ok - accept

driver.switch_to.alert.accept()

# confrimation

driver.find_element(By.XPATH,"//a[@href='#CancelTab']").click()

driver.find_element(By.ID,'CancelTab').click()
time.sleep(2)
driver.switch_to.alert.dismiss()

#text

driver.find_element(By.XPATH,"//a[@href='#Textbox']").click()

driver.find_element(By.ID,'Textbox').click()
time.sleep(2)
tx = driver.switch_to.alert.text
print(tx)
driver.switch_to.alert.send_keys("Test")
driver.switch_to.alert.dismiss()
time.sleep(2)
driver.quit()
