from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    # 1. Открыть страницу
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # 2. Найти и нажать кнопку Start
    start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_button.click()

    # 3. Дождаться появления текста "Hello World!"
    wait = WebDriverWait(driver, 10)
    hello_element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    )

    # 4. Сделать скриншот
    driver.save_screenshot("dynamic_loading_result.png")

    # 5. Проверить текст
    assert hello_element.text == "Hello World!"

    driver.quit()
