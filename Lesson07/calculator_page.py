from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    """Page Object for the slow calculator page."""

    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")
    BUTTON_TEMPLATE = (By.XPATH, "//span[text()='{}']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Open the calculator page."""
        self.driver.get(self.URL)

    def set_delay(self, value):
        """Set the delay value in the delay input field."""
        delay_field = self.driver.find_element(*self.DELAY_INPUT)
        delay_field.clear()
        delay_field.send_keys(str(value))

    def click_button(self, button_text):
        """Click a calculator button by its text (digit or operator)."""
        locator = (
            self.BUTTON_TEMPLATE[0],
            self.BUTTON_TEMPLATE[1].format(button_text),
        )
        self.driver.find_element(*locator).click()

    def get_result(self, timeout=50):
        """
        Wait until the result appears on the screen and return it.
        Timeout should be greater than the configured delay.
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            lambda d: d.find_element(*self.SCREEN).text.strip()
            not in ("", "7", "7+", "7+8")
        )
        return self.driver.find_element(*self.SCREEN).text.strip()
