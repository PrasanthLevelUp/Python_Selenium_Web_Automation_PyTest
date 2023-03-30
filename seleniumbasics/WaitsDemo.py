from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
driver.get("https://demo.automationtesting.in/")
driver.implicitly_wait(3)
driver.maximize_window()

driver.find_element(By.ID,"email").send_keys("Test@gmail.com")
driver.find_element(By.ID,"enterimg").click()

# Wait Sleep
#time.sleep(2)



# Wait Implicit Wait - Implicitly waiting, WebDriver polls the DOM webpage
# where are not available immediately and need some time to load.
#driver.implicitly_wait(3)



# Wait Explicit Wait - hey allow your code to halt program execution,
# or freeze the thread, until the condition you pass it resolves.
# The condition is called with a certain frequency until the timeout of the wait is elapsed.
wait = WebDriverWait(driver,5)
wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@placeholder='First Name']"))).send_keys("Niharika")

