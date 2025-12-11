import pytest
import sqlite3
import os
from logic import insert_project

@pytest.fixture(scope="module")
def setup_database():
    """Фикстура для настройки базы данных перед тестами и её очистки после."""
   
    yield
    try:
        os.remove('users.db')
    except PermissionError:
        pass

@pytest.fixture
def connection():
    """Фикстура для получения соединения с базой данных и его закрытия после теста."""
    conn = sqlite3.connect('users.db')
    yield conn
    conn.close()


def test_add_user(setup_database, connection):
    insert_project('fg','8034034072')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Questions WHERE Email='fg';")
    user = cursor.fetchone()
    assert user, "Пользователь должен быть добавлен в базу данных."