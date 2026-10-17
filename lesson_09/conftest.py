import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Строка подключения (trust-режим, пароль не нужен)
DATABASE_URL = (
    "postgresql+psycopg://postgres@localhost:5432/mydatabase"
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


@pytest.fixture
def db_session():
    """Фикстура сессии SQLAlchemy. После теста сессия закрывается."""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
