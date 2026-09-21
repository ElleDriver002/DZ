from selenium.webdriver.common.by import By


class LoginPage:
    """Page Object for the Sauce Demo login page."""

    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Open the login page."""
        self.driver.get(self.URL)

    def enter_username(self, username):
        """Enter username into the username field."""
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        """Enter password into the password field."""
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        """Click the login button."""
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, username, password):
        """Perform full login with given credentials."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
