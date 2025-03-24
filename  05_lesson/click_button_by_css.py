import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

time.sleep(2)

driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()

time.sleep(3)

driver.quit()
