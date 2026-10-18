"""Тесты каталога товаров на Sauce Demo."""

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@allure.feature("Каталог")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Добавление товара в корзину")
@allure.description(
    "Проверяет, что после добавления рюкзака в корзину "
    "бейдж корзины показывает количество 1."
)
def test_add_item_to_cart(driver: WebDriver) -> None:
    """Добавление товара в корзину."""
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    with allure.step("Открыть сайт и авторизоваться"):
        login_page.open_page()
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавить Sauce Labs Backpack в корзину"):
        inventory_page.add_backpack_to_cart()

    with allure.step("Проверить, что в корзине 1 товар"):
        assert inventory_page.get_cart_count() == "1"
