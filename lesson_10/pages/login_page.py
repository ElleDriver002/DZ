"""Page Object for the Sauce Demo login page."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class LoginPage:
    """Page Object for the Sauce Demo login page."""

    URL: str = "https://www.saucedemo.com/"

    USERNAME_INPUT: tuple[str, str] = (By.ID, "user-name")
    PASSWORD_INPUT: tuple[str, str] = (By.ID, "password")
    LOGIN_BUTTON: tuple[str, str] = (By.ID, "login-button")

    def __init__(self, driver: WebDriver) -> None:
        """
        Initialize LoginPage.

        :param driver: Selenium WebDriver instance
        """
        self.driver = driver

    def open(self) -> None:
        """Open the login page."""
        self.driver.get(self.URL)

    def enter_username(self, username: str) -> None:
        """
        Enter username into the username field.

        :param username: username string
        """
        element: WebElement = self.driver.find_element(*self.USERNAME_INPUT)
        element.send_keys(username)

    def enter_password(self, password: str) -> None:
        """
        Enter password into the password field.

        :param password: password string
        """
        element: WebElement = self.driver.find_element(*self.PASSWORD_INPUT)
        element.send_keys(password)

    def click_login(self) -> None:
        """Click the login button."""
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, username: str, password: str) -> None:
        """
        Perform full login with given credentials.

        :param username: username string
        :param password: password string
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
