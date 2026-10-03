# Lesson 08 — автотесты YouGile API (проекты)

Тестируемые методы (официальная документация):

- [POST /api-v2/projects](https://ru.yougile.com/api-v2#/operations/ProjectController_create) — создание (201)
- [PUT /api-v2/projects/{id}](https://ru.yougile.com/api-v2#/operations/ProjectController_update) — изменение (200 / 404)
- [GET /api-v2/projects/{id}](https://ru.yougile.com/api-v2#/operations/ProjectController_get) — получение (200 / 404)

## Установка

```bash
pip install -r lesson_08/requirements.txt
```

## Настройка для наставника

Токен **не** хранится в репозитории. Перед запуском:

```bash
# Linux / macOS
export YOUGILE_API_TOKEN="ваш_api_ключ"

# опционально (по умолчанию https://ru.yougile.com/api-v2)
export YOUGILE_BASE_URL="https://ru.yougile.com/api-v2"
```

Windows (PowerShell):

```powershell
$env:YOUGILE_API_TOKEN = "ваш_api_ключ"
```

Как получить API-ключ:
https://help.yougile.com/books/baza-znanii-yougile/page/rest-api-v20-v-yougile

## Запуск

```bash
pytest lesson_08 -v
```

## Проверка стиля

```bash
flake8 lesson_08
```

## Структура

| Файл | Описание |
|------|----------|
| `config.py` | BASE_URL, TOKEN из env |
| `api_client.py` | Обёртка Requests (Page Object) |
| `conftest.py` | Фикстуры pytest |
| `test_projects.py` | Позитивные и негативные тесты |

## Покрытие

| Метод | Позитивные | Негативные |
|-------|------------|------------|
| POST | создание с title → 201 + id | без title; пустой title |
| GET | получение созданного → 200 + поля | несуществующий id → 404; невалидный id |
| PUT | смена title → 200 + проверка GET | несуществующий id → 404; невалидный id |

Тесты стабильны: каждый создаёт нужные данные и очищает их (soft-delete через PUT `deleted: true`).
