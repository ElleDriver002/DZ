from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    try:
        wait = WebDriverWait(driver, 50)
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

        delay_input = wait.until(
            EC.presence_of_element_located((By.ID, "delay"))
        )
        delay_input.clear()
        delay_input.send_keys("45")

        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        result = wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, "div.screen"), "15"
            )
        )
        assert result is True
        assert driver.find_element(
            By.CSS_SELECTOR, "div.screen"
        ).text == "15"
    finally:
        driver.quit()
