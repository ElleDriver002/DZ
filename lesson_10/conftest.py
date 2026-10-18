"""Pytest fixtures for UI tests."""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def chrome_driver() -> WebDriver:
    """
    Create and quit a Chrome WebDriver instance.

    :return: Chrome WebDriver
    """
    options = ChromeOptions()
    # Uncomment for headless CI runs:
    # options.add_argument("--headless=new")
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options,
    )
    yield driver
    driver.quit()


@pytest.fixture
def firefox_driver() -> WebDriver:
    """
    Create and quit a Firefox WebDriver instance.

    :return: Firefox WebDriver
    """
    options = FirefoxOptions()
    # Uncomment for headless CI runs:
    # options.add_argument("-headless")

    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install()),
        options=options,
    )
    yield driver
    driver.quit()
