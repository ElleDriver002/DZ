"""Тесты авторизации на Sauce Demo."""

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@allure.feature("Авторизация")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Успешный вход с валидными данными")
@allure.description(
    "Проверяет, что пользователь standard_user может войти "
    "в систему и попасть на страницу каталога товаров."
)
def test_successful_login(driver: WebDriver) -> None:
    """Успешный логин standard_user."""
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    with allure.step("Открыть страницу логина"):
        login_page.open_page()

    with allure.step("Ввести валидные учётные данные и нажать Login"):
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Проверить, что открылась страница каталога"):
        assert inventory_page.is_inventory_displayed(), (
            "Список товаров не отображается"
        )
        assert inventory_page.get_title() == "Products"


@allure.feature("Авторизация")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Ошибка входа при неверном пароле")
@allure.description(
    "Проверяет, что при вводе неверного пароля "
    "отображается сообщение об ошибке."
)
def test_login_with_wrong_password(driver: WebDriver) -> None:
    """Логин с неверным паролем."""
    login_page = LoginPage(driver)

    with allure.step("Открыть страницу логина"):
        login_page.open_page()

    with allure.step("Ввести логин и неверный пароль"):
        login_page.login("standard_user", "wrong_password")

    with allure.step("Проверить наличие сообщения об ошибке"):
        assert login_page.is_error_displayed(), "Сообщение об ошибке не видно"
        error_text = login_page.get_error_message()
        assert "Username and password do not match" in error_text


@allure.feature("Авторизация")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Ошибка входа для заблокированного пользователя")
@allure.description(
    "Проверяет, что locked_out_user не может войти "
    "и видит соответствующее сообщение."
)
def test_locked_out_user(driver: WebDriver) -> None:
    """Логин заблокированным пользователем."""
    login_page = LoginPage(driver)

    with allure.step("Открыть страницу логина"):
        login_page.open_page()

    with allure.step("Войти как locked_out_user"):
        login_page.login("locked_out_user", "secret_sauce")

    with allure.step("Проверить сообщение о блокировке"):
        assert login_page.is_error_displayed()
        error_text = login_page.get_error_message()
        assert "locked out" in error_text.lower()
