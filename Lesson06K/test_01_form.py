from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import platform


def test_form_validation():
    system = platform.system()

    if system == "Windows":
        # Edge (Windows)
        options = webdriver.EdgeOptions()
        driver = webdriver.Edge(options=options)
    elif system == "Darwin":
        # Safari (macOS)
        driver = webdriver.Safari()
    else:
        # Fallback для Linux
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

    try:
        wait = WebDriverWait(driver, 10)
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        )

        wait.until(
            EC.presence_of_element_located((By.NAME, "first-name"))
        ).send_keys("Иван")
        driver.find_element(By.NAME, "last-name").send_keys("Петров")
        driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
        driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
        driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
        # Zip code оставляем пустым
        driver.find_element(By.NAME, "city").send_keys("Москва")
        driver.find_element(By.NAME, "country").send_keys("Россия")
        driver.find_element(By.NAME, "job-position").send_keys("QA")
        driver.find_element(By.NAME, "company").send_keys("SkyPro")

        submit_btn = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[type=submit]")
            )
        )
        driver.execute_script(
            "arguments[0].scrollIntoView(true);", submit_btn
        )
        driver.execute_script("arguments[0].click();", submit_btn)

        wait.until(EC.presence_of_element_located((By.ID, "zip-code")))

        # Zip code — красный
        zip_code = driver.find_element(By.ID, "zip-code")
        assert "alert-danger" in zip_code.get_attribute("class")

        # Остальные — зелёные
        success_fields = [
            "first-name", "last-name", "address", "city",
            "country", "e-mail", "phone", "job-position", "company",
        ]
        for field_id in success_fields:
            element = driver.find_element(By.ID, field_id)
            assert "alert-success" in element.get_attribute("class"), (
                f"Поле {field_id} не подсвечено зелёным"
            )
    finally:
        driver.quit()
