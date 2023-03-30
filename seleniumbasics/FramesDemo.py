from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

# SwitchTo Frames Window
# Using Index

#driver.switch_to.frame(0)

# Using name or id

driver.switch_to.frame("singleframe") # id
#driver.switch_to.frame("SingleFrame") # name

# Using web element
#single_frame = driver.find_element(By.XPATH, "//div[@id='Single']/iframe" )
#driver.switch_to.frame(single_frame)

text = driver.find_element(By.TAG_NAME, "input")

text.send_keys("This is text box")
# Return to home default

driver.switch_to.default_content()

