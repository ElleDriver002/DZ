from selenium.webdriver.common.by import By


class CheckoutPage:
    """Page Object for the Sauce Demo checkout pages (info + overview)."""

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver

    def fill_form(self, first_name, last_name, postal_code):
        """Fill the checkout information form."""
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(postal_code)

    def click_continue(self):
        """Click the Continue button to go to the overview page."""
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_total(self):
        """Return the total amount text from the overview page."""
        return self.driver.find_element(*self.TOTAL_LABEL).text
