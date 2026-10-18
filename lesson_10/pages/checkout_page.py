"""Page Object for the Sauce Demo checkout pages (info + overview)."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """Page Object for the Sauce Demo checkout pages (info + overview)."""

    FIRST_NAME_INPUT: tuple[str, str] = (By.ID, "first-name")
    LAST_NAME_INPUT: tuple[str, str] = (By.ID, "last-name")
    POSTAL_CODE_INPUT: tuple[str, str] = (By.ID, "postal-code")
    CONTINUE_BUTTON: tuple[str, str] = (By.ID, "continue")
    TOTAL_LABEL: tuple[str, str] = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver: WebDriver) -> None:
        """
        Initialize CheckoutPage.

        :param driver: Selenium WebDriver instance
        """
        self.driver = driver

    def fill_form(
        self,
        first_name: str,
        last_name: str,
        postal_code: str,
    ) -> None:
        """
        Fill the checkout information form.

        :param first_name: customer first name
        :param last_name: customer last name
        :param postal_code: postal / ZIP code
        """
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(
            postal_code
        )

    def click_continue(self) -> None:
        """Click the Continue button to go to the overview page."""
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_total(self) -> str:
        """
        Return the total amount text from the overview page.

        :return: total label text (e.g. 'Total: $58.29')
        """
        return self.driver.find_element(*self.TOTAL_LABEL).text
