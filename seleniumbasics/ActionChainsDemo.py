import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
driver.get("https://magento.softwaretestingboard.com/")
driver.implicitly_wait(3)
driver.maximize_window()

#  ActionChains - mouse movements, mouse button actions, keypress, and context menu interactions

women = driver.find_element(By.XPATH, "//a[@id='ui-id-4']")

action = ActionChains(driver)

action.move_to_element(women).perform()

tops = driver.find_element(By.XPATH, "//a[@id='ui-id-9']")

action.move_to_element(tops).perform()

jackets = driver.find_element(By.XPATH, "//a[@id='ui-id-11']")

action.click(jackets).perform()

time.sleep(3)

search = driver.find_element(By.ID, "search")

action.click(search).key_down(Keys.SHIFT).send_keys("Test").key_up(Keys.SHIFT).send_keys(Keys.ENTER).perform()

print(driver.get_screenshot_as_base64())