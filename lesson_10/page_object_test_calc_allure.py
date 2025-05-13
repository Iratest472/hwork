import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure


class Calculator:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.waiter = WebDriverWait(driver, 10)

    @allure.step("Установка задержки: {delay} мс")
    def set_delay(self, delay):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    @allure.step("Нажатие кнопки: {button}")
    def click_button(self, button):
        self.driver.find_element(By.XPATH, f"//span[text() = '{button}']").click()

    @allure.step("Ожидание результата: {result}")
    def get_result(self, result):
        self.waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), f"{result}"))

    @allure.step("Проверка результата на экране")
    def check_screen_result(self, expected_result: str):
        actual_result = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        assert actual_result == expected_result, (
            f"Ожидается: '{expected_result}', Получено: '{actual_result}'"
        )


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title("Проверка расчёта 7 + 8 на калькуляторе")
@allure.description("Проведение простого расчёта 7 + 8 и проверка результата на экране калькулятора.")
@allure.feature("Расчёты на калькуляторе")
@allure.severity(allure.severity_level.MINOR)
def test_calculation(driver):
    with allure.step("Создание экземпляра калькулятора"):
        calc = Calculator(driver)

    with allure.step("Задание задержки на калькуляторе"):
        calc.set_delay(45)

    with allure.step("Ввод выражения 7 + 8"):
        calc.click_button('7')
        calc.click_button('+')
        calc.click_button('8')
        calc.click_button('=')

    with allure.step("Ожидание результата вычисления"):
        calc.get_result('15')

    with allure.step("Проверка правильного результата"):
        calc.check_screen_result('15')