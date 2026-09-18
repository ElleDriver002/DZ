from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()

    # ===== РЕАЛЬНЫЕ cookie двух аккаунтов =====
    cookie_user1 = {
        "name": "session",
        "value": "NGJlNzRjMTMtNTE2NS00ZmRmLTg1ZGEtOGJkOGI2NzA2ZTgy",
        "domain": ".gitflic.ru",
        "path": "/"
    }

    cookie_user2 = {
        "name": "session",
        "value": "ZTU5MTA4ZTEtNzRjMC00YTA1LTk0NzctMWZiZGMxNmMyMWQz",
        "domain": ".gitflic.ru",
        "path": "/"
    }

    # ---------- Пользователь 1 ----------
    # 1. Открыть главную
    driver.get("https://gitflic.ru/")

    # 2. Установить cookie user1
    driver.add_cookie(cookie_user1)

    # 3. Обновить страницу (чтобы cookie применились)
    driver.refresh()

    # 4. Перейти на страницу профиля user1
    driver.get("https://gitflic.ru/user/aelle-driver")

    # 5. Сохранить URL
    url_user1 = driver.current_url

    # ---------- Выход ----------
    # 6. Очистить все cookie
    driver.delete_all_cookies()

    # ---------- Пользователь 2 ----------
    # 7. Снова открыть домен (обязательно перед add_cookie)
    driver.get("https://gitflic.ru/")

    # Установить cookie user2
    driver.add_cookie(cookie_user2)

    # 8. Обновить страницу
    driver.refresh()

    # 9. Перейти на страницу профиля user2
    driver.get("https://gitflic.ru/user/olyase")

    # 10. Сохранить URL
    url_user2 = driver.current_url

    # 11. Проверить, что URL разные
    assert url_user1 != url_user2

    driver.quit()
