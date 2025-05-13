import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from shop_class import Shop
import allure

# Аннотируем класс Shop методами с использованием декоратора @allure.step
class Shop:

    @allure.step("Открыть страницу магазина")
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.waiter = WebDriverWait(driver, 10)

    @allure.step("Ввести имя пользователя: {username}")
    def enter_username(self, username):
        self.driver.find_element(by=By.CSS_SELECTOR, value='input[id="user-name"]').send_keys(username)

    @allure.step("Ввести пароль: {password}")
    def enter_password(self, password):
        self.driver.find_element(by=By.CSS_SELECTOR, value='input[id="password"]').send_keys(password)

    @allure.step("Нажать кнопку Вход")
    def click_login_button(self):
        self.driver.find_element(by=By.CSS_SELECTOR, value='#login-button').click()

    @allure.step("Добавить товары в корзину")
    def add_items_to_cart(self):
        self.driver.find_element(by=By.CSS_SELECTOR, value="#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(by=By.CSS_SELECTOR, value="#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(by=By.CSS_SELECTOR, value="#add-to-cart-sauce-labs-onesie").click()
        self.driver.find_element(by=By.CSS_SELECTOR, value=".shopping_cart_link").click()

    @allure.step("Перейти к оформлению заказа")
    def get_checkout_button(self):
        checkout_button = self.waiter.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout")))
        checkout_button.click()

    @allure.step("Заполнить имя: {first_name}")
    def fill_first_name(self, first_name):
        first_name_field = self.driver.find_element(by=By.CSS_SELECTOR, value='input[id="first-name"]')
        first_name_field.send_keys(first_name)

    @allure.step("Заполнить фамилию: {last_name}")
    def fill_last_name(self, last_name):
        last_name_field = self.driver.find_element(by=By.CSS_SELECTOR, value='input[id="last-name"]')
        last_name_field.send_keys(last_name)

    @allure.step("Заполнить почтовый индекс: {zip}")
    def fill_zip(self, zip):
        zip_field = self.driver.find_element(by=By.CSS_SELECTOR, value='input[id="postal-code"]')
        zip_field.send_keys(zip)

    @allure.step("Продолжить оформление заказа")
    def click_continue_button(self):
        self.driver.find_element(by=By.CSS_SELECTOR, value="#continue").click()

    @allure.step("Проверить итоговую сумму: {expected_total}")
    def check_total_amount(self, expected_total: str):
        total_label = self.driver.find_element(by=By.CSS_SELECTOR, value='div.summary_total_label')
        actual_total = total_label.text
        with allure.step(f"Проверь итоговую сумму ({expected_total})"):
            assert actual_total == expected_total, f"Ожидалось: '{expected_total}', Получили: '{actual_total}'"


# Декорируем тест необходимыми атрибутами Allure
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.feature("Оформление заказа")
@allure.story("Покупка товаров и проверка итоговой суммы")
@allure.title("Корректность итоговой суммы при оформлении заказа")
@allure.description("Тест проверяет покупку трех товаров и итоговую сумму при оформлении заказа.")
@allure.severity(allure.severity_level.NORMAL)
def test_shop_order(driver):
    with allure.step("Создание экземпляра класса Shop"):
        shop = Shop(driver)

    with allure.step("Авторизация пользователя"):
        shop.enter_username('standard_user')
        shop.enter_password('secret_sauce')
        shop.click_login_button()

    with allure.step("Добавление товаров в корзину"):
        shop.add_items_to_cart()

    with allure.step("Начало оформления заказа"):
        shop.get_checkout_button()

    with allure.step("Заполнение личных данных"):
        shop.fill_first_name('Ирина')
        shop.fill_last_name('Михейкина')
        shop.fill_zip('490000')

    with allure.step("Продолжение оформления заказа"):
        shop.click_continue_button()

    with allure.step("Проверка итоговой суммы"):
        shop.check_total_amount('Total: $58.29')
