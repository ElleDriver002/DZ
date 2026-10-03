"""Конфигурация тестов YouGile API.

Токен и URL берутся из переменных окружения — в коде секретов нет.

Наставнику перед запуском:
    export YOUGILE_API_TOKEN="ваш_api_ключ"
    # опционально (по умолчанию https://ru.yougile.com/api-v2):
    export YOUGILE_BASE_URL="https://ru.yougile.com/api-v2"
"""
import os

BASE_URL = os.getenv("YOUGILE_BASE_URL", "https://ru.yougile.com/api-v2")
TOKEN = os.getenv("YOUGILE_API_TOKEN", "")

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {TOKEN}",
}
