from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chr_options)
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()

#Select class declaration with Webelement
select_web = driver.find_element(By.ID, 'Skills')

sel = Select(select_web)
#select by index
sel.select_by_index(5)
#select by value

sel.select_by_value('Configuration')

#select by visible text
sel.select_by_visible_text('Design')

print(driver.current_url)

#navigato different url
driver.get('https://www.google.com/')

print(driver.current_url)
#back
driver.back()

#refresh

driver.refresh()

#forward
driver.forward()

driver.quit()











