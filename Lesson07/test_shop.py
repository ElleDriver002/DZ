from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_saucedemo_checkout():
    """
    Test the Sauce Demo shop flow:
    - Login as standard_user
    - Add three products to cart
    - Checkout and fill form
    - Assert total is $58.29
    """
    options = Options()
    # Раскомментируйте при необходимости headless-режима:
    # options.add_argument("-headless")

    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install()),
        options=options,
    )

    try:
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.add_to_cart("Sauce Labs Backpack")
        inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
        inventory_page.add_to_cart("Sauce Labs Onesie")
        inventory_page.go_to_cart()

        cart_page = CartPage(driver)
        cart_page.click_checkout()

        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form("Ivan", "Ivanov", "123456")
        checkout_page.click_continue()

        total = checkout_page.get_total()
        # total выглядит как "Total: $58.29"
        assert "$58.29" in total, f"Expected total $58.29, got '{total}'"
    finally:
        driver.quit()


if __name__ == "__main__":
    test_saucedemo_checkout()
    print("Shop test passed")
