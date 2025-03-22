from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")


for _ in range(5):
    driver.find_element(
        By.CSS_SELECTOR, 'button[onclick="addElement()"]').click()


delete_buttons = driver.find_elements(
    By.CSS_SELECTOR, 'button[onclick="deleteElement()"]')
print(f"Количество кнопок 'Delete': {len(delete_buttons)}")
