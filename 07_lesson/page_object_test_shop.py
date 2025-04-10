import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from shop_class import Shop


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_calculator(driver):
    shop = Shop(driver)
    shop.enter_username('standard_user')
    shop.enter_password('secret_sauce')
    shop.click_login_button()
    shop.add_items_to_cart()
    shop.waiter = WebDriverWait(driver, 46)
    shop.get_checkout_button()
    shop.fill_first_name('Ирина')
    shop.fill_last_name('Михейкина')
    shop.fill_zip('490000')
    shop.click_continue_button()
    shop.check_total_amount('Total: $58.29')
