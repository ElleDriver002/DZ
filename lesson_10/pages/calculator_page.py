"""Page Object for the slow calculator page."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    """Page Object for the slow calculator page."""

    URL: str = (
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    DELAY_INPUT: tuple[str, str] = (By.CSS_SELECTOR, "#delay")
    SCREEN: tuple[str, str] = (By.CSS_SELECTOR, ".screen")
    BUTTON_TEMPLATE: tuple[str, str] = (By.XPATH, "//span[text()='{}']")

    def __init__(self, driver: WebDriver) -> None:
        """
        Initialize CalculatorPage.

        :param driver: Selenium WebDriver instance
        """
        self.driver = driver

    def open(self) -> None:
        """Open the calculator page."""
        self.driver.get(self.URL)

    def set_delay(self, value: int) -> None:
        """
        Set the delay value in the delay input field.

        :param value: delay in seconds
        """
        delay_field = self.driver.find_element(*self.DELAY_INPUT)
        delay_field.clear()
        delay_field.send_keys(str(value))

    def click_button(self, button_text: str) -> None:
        """
        Click a calculator button by its text (digit or operator).

        :param button_text: button label, e.g. '7', '+', '='
        """
        locator: tuple[str, str] = (
            self.BUTTON_TEMPLATE[0],
            self.BUTTON_TEMPLATE[1].format(button_text),
        )
        self.driver.find_element(*locator).click()

    def get_result(self, timeout: int = 50) -> str:
        """
        Wait until the result appears on the screen and return it.

        Timeout should be greater than the configured delay.

        :param timeout: maximum wait time in seconds
        :return: text from the calculator screen
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            lambda d: d.find_element(*self.SCREEN).text.strip()
            not in ("", "7", "7+", "7+8")
        )
        return self.driver.find_element(*self.SCREEN).text.strip()
