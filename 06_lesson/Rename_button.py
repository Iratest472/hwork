from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

input_search = driver.find_element(
    By.CSS_SELECTOR, 'input[id="newButtonName"]')
input_search.send_keys("Skypro")

driver.implicitly_wait(10)

button = driver.find_element(
    By.CSS_SELECTOR, '.btn-primary')
button.click()

element = WebDriverWait (driver, 15).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn-primary'))).text

print('SkyPro')