from models import Student


def test_add_student(db_session):
    """Тест добавления нового студента."""
    student = Student(first_name="Иван", last_name="Иванов")
    db_session.add(student)
    db_session.commit()

    # Проверяем, что студент появился в БД
    saved = db_session.query(Student).filter_by(
        first_name="Иван", last_name="Иванов"
    ).first()

    assert saved is not None
    assert saved.first_name == "Иван"
    assert saved.last_name == "Иванов"

    # Удаляем за собой
    db_session.delete(saved)
    db_session.commit()


def test_update_student(db_session):
    """Тест изменения существующего студента."""
    # Создаём студента
    student = Student(first_name="Пётр", last_name="Петров")
    db_session.add(student)
    db_session.commit()

    # Изменяем данные
    student.first_name = "Алексей"
    student.last_name = "Сидоров"
    db_session.commit()

    # Проверяем обновлённые данные
    updated = db_session.query(Student).filter_by(id=student.id).first()
    assert updated is not None
    assert updated.first_name == "Алексей"
    assert updated.last_name == "Сидоров"

    # Удаляем за собой
    db_session.delete(updated)
    db_session.commit()


def test_delete_student(db_session):
    """Тест удаления студента."""
    # Создаём студента
    student = Student(first_name="Сергей", last_name="Сергеев")
    db_session.add(student)
    db_session.commit()
    student_id = student.id

    # Удаляем
    db_session.delete(student)
    db_session.commit()

    # Проверяем, что студента больше нет
    deleted = db_session.query(Student).filter_by(id=student_id).first()
    assert deleted is None
