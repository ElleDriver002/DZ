"""Tests for the slow calculator page."""

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from pages.calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Сложение 7 + 8 на медленном калькуляторе")
@allure.description(
    "Устанавливает задержку 45 секунд, выполняетет 7 + 8 = "
    "и проверяет, что результат равен 15."
)
def test_slow_calculator(chrome_driver: WebDriver) -> None:
    """
    Test the slow calculator:
    - Set delay to 45 seconds
    - Press 7 + 8 =
    - Assert result is 15 after the delay
    """
    page = CalculatorPage(chrome_driver)

    with allure.step("Открыть страницу калькулятора"):
        page.open()

    with allure.step("Установить задержку 45 секунд"):
        page.set_delay(45)

    with allure.step("Нажать кнопки 7 + 8 ="):
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

    with allure.step("Дождаться результата и проверить, что он равен 15"):
        result = page.get_result(timeout=50)
        assert result == "15", f"Expected result 15, got '{result}'"
