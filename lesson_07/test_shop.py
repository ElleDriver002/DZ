from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_shop():
    driver = webdriver.Firefox()
    try:
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory = InventoryPage(driver)
        inventory.add_to_cart("sauce-labs-backpack")
        inventory.add_to_cart("sauce-labs-bolt-t-shirt")
        inventory.add_to_cart("sauce-labs-onesie")
        inventory.go_to_cart()

        cart = CartPage(driver)
        cart.click_checkout()

        checkout = CheckoutPage(driver)
        checkout.fill_form("Иван", "Иванов", "123456")

        total = checkout.get_total()
        assert total == "Total: $58.29"
    finally:
        driver.quit()
