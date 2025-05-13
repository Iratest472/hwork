from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Shop:

    def __init__(self, driver):
        """
        Инициализируем экземпляр класса Shop.

        :param driver: драйвер Selenium (например, Chrome или Firefox)
        """
        self.driver = driver  # Привязываем драйвер к полю класса
        self.driver.get("https://www.saucedemo.com/")  # Открываем стартовую страницу магазина
        self.waiter = WebDriverWait(driver, 10)  # Создаем объект ожидания длительностью 10 секунд

    def enter_username(self, username):
        """
        Вводим имя пользователя в соответствующее поле.

        :param username: имя пользователя (логин)
        """
        input_field = self.driver.find_element(By.CSS_SELECTOR, 'input[id="user-name"]')
        input_field.send_keys(username)  # Вводим имя пользователя

    def enter_password(self, password):
        """
        Вводим пароль в соответствующее поле.

        :param password: пароль пользователя
        """
        input_field = self.driver.find_element(By.CSS_SELECTOR, 'input[id="password"]')
        input_field.send_keys(password)  # Вводим пароль

    def click_login_button(self):
        """
        Нажимаем кнопку входа (Login).
        """
        login_btn = self.driver.find_element(By.CSS_SELECTOR, '#login-button')
        login_btn.click()  # Нажимаем кнопку Login

    def add_items_to_cart(self):
        """
        Добавляем несколько товаров в корзину.
        """
        # Нажимаем кнопку добавления рюкзака в корзину
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        # Нажимаем кнопку добавления футболки Bolt T-Shirt в корзину
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        # Нажимаем кнопку добавления Onesie в корзину
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        # Перейти в корзину
        cart_icon = self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
        cart_icon.click()

    def get_checkout_button(self):
        """
        Нажимаем кнопку Checkout (оформление заказа).
        """
        checkout_btn = self.waiter.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout")))
        checkout_btn.click()  # Нажимаем кнопку Checkout

    def fill_first_name(self, first_name):
        """
        Заполняем поле "First Name" (имя).

        :param first_name: первое имя пользователя
        """
        field = self.driver.find_element(By.CSS_SELECTOR, 'input[id="first-name"]')
        field.send_keys(first_name)  # Вводим имя

    def fill_last_name(self, last_name):
        """
        Заполняем поле "Last Name" (фамилия).

        :param last_name: фамилия пользователя
        """
        field = self.driver.find_element(By.CSS_SELECTOR, 'input[id="last-name"]')
        field.send_keys(last_name)  # Вводим фамилию

    def fill_zip(self, zip):
        """
        Заполняем поле ZIP Code (почтовый индекс).

        :param zip: почтовый индекс пользователя
        """
        field = self.driver.find_element(By.CSS_SELECTOR, 'input[id="postal-code"]')
        field.send_keys(zip)  # Вводим почтовый индекс

    def click_continue_button(self):
        """
        Нажимаем кнопку Continue (продолжить).
        """
        btn = self.driver.find_element(By.CSS_SELECTOR, "#continue")
        btn.click()  # Нажимаем кнопку Продолжить

    def check_total_amount(self, expected_total: str):
        """
        Проверяем итоговую сумму заказа.

        :param expected_total: ожидаемая итоговая сумма
        """
        summary = self.driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label')
        actual_total = summary.text  # Берем реальную сумму заказа
        assert actual_total == expected_total, \
            f"Итоговая сумма неверна!\nОжидалось: {expected_total}\nПолучилось: {actual_total}"  # Проверьте итоговую сумму