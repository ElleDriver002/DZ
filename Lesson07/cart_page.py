from selenium.webdriver.common.by import By


class CartPage:
    """Page Object for the Sauce Demo cart page."""

    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")

    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        """Click the Checkout button."""
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    def get_cart_items_count(self):
        """Return the number of items currently in the cart."""
        return len(self.driver.find_elements(*self.CART_ITEMS))
