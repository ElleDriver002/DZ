"""Page Object for the Sauce Demo cart page."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """Page Object for the Sauce Demo cart page."""

    CHECKOUT_BUTTON: tuple[str, str] = (By.ID, "checkout")
    CART_ITEMS: tuple[str, str] = (By.CLASS_NAME, "cart_item")

    def __init__(self, driver: WebDriver) -> None:
        """
        Initialize CartPage.

        :param driver: Selenium WebDriver instance
        """
        self.driver = driver

    def click_checkout(self) -> None:
        """Click the Checkout button."""
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    def get_cart_items_count(self) -> int:
        """
        Return the number of items currently in the cart.

        :return: number of cart items
        """
        return len(self.driver.find_elements(*self.CART_ITEMS))
