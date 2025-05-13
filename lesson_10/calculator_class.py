from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Calculator:
    """Класc для взаимодействия с онлайн-калькулятором."""

    def __init__(self, driver):
        """
        Инициализация объекта калькулятора.

        :param driver: Экземпляр веб-драйвера Selenium.
        """
        self.driver = driver  # Связываем объект Selenium с нашим объектом
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")  # Загружаем страницу калькулятора
        self.waiter = WebDriverWait(driver, 10)  # Устанавливаем таймер ожидания (до 10 секунд)

    def set_delay(self, delay):
        """
        Изменяет задержку обработки операций калькулятора.

        :param delay: Целое число, определяющее количество миллисекунд задержки.
        """
        delay_input = self.driver.find_element(By.ID, "delay")  # Найти элемент поля задержки
        delay_input.clear()  # Очистить предыдущее значение
        delay_input.send_keys(str(delay))  # Отправляем новое значение задержки

    def click_button(self, button):
        """
        Симулирует нажатие кнопки на калькуляторе.

        :param button: Текст кнопки (например, цифры, операторы, знаки "=").
        """
        self.driver.find_element(By.XPATH, f"//span[text()='{button}']").click()  # Кликаем по соответствующей кнопке

    def get_result(self, result):
        """
        Ожидает и проверяет результат вычисления на экране калькулятора.
        :param result: Результат вычисления, который нужно дождаться.
        """
        self.waiter.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.screen'), f'{result}')
        )  # Ждет, пока результат не появится на экране

    def check_screen_result(self, expected_result: str):
        """
        Проверяет совпадение текущего результата на экране с ожидаемым.
        :param expected_result: Ожидаемый результат на экране калькулятора.
        """
        actual_result = self.driver.find_element(By.CSS_SELECTOR, '.screen').text  # Текущий результат на экране
        assert actual_result == expected_result, (  # Утверждение
            f"Ожидается: '{expected_result}', Получено: '{actual_result}'"
        )