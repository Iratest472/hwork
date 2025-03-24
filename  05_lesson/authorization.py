from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

time.sleep(2)

username_search = driver.find_element(
    By.CSS_SELECTOR, 'input[name="username"]')
username_search.send_keys("tomsmith")

time.sleep(2)
password_search = driver.find_element(
    By.CSS_SELECTOR, 'input[name="password"]')
password_search.send_keys("SuperSecretPassword!")

time.sleep(3)

driver.find_element(By.CSS_SELECTOR, '.fa-sign-in').click()

time.sleep(2)
driver.quit()
