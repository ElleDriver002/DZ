from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    driver.get("https://httpbin.qa-territory.online")
    start_url = driver.current_url

    link = driver.find_element(By.LINK_TEXT, "HTML Form")
    link.click()

    assert "/forms/post" in driver.current_url

    driver.back()

    assert driver.current_url == start_url

    driver.quit()
