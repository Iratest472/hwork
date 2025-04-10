from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Shop:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.waiter = WebDriverWait(driver, 10)

    def enter_username(self, username):
        self.driver.find_element(By.CSS_SELECTOR, 'input[id="user-name"]').send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, 'input[id="password"]').send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    def add_items_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

    def get_checkout_button(self):
        self.waiter.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout"))).click()

    def fill_first_name(self, first_name):
        first_name_field = self.driver.find_element(By.CSS_SELECTOR, 'input[id="first-name"]')
        first_name_field.send_keys(first_name)

    def fill_last_name(self, last_name):
        last_name_field = self.driver.find_element(By.CSS_SELECTOR, 'input[id="last-name"]')
        last_name_field.send_keys(last_name)

    def fill_zip(self, zip):
        zip_field = self.driver.find_element(By.CSS_SELECTOR, 'input[id="postal-code"]')
        zip_field.send_keys(zip)

    def click_continue_button(self):
        self.driver.find_element(By.CSS_SELECTOR, "#continue").click()

    def check_total_amount(self,  expected_total: str):
        actual_total = self.driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
        assert actual_total == expected_total, (
            f"Ожидается: '{expected_total}', Получено: '{actual_total}'")
