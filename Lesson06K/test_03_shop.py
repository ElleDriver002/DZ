from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def test_shop_purchase():
    options = webdriver.FirefoxOptions()
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)

    try:
        wait = WebDriverWait(driver, 15)
        driver.get("https://www.saucedemo.com/")

        # Авторизация
        wait.until(
            EC.presence_of_element_located((By.ID, "user-name"))
        ).send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Добавление товаров
        for item in [
            "sauce-labs-backpack",
            "sauce-labs-bolt-t-shirt",
            "sauce-labs-onesie",
        ]:
            btn = wait.until(
                EC.element_to_be_clickable(
                    (By.ID, f"add-to-cart-{item}")
                )
            )
            btn.click()

        # Корзина
        wait.until(
            EC.element_to_be_clickable(
                (By.CLASS_NAME, "shopping_cart_link")
            )
        ).click()

        # Checkout
        wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

        # Форма
        wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        ).send_keys("Ivan")
        driver.find_element(By.ID, "last-name").send_keys("Petrov")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        driver.find_element(By.ID, "continue").click()

        # Проверка Total
        total_element = wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        assert "$58.29" in total_element.text
    finally:
        driver.quit()
