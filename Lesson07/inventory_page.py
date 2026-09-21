from selenium.webdriver.common.by import By


class InventoryPage:
    """Page Object for the Sauce Demo inventory (main shop) page."""

    PRODUCT_BUTTONS = {
        "Sauce Labs Backpack": "add-to-cart-sauce-labs-backpack",
        "Sauce Labs Bolt T-Shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
        "Sauce Labs Onesie": "add-to-cart-sauce-labs-onesie",
    }

    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_name):
        """Add a product to the cart by its name."""
        data_test = self.PRODUCT_BUTTONS[product_name]
        locator = (By.CSS_SELECTOR, f"[data-test='{data_test}']")
        self.driver.find_element(*locator).click()

    def go_to_cart(self):
        """Navigate to the shopping cart."""
        self.driver.find_element(*self.CART_LINK).click()
