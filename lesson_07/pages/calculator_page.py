from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    def set_delay(self, value: str):
        delay = self.driver.find_element(*self.DELAY_INPUT)
        delay.clear()
        delay.send_keys(value)

    def click_button(self, button_text: str):
        locator = (By.XPATH, f"//span[text()='{button_text}']")
        self.driver.find_element(*locator).click()

    def get_result(self) -> str:
        self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, "15")
        )
        return self.driver.find_element(*self.SCREEN).text.strip()
