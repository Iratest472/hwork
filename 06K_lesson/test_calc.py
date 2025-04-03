from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():

    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = driver.find_element(
        By.CSS_SELECTOR, 'input[id="delay"]')
    delay_input.clear()
    delay_input.send_keys('45')

    driver.implicitly_wait(10)

    seven = driver.find_element(
        By.XPATH, "//span[@class='btn btn-outline-primary' and text()='7']")
    seven.click()
    plus = driver.find_element(
        By.XPATH,
        "//span[@class='operator btn btn-outline-success' and text()='+']")
    plus.click()
    eight = driver.find_element(
        By.XPATH, "//span[@class='btn btn-outline-primary' and text()='8']")
    eight.click()
    equally = driver.find_element(
        By.XPATH, "//span[@class='btn btn-outline-warning' and text()='=']")
    equally.click()
    waiter = WebDriverWait(driver, 46)

    waiter.until(EC.text_to_be_present_in_element((
        By.CSS_SELECTOR, ".screen"), "15"))

    res = driver.find_element(By.CSS_SELECTOR, '.screen').text
    assert res == '15', "Результат не равен 15"

    driver.quit()
