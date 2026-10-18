"""Page Object for the Sauce Demo inventory (main shop) page."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    """Page Object for the Sauce Demo inventory (main shop) page."""

    PRODUCT_BUTTONS: dict[str, str] = {
        "Sauce Labs Backpack": "add-to-cart-sauce-labs-backpack",
        "Sauce Labs Bolt T-Shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
        "Sauce Labs Onesie": "add-to-cart-sauce-labs-onesie",
    }

    CART_LINK: tuple[str, str] = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver: WebDriver) -> None:
        """
        Initialize InventoryPage.

        :param driver: Selenium WebDriver instance
        """
        self.driver = driver

    def add_to_cart(self, product_name: str) -> None:
        """
        Add a product to the cart by its name.

        :param product_name: display name of the product
        """
        data_test: str = self.PRODUCT_BUTTONS[product_name]
        locator: tuple[str, str] = (
            By.CSS_SELECTOR,
            f"[data-test='{data_test}']",
        )
        self.driver.find_element(*locator).click()

    def go_to_cart(self) -> None:
        """Navigate to the shopping cart."""
        self.driver.find_element(*self.CART_LINK).click()
