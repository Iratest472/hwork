from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Calculator:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.waiter = WebDriverWait(driver, 10)

    def set_delay(self, delay):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, button):
        self.driver.find_element(By.XPATH, f"//span[text() = '{button}']").click()

    def get_result(self, result):
        self.waiter.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), f"{result}"))

    def check_screen_result(self, expected_result: str):
        actual_result = self.element.text
        assert actual_result == expected_result, (
            f"Ожидается: '{expected_result}', Получено: '{actual_result}'"
        )
