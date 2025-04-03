from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    first_name = driver.find_element(
        By.CSS_SELECTOR, 'input[name="first-name"]')
    first_name.send_keys("Иван")
    last_name = driver.find_element(
        By.CSS_SELECTOR, 'input[name="last-name"]')
    last_name.send_keys("Петров")
    address = driver.find_element(
        By.CSS_SELECTOR, 'input[name="address"]')
    address.send_keys("Ленина, 55-3")
    email = driver.find_element(
        By.CSS_SELECTOR, 'input[name="e-mail"]')
    email.send_keys("test@skypro.com")
    phone_number = driver.find_element(
        By.CSS_SELECTOR, 'input[name="phone"]')
    phone_number.send_keys("+7985899998787")
    city_s = driver.find_element(
        By.CSS_SELECTOR, 'input[name="city"]')
    city_s.send_keys("Москва")
    country_a = driver.find_element(
        By.CSS_SELECTOR, 'input[name="country"]')
    country_a.send_keys("Россия")
    jobs_position = driver.find_element(
        By.CSS_SELECTOR, 'input[name="job-position"]')
    jobs_position.send_keys("QA")
    company_s = driver.find_element(
        By.CSS_SELECTOR, 'input[name="company"]')
    company_s.send_keys("SkyPro")

    driver.implicitly_wait(10)

    driver.find_element(
        By.CSS_SELECTOR, '.btn-outline-primary').click()

    zip_color = (driver.find_element(
        By.CSS_SELECTOR,
        "#zip-code.alert-danger").
                 value_of_css_property("background-color"))
    assert (zip_color == "rgba(248, 215, 218, 1)"), \
        "Результат не равен 'rgba(248, 215, 218, 1)'"

    name_color = (driver.find_element(
        By.CSS_SELECTOR, "#first-name.alert-success")
                  .value_of_css_property("background-color"))
    assert (name_color ==
            "rgba(209, 231, 221, 1)"), \
        "Результат не равен 'rgba(209, 231, 221, 1)'"

    last_color = (driver.find_element(
        By.CSS_SELECTOR, "#last-name.alert-success").
                  value_of_css_property("background-color"))
    assert (last_color ==
            "rgba(209, 231, 221, 1)"), \
        "Результат не равен 'rgba(209, 231, 221, 1)'"

    address_color = (driver.find_element(
        By.CSS_SELECTOR, "#address.alert-success").
                     value_of_css_property("background-color"))
    assert address_color == "rgba(209, 231, 221, 1)", \
        "Результат не равен 'rgba(209, 231, 221, 1)'"

    city_color = (driver.find_element(
        By.CSS_SELECTOR, "#city.alert-success").
                  value_of_css_property("background-color"))
    assert city_color == "rgba(209, 231, 221, 1)", \
        "Результат не равен 'rgba(209, 231, 221, 1)'"

    country_color = (driver.find_element(
        By.CSS_SELECTOR, "#country.alert-success").
                     value_of_css_property("background-color"))
    assert country_color == "rgba(209, 231, 221, 1)", \
        "Результат не равен 'rgba(209, 231, 221, 1)'"

    email_color = (driver.find_element(
        By.CSS_SELECTOR, "#e-mail.alert-success").
                   value_of_css_property("background-color"))
    assert email_color == "rgba(209, 231, 221, 1)", \
        "Результат не равен 'rgba(209, 231, 221, 1)'"

    phone_color = (driver.find_element(
        By.CSS_SELECTOR, "#phone.alert-success").
                   value_of_css_property("background-color"))
    assert phone_color == "rgba(209, 231, 221, 1)", \
        "Результат не равен 'rgba(209, 231, 221, 1)'"

    job_color = (driver.find_element(
        By.CSS_SELECTOR, "#job-position.alert-success").
                 value_of_css_property("background-color"))
    assert job_color == "rgba(209, 231, 221, 1)", \
        "Результат не равен 'rgba(209, 231, 221, 1)'"

    company_color = (driver.find_element(
        By.CSS_SELECTOR, "#company.alert-success").
                     value_of_css_property("background-color"))
    assert company_color == "rgba(209, 231, 221, 1)", \
        "Результат не равен 'rgba(209, 231, 221, 1)'"

    driver.quit()
