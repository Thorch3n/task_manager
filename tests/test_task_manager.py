import pytest
from models import TaskManager


@pytest.fixture
def task_manager():
    """Фикстура для создания менеджера задач с пустым файлом"""
    manager = TaskManager('test_data.json')
    yield manager
    try:
        import os
        os.remove('test_data.json')
    except:
        pass


def test_add_task(task_manager):
    """Проверка добавления задачи"""
    task_manager.add_task("Задача 1", "Описание задачи 1", "Работа", "31-12-2024", "Низкий")

    assert len(task_manager.tasks) == 1
    assert task_manager.tasks[0].title == "Задача 1"
    assert task_manager.tasks[0].description == "Описание задачи 1"
    assert task_manager.tasks[0].category == "Работа"
    assert task_manager.tasks[0].due_date == "31-12-2024"
    assert task_manager.tasks[0].priority == "Низкий"


def test_edit_task(task_manager):
    """Проверка редактирования задачи"""
    task_manager.add_task("Задача 1", "Описание задачи 1", "Работа", "31-12-2024", "Низкий")
    task_id = task_manager.tasks[0].id
    task_manager.edit_task(task_id, title="Задача 1 (редактированная)",
                           description="Описание задачи 1 (редактированное)", due_date="01-01-2025")

    assert task_manager.tasks[0].title == "Задача 1 (редактированная)"
    assert task_manager.tasks[0].description == "Описание задачи 1 (редактированное)"
    assert task_manager.tasks[0].due_date == "01-01-2025"


def test_find_tasks_by_keyword(task_manager):
    """Проверка поиска задач по ключевому слову"""
    task_manager.add_task("Задача 1", "Описание задачи 1", "Работа", "31-12-2024", "Низкий")
    task_manager.add_task("Задача 2", "Описание задачи 2", "Личное", "31-12-2024", "Средний")

    tasks = task_manager.find_tasks(keyword="Задача 1")

    assert len(tasks) == 1
    assert tasks[0].title == "Задача 1"


def test_delete_task_by_id(task_manager):
    """Проверка удаления задачи по ID"""
    task_manager.add_task("Задача 1", "Описание задачи 1", "Работа", "31-12-2024", "Низкий")
    task_id = task_manager.tasks[0].id
    task_manager.delete_task(task_id)

    assert len(task_manager.tasks) == 0
