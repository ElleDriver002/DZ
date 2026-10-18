"""Базовый класс страницы (Page Object)."""

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Базовый Page Object с общими методами работы со страницей."""

    def __init__(self, driver: WebDriver, timeout: int = 10) -> None:
        """
        Инициализация базовой страницы.

        :param driver: экземпляр WebDriver
        :param timeout: время ожидания элементов в секундах
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url: str) -> None:
        """
        Открыть указанный URL.

        :param url: адрес страницы
        """
        self.driver.get(url)

    def find(self, locator: tuple[str, str]) -> WebElement:
        """
        Найти элемент по локатору.

        :param locator: кортеж (By, value)
        :return: найденный WebElement
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_visible(self, locator: tuple[str, str]) -> WebElement:
        """
        Найти видимый элемент по локатору.

        :param locator: кортеж (By, value)
        :return: найденный WebElement
        """
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator: tuple[str, str]) -> None:
        """
        Кликнуть по элементу.

        :param locator: кортеж (By, value)
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def type_text(self, locator: tuple[str, str], text: str) -> None:
        """
        Очистить поле и ввести текст.

        :param locator: кортеж (By, value)
        :param text: текст для ввода
        """
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple[str, str]) -> str:
        """
        Получить текст элемента.

        :param locator: кортеж (By, value)
        :return: текст элемента
        """
        return self.find_visible(locator).text

    def is_visible(self, locator: tuple[str, str]) -> bool:
        """
        Проверить, виден ли элемент.

        :param locator: кортеж (By, value)
        :return: True, если элемент виден, иначе False
        """
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def get_current_url(self) -> str:
        """
        Получить текущий URL страницы.

        :return: текущий URL
        """
        return self.driver.current_url
