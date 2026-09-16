from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Иван")

    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
    submit_button.click()

    assert driver.current_url != "https://httpbin.qa-territory.online/forms/post"

    driver.quit()
