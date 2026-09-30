from selenium.webdriver.common.by import By


class InventoryPage:
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_name: str):
        button_id = f"add-to-cart-{product_name}"
        self.driver.find_element(By.ID, button_id).click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
