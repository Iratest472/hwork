from selenium import webdriver
from selenium.webdriver.common.by import By


def test_shop():

    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    (driver.find_element(
        By.CSS_SELECTOR, 'input[id="user-name"]').
     send_keys('standard_user'))

    password_search = driver.find_element(
        By.CSS_SELECTOR, 'input[id="password"]')
    password_search.send_keys('secret_sauce')

    driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    driver.implicitly_wait(10)

    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    firstName = driver.find_element(
        By.CSS_SELECTOR, 'input[id="first-name"]')
    firstName.send_keys('Ирина')

    lastName = driver.find_element(
        By.CSS_SELECTOR, 'input[id="last-name"]')
    lastName.send_keys('Михейкина')

    zip = driver.find_element(
        By.CSS_SELECTOR, 'input[id="postal-code"]')
    zip.send_keys('490000')

    driver.find_element(By.CSS_SELECTOR, "#continue").click()

    total = driver.find_element(
        By.CSS_SELECTOR, 'div.summary_total_label').text
    assert total == 'Total: $58.29'

    driver.quit()
