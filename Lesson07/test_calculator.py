from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.calculator_page import CalculatorPage


def test_slow_calculator():
    """
    Test the slow calculator:
    - Set delay to 45 seconds
    - Press 7 + 8 =
    - Assert result is 15 after the delay
    """
    options = Options()
    # Раскомментируйте при необходимости headless-режима:
    # options.add_argument("--headless")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options,
    )

    try:
        page = CalculatorPage(driver)
        page.open()
        page.set_delay(45)
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

        result = page.get_result(timeout=50)
        assert result == "15", f"Expected result 15, got '{result}'"
    finally:
        driver.quit()


if __name__ == "__main__":
    test_slow_calculator()
    print("Calculator test passed")
