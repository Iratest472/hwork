import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from calculator_class import Calculator


#  Фикстура для запуска и остановки браузера
# Используется PyTest-функция @pytest.fixture для автоматического открытия/закрытия браузера
@pytest.fixture()
def driver():
    """
    Фикстура для инициализации и завершения сеанса работы с браузером.

    Эта фикстура запускает браузер Chrome, разворачивает окно на весь экран,
    загружает нужную страницу и освобождает ресурсы после завершения тестов.
    """
    driver = webdriver.Chrome()  # Запускаем браузер Chrome
    driver.maximize_window()  # Разворачиваем окно браузера на весь экран
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")  # Открываем сайт с калькулятором
    yield driver  # Передача контроля обратно в тестовые функции
    driver.quit()  # Завершаем работу браузера после окончания тестов


#  Основной тестовый метод
def test_calculator(driver):
    """
    Тестирование функционала калькулятора.

    :param driver: Драйвер браузера, предоставляемый фикстурой driver().
    """
    calculator = Calculator(driver)  # Создаем экземпляр класса Calculator
    calculator.set_delay(45)  # Задерживаем ввод цифр на 45 секунд (для симуляции медленных устройств)
    calculator.click_button('7')  # Нажимаем цифру 7
    calculator.click_button('+')  # Нажимаем знак сложения +
    calculator.click_button('8')  # Нажимаем цифру 8
    calculator.click_button('=')  # Нажимаем знак равенства =

    # Ждем до 46 секунд пока появится результат вычисления
    calculator.waiter = WebDriverWait(driver, 46)

    # Проверяем, что результат совпадает с ожидаемым (15)
    calculator.get_result('15')