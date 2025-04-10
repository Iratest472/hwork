import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from calculator_class import Calculator


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    yield driver
    driver.quit()


def test_calculator(driver):
    calculator = Calculator(driver)
    calculator.set_delay(45)
    calculator.click_button('7')
    calculator.click_button('+')
    calculator.click_button('8')
    calculator.click_button('=')

    calculator.waiter = WebDriverWait(driver, 46)

    calculator.get_result('15')
