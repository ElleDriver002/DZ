"""Tests for the Sauce Demo shop checkout flow."""

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Магазин")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Покупка трёх товаров: итоговая сумма $58.29")
@allure.description(
    "Авторизация standard_user, добавление трёх товаров в корзину, "
    "оформление заказа и проверка итоговой суммы $58.29."
)
def test_saucedemo_checkout(firefox_driver: WebDriver) -> None:
    """
    Test the Sauce Demo shop flow:
    - Login as standard_user
    - Add three products to cart
    - Checkout and fill form
    - Assert total is $58.29
    """
    driver = firefox_driver

    with allure.step("Открыть сайт и войти как standard_user"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавить три товара в корзину и перейти в корзину"):
        inventory_page = InventoryPage(driver)
        inventory_page.add_to_cart("Sauce Labs Backpack")
        inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
        inventory_page.add_to_cart("Sauce Labs Onesie")
        inventory_page.go_to_cart()

    with allure.step("Нажать Checkout"):
        cart_page = CartPage(driver)
        cart_page.click_checkout()

    with allure.step("Заполнить форму покупателя и продолжить"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form("Ivan", "Ivanov", "123456")
        checkout_page.click_continue()

    with allure.step("Проверить, что итоговая сумма содержит $58.29"):
        total = checkout_page.get_total()
        assert "$58.29" in total, f"Expected total $58.29, got '{total}'"
