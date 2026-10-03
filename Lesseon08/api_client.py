"""Клиент YouGile API для работы с проектами (слой в духе Page Object)."""
import requests

from config import BASE_URL, HEADERS


class ProjectsApi:
    """Обёртка над эндпоинтами /projects."""

    def __init__(self, base_url=None, headers=None):
        self.base_url = base_url or BASE_URL
        self.headers = headers or HEADERS
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def create_project(self, payload):
        """POST /projects — создание проекта. Успех: 201."""
        url = f"{self.base_url}/projects"
        return self.session.post(url, json=payload)

    def get_project(self, project_id):
        """GET /projects/{id} — получение проекта. Успех: 200."""
        url = f"{self.base_url}/projects/{project_id}"
        return self.session.get(url)

    def update_project(self, project_id, payload):
        """PUT /projects/{id} — изменение проекта. Успех: 200."""
        url = f"{self.base_url}/projects/{project_id}"
        return self.session.put(url, json=payload)

    def delete_project(self, project_id):
        """Мягкое удаление: PUT с deleted=true."""
        return self.update_project(project_id, {"deleted": True})
