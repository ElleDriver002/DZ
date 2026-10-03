"""Автотесты YouGile API: POST, PUT, GET /api-v2/projects.

Документация:
  POST  https://ru.yougile.com/api-v2#/operations/ProjectController_create
  PUT   https://ru.yougile.com/api-v2#/operations/ProjectController_update
  GET   https://ru.yougile.com/api-v2#/operations/ProjectController_get
"""
import uuid


# ---------------------------------------------------------------------------
# POST /api-v2/projects  (успех: 201, тело ответа: {"id": "..."})
# ---------------------------------------------------------------------------


def test_create_project_positive(api):
    """Позитивный: создание проекта с валидным title."""
    title = f"pytest_create_{uuid.uuid4().hex[:8]}"
    response = api.create_project({"title": title})

    assert response.status_code == 201
    body = response.json()
    assert "id" in body
    assert isinstance(body["id"], str)
    assert len(body["id"]) > 0

    api.delete_project(body["id"])


def test_create_project_without_title_negative(api):
    """Негативный: создание проекта без обязательного поля title."""
    response = api.create_project({})

    assert response.status_code >= 400
    # Проверяем, что API вернул описание ошибки
    assert response.text
    body = response.json()
    assert body, "Ожидалось тело ответа с описанием ошибки"


def test_create_project_empty_title_negative(api):
    """Негативный: создание проекта с пустым title."""
    response = api.create_project({"title": ""})

    assert response.status_code >= 400
    assert response.text
    body = response.json()
    assert body, "Ожидалось тело ответа с описанием ошибки"


# ---------------------------------------------------------------------------
# GET /api-v2/projects/{id}  (успех: 200 ProjectDto, ошибка: 404)
# ---------------------------------------------------------------------------


def test_get_project_positive(api, created_project):
    """Позитивный: получение существующего проекта по id."""
    project_id = created_project["id"]
    expected_title = created_project["title"]

    response = api.get_project(project_id)

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == project_id
    assert body["title"] == expected_title
    assert "timestamp" in body
    # поле deleted может отсутствовать, если проект не удалён
    assert body.get("deleted", False) is False


def test_get_project_not_found_negative(api):
    """Негативный: получение проекта с несуществующим id."""
    fake_id = str(uuid.uuid4())
    response = api.get_project(fake_id)

    assert response.status_code == 404
    # API возвращает ошибку (текст или JSON)
    assert response.text is not None


def test_get_project_invalid_id_negative(api):
    """Негативный: получение проекта с невалидным id."""
    response = api.get_project("not-a-valid-uuid")

    assert response.status_code >= 400
    assert response.text is not None


# ---------------------------------------------------------------------------
# PUT /api-v2/projects/{id}  (успех: 200 {"id": "..."}, ошибка: 404)
# ---------------------------------------------------------------------------


def test_update_project_positive(api, created_project):
    """Позитивный: обновление title существующего проекта."""
    project_id = created_project["id"]
    new_title = f"updated_{uuid.uuid4().hex[:8]}"

    response = api.update_project(project_id, {"title": new_title})

    assert response.status_code == 200
    body = response.json()
    assert body["id"] == project_id

    # Проверяем, что изменения сохранились
    get_response = api.get_project(project_id)
    assert get_response.status_code == 200
    assert get_response.json()["title"] == new_title


def test_update_project_not_found_negative(api):
    """Негативный: обновление проекта с несуществующим id."""
    fake_id = str(uuid.uuid4())
    response = api.update_project(fake_id, {"title": "should_fail"})

    assert response.status_code == 404
    assert response.text is not None


def test_update_project_invalid_id_negative(api):
    """Негативный: обновление проекта с невалидным id."""
    response = api.update_project("invalid-id", {"title": "should_fail"})

    assert response.status_code >= 400
    assert response.text is not None
