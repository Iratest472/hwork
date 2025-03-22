import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get(" http://the-internet.herokuapp.com/add_remove_elements/")

button = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')
button.click()
button.click()
button.click()
button.click()
button.click()

time.sleep(5)

delete = driver.find_elements(
    By.CSS_SELECTOR, 'Button[onclick="deleteElement()"]')

print(len(delete))
