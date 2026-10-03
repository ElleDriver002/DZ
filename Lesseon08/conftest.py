"""Фикстуры pytest для тестов YouGile API."""
import uuid

import pytest

from api_client import ProjectsApi
from config import TOKEN


@pytest.fixture(scope="session")
def api():
    """Общий клиент API на всю сессию."""
    if not TOKEN:
        pytest.skip(
            "Не задана переменная окружения YOUGILE_API_TOKEN. "
            "Укажите API-ключ YouGile для запуска тестов."
        )
    return ProjectsApi()


@pytest.fixture
def created_project(api):
    """Создаёт проект перед тестом и мягко удаляет после."""
    title = f"test_project_{uuid.uuid4().hex[:8]}"
    response = api.create_project({"title": title})
    assert response.status_code == 201, (
        f"Не удалось создать проект: {response.status_code} {response.text}"
    )
    project_id = response.json()["id"]
    yield {"id": project_id, "title": title}
    api.delete_project(project_id)
